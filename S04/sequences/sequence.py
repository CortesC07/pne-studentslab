from pathlib import Path


FILENAME = "sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()
file_contents = file_contents.split("\n")
body = "".join(file_contents[1: ])
print(body)
print("total number of bases: ", len(body))