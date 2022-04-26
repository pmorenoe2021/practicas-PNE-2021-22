from Seq1 import Seq
print("-----| Practice 1, Exercise 10 |------")

GENES = ["U5", "ADA", "FRAT1"]
for seq in GENES:
    filename = seq + ".txt"
    s = Seq()
    s.read_fasta(filename)
    bases = s.seq_count()
    most_freq = None
    for key, value in bases.items():
        if most_freq:
            if value > most_freq[1]:
                most_freq = (key, value)
        else:
            most_freq = (key, value)
    print(f"Gene {seq}: Most frequent Base: {most_freq}")
