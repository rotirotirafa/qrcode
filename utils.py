import os

from settings import BASE_PATH, FILE_PATH


def create_files_directory():
    try:
        files_path = os.path.join(BASE_PATH, FILE_PATH)
        os.mkdir(files_path)
        print(f'{files_path} Created!!!')
        return True
    except Exception as ex:
        msg = f'Not able to create /files directory -> {ex}'
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
