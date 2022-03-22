import P0
print("-----| Exercise 1 |------")
f = P0.seq_ping()
print(f)
print( )



print("-----| Exercise 2 |------")
FOLDER = "./Genes/"
filename = input("File´s name: ")
print(f"DNA file: {filename}")
sequence = P0.seq_read_fasta(FOLDER + filename)
print(f"The first 20 bases are: {sequence[:20]}")
print()



print("-----| Exercise 3 |------")
FOLDER = "./Genes/"
l = ["U5", "ADA", "FXN", "FRAT1"]

for seq in l:
    filename = seq + ".txt"
    sequence = P0.seq_read_fasta(FOLDER + filename)
    print(f"Gene {seq} ---> Length: {P0.seq_len(sequence)}")
print( )


print("-----| Exercise 4 |------")
FOLDER = "./Genes/"
l = ["U5", "ADA", "FXN", "FRAT1"]
bases = ["A", "C", "T", "G"]

for seq in l:
    filename = seq + ".txt"
    sequence = P0.seq_read_fasta(FOLDER + filename)
    print(f"Gene {seq}")
    for base in bases:
        print(f"{base} : {P0.seq_count_base(sequence, base)}")


print()


print("-----| Exercise 5 |------")
FOLDER = "./Genes/"
l = ["U5", "ADA", "FXN", "FRAT1"]
for seq in l:
    filename = seq + ".txt"
    sequence = P0.seq_read_fasta(FOLDER + filename)
    print(f"Gene {seq}: {P0.seq_count(sequence)}")
print()



print("-----| Exercise 6 |------")
seq = "U5"
FOLDER = "./Genes/"
filename = seq + ".txt"
sequence = P0.seq_read_fasta(FOLDER + filename)

frag, rev = P0.seq_reverse(sequence)
print(f"Frag: {frag}\nRev: {rev}")
print()



print("-----| Exercise 7 |------")
gene = "U5"
FOLDER = "./Genes/"
filename = gene + ".txt"

sequence = P0.seq_read_fasta(FOLDER + filename)
print(f"Gene: {gene}")
frag = sequence[:20]
print(f"Frag: {frag}\nComp: {P0.seq_complement(frag)}")
print()



print("-----| Exercise 8 |------")
FOLDER = "./Genes/"
genes = ["U5", "ADA", "FXN", "FRAT1"]

for seq in genes:
    filename = seq + ".txt"
    sequence = P0.seq_read_fasta(FOLDER + filename)
    print(f"Gene {seq}: Most frequent Base: {P0.most_f_b(sequence)}")


