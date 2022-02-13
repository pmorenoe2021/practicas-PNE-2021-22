import Seq0
l = ["U5", "ADA", "FRAT1", "RNU6_269P", "FXN"]
for s in l :
    let_a, let_c, let_g, let_t = Seq0.seq_count_base(s)
    print("Gene",s,": ", "\nA:", let_a, "\nC:", let_c, "\nT:", let_t, "\nG:", let_g)


