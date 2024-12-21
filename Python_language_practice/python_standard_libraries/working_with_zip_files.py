from pathlib import Path
from zipfile import ZipFile

with ZipFile("python.zip", "w") as zipfile:
    for path in Path("D:/My data/Python_language_practice/python_django_framework").rglob("*.*"):
        zipfile.write(path)

with ZipFile("python.zip") as zipfile:
    for name in zipfile.namelist():
        print(name)
