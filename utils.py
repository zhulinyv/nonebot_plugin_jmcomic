import os
import shutil

for folder in ["./data", "./data/jm"]:
    if not os.path.exists(folder):
        os.mkdir(folder)

if not os.path.exists(path := "./data/jm/option.yml"):
    shutil.copyfile(f"{os.path.dirname(os.path.abspath(__file__))}/option.yml", path)
