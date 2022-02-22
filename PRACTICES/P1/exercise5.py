from PRACTICES.P0.Seq0 import seq_count_base
from Seq1 import Seq
# -- Creating a Null sequence
s_l =["", "ACTGA", "Invalid sequence"]
sequences = []

for st in s_l:
    let_a, let_c, let_g, let_t = count_base(st)
    if st == "":
        sequences.append(Seq())
    else:
        sequences.append(Seq(st))

for i in range(0, len(sequences)):
    print("Sequence", str(i + 1) + ":", sequences[i])
    print("A:",let_a,"C:", let_c ,"T:", let_t,"G:", let_g,)