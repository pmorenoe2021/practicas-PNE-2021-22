from Seq1 import Seq
print("-----| Practice 1, Exercise 10 |------")
# -- Create a Null sequence
l = ["U5", "ADA", "FRAT1", "RNU6_269P", "FXN"]
for seq in l:
    s = Seq()
    bases = s.base_count(seq)
    biggest = bases["A"]
    for key, value in bases.items():
        if value > biggest:
            biggest = value
            x = key
    print("Gene", s, ": Most frequent Base:", x)
