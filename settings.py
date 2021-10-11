import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = 'files'
URL_PATH = f'{BASE_PATH}/{FILE_PATH}'

def create_files_path():
    files_path = os.path.join(BASE_PATH, FILE_PATH)
    os.mkdir(files_path)
