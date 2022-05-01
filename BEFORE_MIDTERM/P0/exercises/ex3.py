import Seq0
l = ["U5", "ADA", "FRAT1", "RNU6_269P", "FXN.txt"]
for s in l:
    print("Gene:",s,  "Length:",len(Seq0.seq_read_fasta(s)))
