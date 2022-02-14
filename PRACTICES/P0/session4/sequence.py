from pathlib import Path

filename = input("FILE NAME: ")

try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    total = 0
    body = lines[1:]
    for line in body:
        total += len(line)
    print(f"TOTAL Nº OF BASES: {total}")

except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")
except IndexError:
    print(f"[ERROR]: file '{filename}' is empty")