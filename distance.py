import math

class DistanceResolver:

    def __init__(self, cities):
        self.cities = cities

    def get_distance(self, city_1, city_2):
        location_1 = self.cities.get_city(city_1)
        location_2 = self.cities.get_city(city_2)
        x_dist = location_2.x - location_1.x
        y_dist = location_2.y - location_1.y
        return math.sqrt(x_dist**2) + math.sqrt(y_dist**2)
    
    # Calcula a distancia das cidades
    def calculate_distance(self, chromosome):
        cities = chromosome.get_cities()
        path = cities[:]

        # Deve voltar a primeira cidade
        path.append(cities[0])

        total_distance = 0
        for i in range(len(cities)):
            city_1 = path[i]
            city_2 = path[i + 1]
            total_distance += self.get_distance(city_1, city_2)

        return total_distance
