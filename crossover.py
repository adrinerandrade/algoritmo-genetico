from random import randint
from chromosome import Chromosome

class Crossover:

    def __init__(self, parent_1, parent_2):
        self.parent_1 = Chromosome(parent_1.get_cities()[:])
        self.parent_2 = Chromosome(parent_2.get_cities()[:])

    # Cria um gene filho
    def generate_children(self):
        genes_1 = self.parent_1.get_cities()
        genes_2 = self.parent_2.get_cities()
        selected_gene = randint(0, len(genes_1) - 1)
        self.exchange_gene(selected_gene, genes_1, genes_2)
        exchanged_genes = []
        exchanged_genes.append(selected_gene)
        while True:
            duplicated_gene = self.get_duplicated_gene(genes_1, exchanged_genes)
            if (duplicated_gene == -1):
                break
            self.exchange_gene(duplicated_gene, genes_1, genes_2)
            exchanged_genes.append(duplicated_gene)

        return (Chromosome(genes_1), Chromosome(genes_2))

    def exchange_gene(self, gene, genes_1, genes_2):
        tmp = genes_1[gene]
        genes_1[gene] = genes_2[gene]
        genes_2[gene] = tmp

    # Dulica o gene
    def get_duplicated_gene(self, genes, exchanged_genes):
        for gene in range(len(genes)):
            if gene in exchanged_genes:
                continue
                
            if len([g for g in genes if g == genes[gene]]) > 1:
                return gene

        return -1
