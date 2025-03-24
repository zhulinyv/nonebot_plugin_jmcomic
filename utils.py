import os
import shutil

if not os.path.exists(path := "./data"):
    os.mkdir("./data")

if not os.path.exists(path := "./data/jm"):
    os.mkdir(path)

if not os.path.exists(path := "./data/jm/option.yml"):
    shutil.copyfile(f"{os.path.dirname(os.path.abspath(__file__))}/option.yml", path)
