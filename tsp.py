from charles.charles import Population, Individual
from charles.search import hill_climb, sim_annealing
from data.tsp_data import distance_matrix
from copy import deepcopy


def evaluate(self):
    """A simple objective function to calculate distances
    for the TSP problem.

    Returns:
        int: the total distance of the path
    """

    fitness = 0

    for i in range(len(self.representation)):
        # Calculates full distance, including from last city
        # to first, to terminate the trip
        fitness += distance_matrix[self.representation[i - 1]][self.representation[i]]

    return int(fitness)


def get_neighbours(self):
    """A neighbourhood function for the TSP problem. Switches
    indexes around in pairs.

    Returns:
        list: a list of individuals
    """
    n = [deepcopy(self.representation) for i in range(len(self.representation) - 1)]

    for count, i in enumerate(n):
        i[count], i[count + 1] = i[count + 1], i[count]

    n = [Individual(i) for i in n]
    return n


# Monkey patching
Individual.evaluate = evaluate
Individual.get_neighbours = get_neighbours


pop = Population(
    size=20,
    sol_size=len(distance_matrix[0]),
    valid_set=[i for i in range(len(distance_matrix[0]))],
    replacement=False,
    optim="min",
)


hill_climb(pop, log=0)
sim_annealing(pop, L=20, c=100)


# ToDO: selection with replacreent?!

"""
SELECTION
selection with replacement?!
- when calc probs for the first, said to reclalc probs for the 2nd (only when using cross over?!)


***MUTATION***
flip one bit with given prob 

***CROSSOVER***

One point Crossover
- cut strings at one point
- Offspring1: take first part of p1 and 2nd of parent 2
- Offspring2: vise verca

"""