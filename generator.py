from random import randint
from chromosome import Chromosome

class Generator:
    # Gera os chromossomos
    def generate_random_chromosome(self):
        cities = []
        for i in range(20):
            cities.append(i)

        genes = []
        while len(cities) > 0:
            city = randint(0, len(cities) - 1)
            genes.append(cities.pop(city))
        
        return Chromosome(genes)

        