def to_rna(dna):
    rna = ''
    #if not set('GCTAU').issuperset(dna)
    if set('GCTA').issuperset(dna):
        for n in dna:
            rna += replace_nucleotide(n)
        return rna
    else:
        raise ValueError('cant even')

def replace_nucleotide(n):
  return {'G': 'C','C': 'G','T': 'A','A': 'U'}.get(n, 'x')
