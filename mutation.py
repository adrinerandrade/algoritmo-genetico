from random import randint

class Mutation:
    def __init__(self, chromosome):
        self.chromosome = chromosome

    # Cria a mutação
    def mutate(self):
        # 5% de chance de ocorrer uma mutação
        do_mutation = randint(1, 100) <= 5
        if (do_mutation):
            genes = self.chromosome.get_cities()
            gene_1 = randint(0, len(genes) - 1)
            gene_2 = randint(0, len(genes) - 1)
            tmp = genes[gene_1]
            genes[gene_1] = genes[gene_2]
            genes[gene_2] = tmp