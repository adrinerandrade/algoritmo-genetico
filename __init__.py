from cities import Cities
from population import Population
from distance import DistanceResolver
import matplotlib.pyplot as plt
import matplotlib

cities_location = Cities()
population = Population(cities_location)

for _ in range(10000):
    population.next_generation()    

# resultado final
final_population = population.get_population()
best_solution = final_population[0]
best_chromosome = best_solution[0]
best_distance = best_solution[1]

print("Tamanho da população: {}".format(len(final_population)))
print("Taxa de mutação: 5%")
print("Número de cidades: {}".format(cities_location.get_cities_count()))
print("Melhor solução: {}".format(best_distance))

plt.plot(cities_location.get_cities()[0], cities_location.get_cities()[1], 'ro')

best_chromosome_cities = best_chromosome.get_cities()
best_path_x = []
best_path_y = []
for i in range(len(best_chromosome_cities)):
    city = cities_location.get_city(best_chromosome_cities[i])
    best_path_x.append(city.x)
    best_path_y.append(city.y)

first_city = cities_location.get_city(best_chromosome_cities[0])
best_path_x.append(first_city.x)
best_path_y.append(first_city.y)

plt.plot(best_path_x, best_path_y)

plt.show()
