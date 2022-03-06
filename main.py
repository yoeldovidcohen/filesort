

import secrets
import shutil
from os import getcwd, mkdir
from pathlib import Path

sysdirname="thenewdir"
systempdirname=sysdirname+"temp"

# shutil.


working_dir = Path(Path.cwd())

sysdir = Path(Path.joinpath(Path.cwd(), sysdirname))
sysdir.mkdir(exist_ok=True)

sysdirtemp= Path(Path.joinpath(Path.cwd(), systempdirname))
sysdirtemp.mkdir(exist_ok=True)

print(working_dir.is_dir())
itr_working_dir = working_dir.iterdir()
for item in itr_working_dir:
    print(item.name)
    is_system_folder = sysdirname in item.name
    print(str(is_system_folder))
    if not is_system_folder:
        # print(new_name.name)
        shutil.move(item, sysdirtemp)

size = 0


def iterdir(dir_path: Path):
    global size
    for item in dir_path.iterdir():
        print(item.as_uri)
        if item.is_file():
            size += item.stat().st_size
            if item.suffix:
                suffix = item.suffix[1:]

                suffix_folder = Path.joinpath(sysdir, suffix)
                suffix_folder.mkdir(exist_ok=True)
                new_path=Path.joinpath(suffix_folder, item.name)
                if new_path.exists():
                    last_dot_pos=item.name.rfind('.')
                    new_random_name = f"{item.name[:last_dot_pos]}_{secrets.token_hex(4)}{item.name[last_dot_pos:]}"
                    new_path = Path.joinpath(suffix_folder, new_random_name)
                    print("file exists")
                    print(new_path)
                    a = input('hi\n')

                    # exit()
                print(new_path.as_uri)
                shutil.move(item, new_path, )
                print(suffix)
            else:
                print(f"${item.name} has no suffix")
        if item.is_dir():
            print(f"${item.name} is a directory")
            iterdir(item)

iterdir(sysdirtemp)

print(str(size))
