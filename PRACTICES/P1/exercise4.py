from Seq1 import Seq
# -- Creating a Null sequence
s1 =["", "ACTGA", "Invalid sequence"]
sequences = []

for st in s_l:
    if st == "":
        sequences.append(Seq())
    else:
        sequences.append(Seq(st))

for i in range(0, len(sequences)):
    print(f"Sequence {str(i + 1)}:(Length = {st.len()}) {sequences[i]}")