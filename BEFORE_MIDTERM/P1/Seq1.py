class Seq:
    BASES_ALLOWED = ["A", "C", "T", "G"]
    BASES_COMPLEMENTS = {"A": "T", "C": "G", "G": "C", "T": "A"}

    @staticmethod
    def valid_bases(bases):
        valid = True
        i = 0
        while i < len(bases) and valid:
            if bases[i] in Seq.BASES_ALLOWED:
                i += 1
            else:
                valid = False
        return valid

    def __init__(self, bases="NULL"):
        if bases == "NULL":
            self.bases = bases
            print("NULL se created")

        elif Seq.valid_bases(bases):
            self.bases = bases
            print("New sequence created")
        else:
            self.bases = "ERROR"
            print("Invalid sequence detected")

    def __str__(self):
        return self.bases

    def len(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return len(self.bases)

    def count_base(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return self.bases.count(base)

    def seq_count(self):
        result = {}
        if self.bases == "NULL" or self.bases == "ERROR":
            for base in Seq.BASES_ALLOWED:
                result[base] = 0
        else:
            for base in Seq.BASES_ALLOWED:
                result[base] = self.bases.count(base)

        return result

    def seq_reverse(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        return self.bases[::-1]

    def seq_complement(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases

        result = ""
        for base in self.bases:
            result += Seq.BASES_COMPLEMENTS[base]
        return result


    def read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.bases = ""
        for line in body:
            self.bases += line
        return