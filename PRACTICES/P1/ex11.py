from Seq1 import Seq

s_l =["ACCTGC", "Hello? Am I a valid sequence?"]
sequences = []

for st in s_l:
    if Seq.valid_seq2(st):
        sequences.append(Seq(st))
    else:
        sequences.append(Seq("ERROR"))

for i in range(0, len(sequences)):
    print("sequence", str(i) + ":", sequences[i])
