import Seq0
l = ["U5", "ADA", "FRAT1", "RNU6_269P", "FXN.txt"]
for s in l:
    bases = Seq0.base_count(s)
    biggest = bases["A"]
    for key, value in bases.items():
        if value > biggest:
            biggest = value
            x = key
    print("Gene", s, ": Most frequent Base:", x)
# solo estas calculando fxn!