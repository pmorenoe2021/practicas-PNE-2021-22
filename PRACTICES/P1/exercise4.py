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
    if sequences[i] == "NULL" or sequences[i] == "ERROR": # NO TE FUNCIONA ETSA PARTE
        length_st = 0
    else:
        st = str(sequences[i])
        length_st =  len(st)
    print("Sequence", str(i + 1) + ": Length =",length_st, sequences[i])