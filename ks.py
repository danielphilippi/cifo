from charles.charles import Population, Individual
from copy import deepcopy
from data.ks_data import values, weights, capacity
from charles.selection import fps
from charles.mutation import binary_mutation
from charles.crossover import single_point_crossover
from random import random
from operator import attrgetter

"""
why pop?

"""
def evaluate(self):
    fitness = 0
    weight = 0
    for bit in range(len(self.representation)):
        if self.representation[bit] == 1:
            fitness += values[bit]
            weight += weights[bit]
    if weight > capacity:
        fitness = capacity - weight

    return fitness


def get_neighbours(self):
    n = [deepcopy(self.representation) for i in range(len(self.representation))]

    for count, i in enumerate(n):
        if i[count] == 1:
            i[count] = 0
        elif i[count] == 0:
            i[count] = 1

    n = [Individual(i) for i in n]
    return n


Individual.evaluate = evaluate
Individual.get_neighbours = get_neighbours

# look up init from Population...
pop = Population(
    size=20, optim='max', sol_size=len(values), valid_set=[0,1], replacement=True
)

#hill_climb(pop, log=1)
#sim_annealing(pop, L=20, c=100)

n_generations = 100
prob_co = 0.5
prob_m = 0.5
for i in range(n_generations):
    new_pop = []
    while len(new_pop) < len(pop):
        parent1, parent2 = fps(pop), fps(pop)
        # crossover
        if random() < prob_co: # if rand(0,1) is smaller than prob_co
            offspring1, offspring2 = single_point_crossover(parent1, parent2)
        else:
            offspring1, offspring2 = parent1, parent2

        # mutation
        if random() < prob_m:
            offspring1 = binary_mutation(offspring1)
        if random() < prob_m:
            offspring2 = binary_mutation(offspring2)

        new_pop.append(Individual(representation=offspring1))
        new_pop.append(Individual(representation=offspring2))
    pop.individuals = new_pop
    print(f'Best indiv: {max(pop, key=attrgetter("fitness"))}')
