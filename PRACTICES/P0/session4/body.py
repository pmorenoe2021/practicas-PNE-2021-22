from pathlib import Path

filename = input("FILE NAME: ")
try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    print(f"Body of the file '{filename}' file")
    for line in body:
        print(line)

except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")
except IndexError:
    print(f"[ERROR]: file '{filename}' is empty")