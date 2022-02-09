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

def seq_read_fasta(filename):
    seq = open("./session4/" + filename + ".txt", "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq

def seq_count_base(seq, base):




