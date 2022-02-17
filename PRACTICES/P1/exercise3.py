from Seq1 import Seq
# -- Creating a Null sequence
s_l =["", "ACTGA", "Invalid sequence"]
sequences = []

for st in s_l:
    if st == "":
        sequences.append(Seq())
    else:
        sequences.append(Seq(st))

for i in range(0, len(sequences)):
    print("Sequence", str(i + 1) + ":", sequences[i])