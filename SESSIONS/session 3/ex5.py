#Create a program for counting the number of bases presented in a DNA sequence.
# The user introduces a sequence of letter representing the DNA chain.
# For example: CATGTAGACTAG.
# Our program should calculate the total length, and the number of bases that compound the sequence.
# In the previous example sequence, the output of our program should be like this:

def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1 # because we assume the sequence is correct at all times so we dont need an if b equal a ...
    return d

dna = input("Introduce the seq: ")
print("total length:", len(dna))
for k, v in count_bases(dna).items():
    print(k + ":", v)
#we put the + between k and : because in the output there isnt a space.
# so since they are both strings we can concatenate them without doing str(k), but since v is an int we need a comma