from P1 import *
print("-----| Exercise 10 |------")
FOLDER = "./sequences/"
l = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
for seq in l:
    filename = seq +".txt"
    sequence = read_fasta(FOLDER + filename)
    s = Seq()
    print(f"Gene {seq}: Most frequent Base: {seq.most_freq_base()}")
