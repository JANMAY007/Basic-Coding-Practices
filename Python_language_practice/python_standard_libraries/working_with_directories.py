from pathlib import Path

path = Path("D:/My data/Python_language_practice")
for p in path.iterdir():
    print(p)

# py_files = [p for p in path.glob("**/*.py")]
# py_files = [p for p in path.glob("*.py")]
py_files = [p for p in path.rglob("*.py")]
for file in py_files:
    print(file)
