def split(parental_chromosomes, pivot):
    """Create a new chromosome using 2 parental_chromosomes,
    don't bothering the gene order.

    Args:
        parental_chromosomes: two gene list [[g1, g2, g3, ..., gn],
            [g1, g2, g3, ..., gn]]
    """
    p1, p2 = parental_chromosomes

    gene_number = len(p1)
    return p1[:pivot] + p2[pivot:gene_number]

def cycle(parental_chromosomes):
    """Create a new chromosome using 2 parentes, keeping gene unicity.

    Args
        parental_chromosomes: two gene list [[g1, g2, g3, ..., gn],
            [g1, g2, g3, ..., gn]]
    """
    p1, p2 = parental_chromosomes
    gene_number = len(p1)
    chromosome = [None for gene in range(gene_number)]

    i = 0
    ciclic = False
    while not ciclic:
        chromosome[i] = p1[i]
        gene = p2[i]
        i = p1.index(gene)

        if p1[i] in chromosome:
            ciclic = True

    for i in range(gene_number):
        if not chromosome[i]:
            chromosome[i] = p2[i]

    return chromosome
