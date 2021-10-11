import os, logging

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = 'files'
URL_PATH = f'{BASE_PATH}/{FILE_PATH}'

def create_files_directory():
    try:
        files_path = os.path.join(BASE_PATH, FILE_PATH)
        os.mkdir(files_path)
        print(f'{files_path} Created!!!')
    except Exception as ex:
        print(f'Not able to create /files directory -> {ex}')

try:
    if os.path.exists('files') is False:
        print('Creating FILES path..')
        create_files_directory()
    else:
        print('/files direcotory is already there.')
    
except Exception as ex:
    print(f'Not able to create /files directory -> {ex}')
    pass