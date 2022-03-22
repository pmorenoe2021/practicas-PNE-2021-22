FILENAME = input("ENTER THE NAME OF A FILE: ")
s.read_fasta(FILENAME)


def seq_read_fasta(self, filename):  # 3
    from pathlib import Path
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    sequence = ""
    for line in body:
        sequence += line
    return sequence

    FOLDER = "./Genes/"
    filename = input("Enter the name of the file: ")
    s = Seq()
    sequence = Seq.seq_read_fasta(FOLDER + filename)