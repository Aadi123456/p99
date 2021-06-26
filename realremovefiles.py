import os
import shutil
import time
# replace the path with your desired path.
path = '/Users/Aadi/Downloads/newFolder'

def remove_files(dir_path, n):
    all_files = os.listdir(dir_path)
    now = time.time()
    n_days = n 
    
    for files in all_files:
        file_path = os.path.join(dir_path, files)

        if not os.path.isfile(file_path):
            continue

        if os.stat(file_path).st_mtime < now - n_days:
            os.remove(file_path)
            print("Deleted ", files)

remove_files(path, 0)
