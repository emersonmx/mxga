from random import randint as rand

def random(chromosome):
'''Applying random mutation in a gene.
Parameters:
    chromosome: a gene list [g1, g2, g3, ..., gn]
'''
    gene_size = len(chromosome) - 1
    source = rand(0, gene_size)
    destination = rand(0, gene_size)

    chromosome[source], chromosome[destination] = (chromosome[destination],
                                                   chromosome[source])

    return chromosome
