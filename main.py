

from os import getcwd, mkdir
from pathlib import Path
import shutil

sysdirname="thenewdir"
systempdirname=sysdirname+"temp"




working_dir = Path(Path.cwd())

sysdir = Path(Path.joinpath(Path.cwd(), sysdirname))
# sysdir.mkdir(exist_ok=True)

sysdirtemp= Path(Path.joinpath(Path.cwd(), systempdirname))
# sysdirtemp.mkdir(exist_ok=True)

print(working_dir.is_dir())
itr_working_dir = working_dir.iterdir()
for item in itr_working_dir:
    print(item.name)
    is_system_folder = 'the_new_dir' in item.name
    print(str(is_system_folder))
    if not is_system_folder:
        # print(new_name.name)
        shutil.move(item, sysdirtemp)


def iterdir(dir_path: Path):
    for item in dir_path.iterdir():
        print(item.as_uri)
        if item.is_file():
            if item.suffix:
                print(item.suffix[1:])
            else:
                print(f"${item.name} has no suffix")
        if item.is_dir():
            print(f"${item.name} is a directory")
            iterdir(item)

iterdir(sysdirtemp)