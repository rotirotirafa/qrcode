import os, logging
from exceptions import DirectoryExists

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = 'files'
URL_PATH = f'{BASE_PATH}/{FILE_PATH}'

def create_files_directory():
    try:
        files_path = os.path.join(BASE_PATH, FILE_PATH)
        os.mkdir(files_path)
        print(f'{files_path} Created!!!')
        return True
    except Exception as ex:
        msg = f'Not able to create /files directory -> {ex}'
        logging.error(msg)
        print(msg)
        return False

def remove_files_directory():
    try:
        files_path = os.path.join(BASE_PATH, FILE_PATH)
        if files_path:
            os.rmdir(files_path)
            return True
        return None
    except Exception as ex:
        msg = f'Not able to REMOVE /files directory -> {ex}'
        logging.error(msg)
        print(msg)

try:
    if os.path.exists('files') is False:
        print('Creating FILES path..')
        create_files_directory()
    else:
        print('/files direcotory is already there.')
        pass
    
except Exception as ex:
    print(f'Not able to create /files directory -> {ex}')
    pass