FOLDER_TO_TRACK = '/home/msz/Downloads'
FOLDER_DESTINATION = FOLDER_TO_TRACK + '/sorted'

directory = {
        'unspecified': FOLDER_DESTINATION + '/unspecified',
        'text': FOLDER_DESTINATION + '/text',
        'audio': FOLDER_DESTINATION + '/audio',
        'video': FOLDER_DESTINATION + '/video',
        'images': FOLDER_DESTINATION + '/images',
        'internet': FOLDER_DESTINATION + '/internet',
        'compressed': FOLDER_DESTINATION + '/compressed',
        'disc': FOLDER_DESTINATION + '/disc',
        'data': FOLDER_DESTINATION + '/data',
        'executables': FOLDER_DESTINATION + '/executables',
        'fonts': FOLDER_DESTINATION + '/fonts',
        'presentations': FOLDER_DESTINATION + '/presentations',
        'programming': FOLDER_DESTINATION + '/programming',
        'spreadsheets': FOLDER_DESTINATION + '/spreadsheets',
        'system': FOLDER_DESTINATION + '/system'
        }
file_type = {
        'text': ['.txt', '.doc', '.docx', '.odt', '.pdf', '.rtf', '.tex', '.aux', '.wks', '.wps', '.wpd'],
        'audio': ['.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', 'wma', '.wpl', '.m3u'],
        'video': ['.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv'],
        'images': ['.ai', '.bmp', '.gif', '.jpg', '.jpeg', '.png', '.ps', '.psd', '.svg', '.tif', '.tiff', '.cr2'],
        'internet': ['.asp', '.aspx', '.cer', '.cfm', '.cgi', '.pl', '.css', '.htm', '.js', '.jsp', '.part', '.php', '.rss', '.xhtml', '.html'],
        'compressed': ['.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip'],
        'disc': ['.bin', '.dmg', '.iso', '.toast', '.vcd'],
        'data': ['.csv', '.tsv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.tar', '.xml', '.json'],
        'executables': ['.apk', '.bat', '.com', '.exe', '.gadget', '.jar', '.wsf', '.AppImage'],
        'fonts': ['.fnt', '.fon', '.otf', '.ttf'],
        'presentations': ['.key', '.odp', '.pps', '.ppt', '.pptx'],
        'programming': ['.c', '.class', '.java', '.py', '.sh', '.h', '.ino'],
        'spreadsheets': ['.ods', '.xlr', '.xls', '.xlsx'],
        'system': ['.bak', '.cab', '.dll', '.dmp', '.drv', '.icns', '.ico', '.ini', '.lnk', '.msi', '.sys', '.tmp']
        }

