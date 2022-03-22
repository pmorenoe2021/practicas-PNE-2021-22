#module
def seq_ping():
    print("ok")

def valid_filename():
    exit = False
    while not exit:
        filename = input("NAME OF THE FILE : ")
        try:
            f = open("./session4/" + filename + ".txt", "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("file does not exist")

def seq_read_fasta(filename): #3
    seq = open("./session4/" + filename + ".txt", "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

def seq_count_base(seq):#4
    seq = open("./session4/" + seq + ".txt", "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
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
    return let_a, let_c, let_g, let_t

def seq_count(seq): #5
    seq = open("./session4/" + seq + ".txt", "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for l in seq:
        if l.upper() == "A":
            d['A'] += 1
        elif l.upper() == "T":
            d['T'] += 1
        elif l.upper() == "C":
            d['C'] += 1
        elif l.upper() == "G":
            d['G'] += 1
    return d

def seq_reverse(seq): #6
    n = 20
    seq = open("./session4/" + seq + ".txt", "r").read()
    seq = seq[seq.find("\n") + 1:].replace("\n", "")
    frag = seq[:n + 1]
    rev = frag[::-1]
    return frag, rev


def seq_complement(seq): #7
    n = 20
    comp = []
    seq = open("./session4/" + seq + ".txt", "r").read()
    seq = seq[seq.find("\n") + 1:].replace("\n", "")
    frag = seq[:n + 1]
    for b in frag:
        if b == "A":
            comp.append("T")
        elif b == "T":
            comp.append("A")
        elif b == "C":
            comp.append("G")
        elif b == "G":
            comp.append("C")

    return frag, comp

def base_count(s):#8
    s = open("./session4/" + s + ".txt", "r").read()
    s = s[s.find("\n") + 1:].replace("\n", "")
    let_a = 0
    let_c = 0
    let_g = 0
    let_t = 0
    for l in s:
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

    #def read_fasta(self, filename):
     #   f = open("./Genes/" + filename + ".txt", "r").read()
      #  self.strbases = seq = f[f.find("\n"):].replace("\n", "")
        #this is a method not function so it is not neccessary to return something
        # bc we are modifiying attributes of the class



