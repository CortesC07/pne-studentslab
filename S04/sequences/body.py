from pathlib import path


FILENAME = "sequences/U5.txt"
file_contents = Path(FILENAME).read_text()
file_contents = file_contents.split("\n")
body = "".join(file_contents[1: ])