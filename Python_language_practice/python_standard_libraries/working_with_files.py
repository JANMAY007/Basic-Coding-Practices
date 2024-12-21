from pathlib import Path
import shutil

source = Path("D:/My data/Python_language_practice/install.py")
target = Path("D:/My data/Python_language_practice/code jam solutions/install.py")

shutil.copy(source, target)

path = Path("D:/My data/Python_language_practice/install.py")
data = input()
path.read_text()
path.write_text(data)
# this methods are more efficient for the file handling
with path as file:
    ...
