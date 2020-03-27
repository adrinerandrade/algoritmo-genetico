from generator import Generator
from distance import DistanceResolver
from roulette import Roulette
from chromosome import Chromosome
from random import randint
from crossover import Crossover
from mutation import Mutation

class Population:
    def __init__(self, cities):
        self.population_size = 20
        self.population = []
        self.distance_resolver = DistanceResolver(cities)
        gen = Generator()
        for _ in range(self.population_size):
            self.population.append(gen.generate_random_chromosome())
    
    def get_population(self): 
        return self.select_best_parents(20)

    # Cria a proxima geração
    def next_generation(self):
        parents = self.select_best_parents(10)
        newPop = []
        newPop.extend(map(lambda tup: tup[0], parents))
        newPop.extend(self.createChildren(parents))
        self.population = newPop

    # Seleciona a melhor metade da população
    def select_best_parents(self, limit):
        distances = []
        for i in range(len(self.population)):
            chromosome = self.population[i]
            distance = self.distance_resolver.calculate_distance(chromosome)
            distances.append((chromosome, distance))
        distances.sort(key=lambda tup: tup[1])
        return distances[0:limit]

    # Crias os filhos com base na roleta
    def createChildren(self, parents):
        roulette = Roulette(parents)
        children = []
        for _ in range(5):
            parent_1 = roulette.select_parent()
            parent_2 = roulette.select_parent()
            new_children = Crossover(parent_1, parent_2).generate_children()
            Mutation(new_children[0]).mutate()
            Mutation(new_children[1]).mutate()
            children.append(new_children[0])
            children.append(new_children[1])
            
        return children
