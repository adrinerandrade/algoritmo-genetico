class Chromosome:

    def __init__(self, cities):
        self.size = 20
        cities_set = set(cities)
        for city in cities:
            if city < 0 or city > 19:
                raise Exception('Cromossomo com cidade inválida: {}'.format(city))
        if len(cities_set) != self.size:
            raise Exception('Cromossomo inválido. Verifique se não está sendo criado cidades repetidas, ou com um tamanho inválido.')
        self.cities = cities

    def get_cities(self):
        return self.cities