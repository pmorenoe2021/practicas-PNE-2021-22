class Seq:
    """A class for representing Genes"""

    def __init__(self, strbases ="NULL"):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if self.strbases == "NULL":
            print("NULL se created")

        elif not self.valid_seq():
            self.strbases = "ERROR"
            print("INVALID Seq!")

        else:
            print("New sequence created!")


    @staticmethod
    def valid_seq2(sequence):
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "T" and c != "G":
                valid = False
            i += 1
        return valid

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == "ERROR" or self.strbases == "NULL":
            result = 0
        else:
            result = len(self.strbases)
        return result

    def count_base(self, list_bases):
        count = 0
        if self.strbases == "ERROR" or self.strbases == "NULL":
            count = 0
        else:
            for s in self.strbases:
                if s == list_bases:
                    count += 1
        return count

    def seq_count(self):
        d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for l in self.strbases:
            if l.upper() == "A":
                d['A'] += 1
            elif l.upper() == "T":
                d['T'] += 1
            elif l.upper() == "C":
                d['C'] += 1
            elif l.upper() == "G":
                d['G'] += 1
        return d

    def seq_reverse(self):
        frag = self.strbases
        rev = frag[::-1]
        if frag == "ERROR" or frag == "NULL":
            rev = frag
        return rev

    def seq_complement(self):
        comp = ""
        frag = self.strbases
        for b in frag:
            if b == "A":
                comp += "T"
            elif b == "T":
                comp += "A"
            elif b == "C":
                comp += "G"
            elif b == "G":
                comp +="C"
        if frag == "ERROR" or frag == "NULL":
            comp = frag

        return comp

    def valid_filename(self):
        exit = False
        while not exit:
            filename = input("NAME OF THE FILE : ")
            try:
                f = open("./Genes/" + filename + ".txt", "r")
                exit = True
                return filename
            except FileNotFoundError:
                print("file does not exist")

    def read_fasta(self, filename):
        f = open("./Genes/" + filename + ".txt", "r").read()
        self.strbases = seq = f[f.find("\n"):].replace("\n", "")



    def base_count(self, seq):  # TERMINAR
        seq = open("./Genes/" + seq + ".txt", "r").read()
        seq = seq[seq.find("\n") + 1:].replace("\n", "")
        let_a = 0
        let_c = 0
        let_g = 0
        let_t = 0
        for l in seq:
            if l.upper() == "A":
                let_a += 1
            elif l.upper() == "C":
                let_c += 1
            elif l.upper() == "G":
                let_g += 1
            elif l.upper() == "T":
                let_t += 1
        bases = {"A": let_a, "C": let_c, "G": let_g, "T": let_t}
        return bases

#    def read_fasta(self, filename):
       # from pathlib import Path
        #file_contents = Path(filename).read_text()
        #lines = file_contents.splitlines()
       # body = lines[1:]
        #self.strbases = ""
       # for line in body:
        #    self.strbases += 1