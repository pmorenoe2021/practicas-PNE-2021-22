def seq_ping():
    print("Testing the seq_ping() funcion")
    return "OK"


def seq_len(seq):
    return len(seq)


def seq_read_fasta(filename):  # 3
    from pathlib import Path
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    sequence = ""
    for line in body:
        sequence += line
    return sequence




def seq_count_base(seq, base):
    base = ["A", "C", "T", "G"]
    ca = 0
    cc = 0
    ct = 0
    cg = 0
    for e in seq:
        if e == "A":
            ca += 1
        elif e == "C":
            cc += 1
        elif e == "T":
            ct += 1
        elif e == "G":
            cg += 1

    return ca, cc, ct, cg


def seq_count_base(seq, base):
    return seq.count(base)
    # OTRA MANERA MAS ESPARTANA
    # total = 0
    # for b in seq:
    #    if b == base:
    #        total += 1
    # return total


def seq_count(seq):
    d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for e in seq:
        if e == "A":
            d["A"] += 1
        elif e == "T":
            d["T"] += 1
        elif e == "C":
            d["C"] += 1
        elif e == "G":
            d["G"] += 1
    return d


def seq_reverse(seq):
    frag = seq[:20]
    rev = frag[::-1]
    return frag, rev


def seq_complement(seq):
    COMPLEMENTS = {"A": "T", "C": "G", "T": "A", "G": "C"}
    result = ""
    for base in seq:
        result += COMPLEMENTS[base]
    return result


def most_f_b(seq):
    d = seq_count(seq)
    max_k = None
    max_v = 0
    for k, v in d.items(): # podrias haber puesto seq_count(seq).items(
        if v >= max_v:
            max_v = v
            max_k = k
    return max_k
