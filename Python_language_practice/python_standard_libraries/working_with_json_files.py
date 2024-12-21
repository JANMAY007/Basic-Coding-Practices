from pathlib import Path
import json
# writing in the file
"""movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "kindergarten cop", "year": 1993}
]

data = json.dumps(movies)
# print(data)
Path("movies.json").write_text(data)"""

# reading from the file

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
