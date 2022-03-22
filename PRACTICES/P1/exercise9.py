from Seq1 import Seq
# -- Create a Null sequence
s = Seq()
FILENAME = "FRAT1.txt"
s.read_fasta(FILENAME)
print(f"Sequence:(Length = {s.len()})",s,"\nBases :",s.seq_count(),"\nRev: ",s.seq_reverse(),"\nComp: ",s.seq_complement())