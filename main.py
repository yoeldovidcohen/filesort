from ast import For
import os

directory = os.getcwd()

new_folder_name = 'the_sorted_files'

if not os.path.exists(new_folder_name):
    os.makedirs(new_folder_name)



def move_file(filepath: os.DirEntry[str]):
    
    return

def get_file_name_from_path(filepath):
    return filepath.path[filepath.path.rfind('/')+1:-1]


# size = 0


def all_files_list(directory):
    global size

    for filename in os.scandir(directory):
        
        if filename.is_file():
            # size += os.path.getsize(filename)
            print(filename.path)
            last_file_name = get_file_name_from_path(filename) 
            print(last_file_name)
            # print(filename.path[filename.path.rfind('.)')+1:-1])
            # print(filename.path[last_file_name:-1])
        elif filename.is_dir():
            print(filename.path)
            all_files_list(filename.path)


all_files_list(directory)
# print(size)