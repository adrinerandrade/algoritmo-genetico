from random import randint

class Roulette:

    def __init__(self, parents):
        self.total = 0.0
        for parent in parents:
            self.total += 1/parent[1]

        self.probs = list(map(lambda parent: (parent[0], (1/parent[1])/self.total), parents))
        self.probs.sort(key=lambda tup: tup[1])
        for i in range(1, len(self.probs) - 1):
            self.probs[i] = (self.probs[i][0], self.probs[i - 1][1] + self.probs[i][1])

        last_index = len(self.probs) - 1
        self.probs[last_index] = (self.probs[last_index][0], 1)

    def select_parent(self):
        number = randint(1, 10000) / 10000
        for i in range(len(self.probs)):
            if number <= self.probs[i][1]:
                return self.probs[i][0]
        print('Não deveria dar este erro. Roleta não encontrou, retornando o de maior probabilidade')
        return self.probs[i][0]
            
