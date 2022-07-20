import os
import shutil

def delete_empty_folders(folder_location):
    all_directories = list(os.walk(folder_location))
    for path, a, b in all_directories:
        if len(os.listdir(path)) == 0:
            shutil.rmtree(path)
if __name__ == '__main__':
    delete_empty_folders("/home/joelouisbdonin/Documents/notempty")