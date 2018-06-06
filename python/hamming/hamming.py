def distance(strand_a, strand_b):
    a = list(strand_a)
    b = list(strand_b)
    c = 0
    d = 0
    
    if len(a) == len(b):
        for x in a:
            if a[c] != b[c]:
                d += 1
            c += 1
        return d
    else:
        raise ValueError("Nope")
    pass
