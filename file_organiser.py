from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil
from extensions import directory, file_type

FOLDER_TO_TRACK = '/home/msz/Downloads'
FOLDER_DESTINATION = FOLDER_TO_TRACK + '/sorted'

def get_key(suffix):
    for key, value in file_type.items():
        for v in value:
            if suffix == v:
                return key


class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        for filename in os.listdir(FOLDER_TO_TRACK):
            i = 1
            if filename != 'sorted':
                try:
                    new_name = filename
                    extension = 'unspecified'
                    extension = str(os.path.splitext(FOLDER_TO_TRACK + '/' + filename)[1]) # stores extension of the new file
                    
                    suffix_type = get_key(extension) # use get_key function
                    if suffix_type == None:
                        suffix_type = 'unspecified'

                    if not os.path.exists(FOLDER_DESTINATION + '/' + suffix_type):
                        os.makedirs(FOLDER_DESTINATION + '/' + suffix_type)
                        print('Created folder(s): ' + FOLDER_DESTINATION + '/' + suffix_type)

                    file_exists = os.path.isfile(directory[suffix_type] + "/" + new_name)

                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(FOLDER_TO_TRACK + "/" + new_name)[0] \
                        + str(i) + os.path.splitext(FOLDER_TO_TRACK + "/" + new_name)[1]
                        new_name = new_name.split("/")[-1]
                        file_exists = os.path.isfile(directory[suffix_type] + "/" + new_name)

                    src = FOLDER_TO_TRACK + "/" + filename
                    new_name = directory[suffix_type] + "/" + new_name
                    os.rename(src, new_name)
                
                except Exception:
                    print(filename)

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, FOLDER_TO_TRACK, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
