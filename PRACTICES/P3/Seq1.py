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

    def __init__(self, strbases="NULL"):
        if strbases == "NULL":
            self.strbases = strbases
            print("NULL se created")

        elif Seq.valid_bases(strbases):
            self.strbases = strbases
            print("New sequence created")
        else:
            self.strbases = "ERROR"
            print("Invalid sequence detected")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "ERROR" or self.strbases == "NULL":
            return 0
        return self.strbases.count(base)

    def seq_count(self):
        result = {}
        if self.strbases == "NULL" or self.strbases == "ERROR":
            for base in Seq.BASES_ALLOWED:
                result[base] = 0
        else:
            for base in Seq.BASES_ALLOWED:
                result[base] = self.strbases.count(base)

        return result

    def seq_reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        return self.strbases[::-1]

    def seq_complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases


    def read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        body = lines[1:]
        self.strbases = ""
        for line in body:
            self.strbases += line


    def info(self):
        result = f"Sequence: {self.strbases}\n"
        result += f"Total length :{self.len()}\n"
        for base, count in self.seq_count().items():
            result += f"{base}:{count}({((count * 100) / self.len()):.1f}% )"
        return result