from ast import For
import os
from pathlib import Path,  PurePath
import argparse
import this





directory = Path(Path.cwd())
files_dir = Path.cwd() / "the_new_directory"
files_dir_temp = Path.cwd() / "the_new_directory_temp"

print(directory.absolute())
# exit()

the_new_dir = Path.mkdir(files_dir, exist_ok=True)
the_themp_dir = Path.mkdir(files_dir_temp, exist_ok=True)

for dir_file in directory.iterdir():
    if not dir_file.name.find("the_new_directory"):
        dir_file.rename(f"${files_dir_temp.absolute}/${dir_file.absolute}")

file_list = directory.glob('**/**')

for file in file_list:
    print(file.absolute())
    