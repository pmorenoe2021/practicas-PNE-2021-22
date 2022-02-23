from Seq1 import Seq
# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
FILENAME = s.valid_filename()
s.read_fasta(FILENAME)
print(f"Sequence:(Length = {s.len()})",s,"\nBases :",s.seq_count(),"\nRev: ",s.seq_reverse(),"\nComp: ",s.seq_complement())