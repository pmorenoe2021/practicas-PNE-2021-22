from pathlib import Path

# -- Constant with the new of the file to open
filename = input("FILE NAME: ")
try:
    # -- Open and read the file
    file_contents = Path(filename).read_text()
    # -- Print the contents on the console
    print(file_contents)
except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")


