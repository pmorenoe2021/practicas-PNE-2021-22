from pathlib import Path

filename = input("FILE NAME: ")
try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    head = lines[0]
    print(f"Head of the file '{filename}' file: \n{head}")

except FileNotFoundError:
    print(f"[ERROR]: file '{filename}' not found")
except IndexError:
    print(f"[ERROR]: file '{filename}' is empty")
    #en realidad no es un error es solo que el fichero esta vacio