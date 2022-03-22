class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):
        self.strbases = strbases

        if self.strbases == "NULL":
            print("NULL Seq Created")

        else:
            if self.strbases == "Invalid sequence":
                print("INVALID Seq!")
                self.strbases = "ERROR"
            else:
                print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            result = 0
        else:
            result = len(self.strbases)
        return result

    def count_bases(self):  # 5
        ca = 0
        ct = 0
        cc = 0
        cg = 0
        for e in self.strbases:
            if e == "A":
                ca += 1
            elif e == "T":
                ct += 1
            elif e == "C":
                cc += 1
            elif e == "G":
                cg += 1

        return f"A:{ca}, T:{ct}, C:{cc}, G:{cg}, "

    def count(self):  # 6
        bases = {"A": 0, "C": 0, "T": 0, "G": 0}
        for e in self.strbases:
            if e in bases:
                bases[e] += 1
        return bases

    def reverse(self):
        rev = self.strbases[::-1]
        if self.strbases == "NULL":
            rev = "NULL"
        elif self.strbases == "ERROR":
            rev = "ERROR"
        return rev

    def complement(self):  # 8
        comp = ""
        if self.strbases == "NULL":
            comp = "NULL"
        elif self.strbases == "ERROR":
            comp = "ERROR"
        for e in self.strbases:
            if e == "A":
                comp += "T"
            elif e == "T":
                comp += "A"
            elif e == "C":
                comp += "G"
            elif e == "G":
                comp += "C"
        return comp

    def valid_filename(self):
        exit = False
        while not exit:
            filename = input("NAME OF THE FILE : ")
            try:
                f = open("./sequences/" + filename + ".txt", "r")
                exit = True
                return filename
            except FileNotFoundError:
                print("file does not exist")

    def read_fasta(self, filename):
        f = open("./sequences/" + filename + ".txt", "r").read()
        self.strbases = seq = f[f.find("\n"):].replace("\n", "")

    def most_freq_base(self, seq):
        f = open("./sequences/" + seq + ".txt", "r").read()
        self.strbases = seq = f[f.find("\n"):].replace("\n", "")
        max_k = None
        max_v = 0
        d = self.count()
        for k, v in d.items():
            if v >= max_v:
                max_k = k
                max_v = v
        return max_k
