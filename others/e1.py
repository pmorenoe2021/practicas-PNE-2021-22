from P1 import Seq #tmb puede poner * y no tienes que poner los seqs delante
print("-----| Exercise 1 |------")
seq1 = Seq("ACTGA")
print(f"Sequence 1: (Length: {seq1.len()}) {seq1}")
print( )


print("-----| Exercise 2 |------")
s = Seq() #null
s2 = Seq("ACTGA") #valid
print(f"Sequence 1: {s}\nSequence 2: {s2}")
print( )


print("-----| Exercise 3 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
print(f"Sequence 1: {s}\nSequence 2: {s2}\nSequence 3: {s3}")
print( )


print("-----| Exercise 4 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
print(f"Sequence 1:(Length: {s1.len()}) {s1}\nSequence 2:(Length: {s2.len()}) {s2}\nSequence 3:(Length: {s3.len()}) {s3}")
print( )

print("-----| Exercise 5 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
print(f"Sequence 1:(Length: {s1.len()}) {s1} \n{s1.count_bases()}")
print(f"Sequence 2:(Length: {s2.len()}) {s2} \n{s2.count_bases()}")
print(f"Sequence 3:(Length: {s3.len()}) {s3} \n{s3.count_bases()}")
print( )



print("-----| Exercise 6 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
print(f"Sequence 1:(Length: {s1.len()}) {s1} \nBases: {s1.count()}")
print(f"Sequence 2:(Length: {s2.len()}) {s2} \nBases: {s2.count()}")
print(f"Sequence 3:(Length: {s3.len()}) {s3} \nBases: {s3.count()}")
print( )



print("-----| Exercise 7 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
print(f"Sequence 1:(Length: {s1.len()}) {s1} \nBases: {s1.count()}\nRev: {s1.reverse()}")
print(f"Sequence 2:(Length: {s2.len()}) {s2} \nBases: {s2.count()}\nRev: {s2.reverse()}")
print(f"Sequence 3:(Length: {s3.len()}) {s3} \nBases: {s3.count()}\nRev: {s3.reverse()}")
print( )



print("-----| Exercise 8 |------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
print(f"Sequence 1:(Length: {s1.len()}) {s1} \nBases: {s1.count()}\nRev: {s1.reverse()}\nComp: {s1.complement()}")
print(f"Sequence 2:(Length: {s2.len()}) {s2} \nBases: {s2.count()}\nRev: {s2.reverse()}\nComp: {s2.complement()}")
print(f"Sequence 3:(Length: {s3.len()}) {s3} \nBases: {s3.count()}\nRev: {s3.reverse()}\nComp: {s3.complement()}")
print( )



print("-----| Exercise 9 |------")
s = Seq()
FILENAME = input("ENTER THE NAME OF A FILE: ")
s.read_fasta(FILENAME)
print(f"Sequence 1:(Length: {s.len()}) {s} \nBases: {s.count()}\nRev: {s.reverse()}\nComp: {s.complement()}")
print( )










