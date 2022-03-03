from ast import For
import os

directory = os.getcwd()

# def file_list(directory):
#     for filename in os.scandir(directory):
#         if filename.is_file():
#             print(filename.path)
        


# def folder_list(directory):
#     for filename in os.scandir(directory):
#         if filename.is_dir():
#             print(filename.path)

# file_list(directory)
# folder_list(directory)

size = 0


def all_files_list(directory):
    global size

    for filename in os.scandir(directory):
        
        if filename.is_file():
            size += os.path.getsize(filename)
            print(filename.path)
        elif filename.is_dir():
            print(filename.path)
            all_files_list(filename.path)


all_files_list(directory)
print(size)