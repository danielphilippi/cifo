from random import randint, sample, shuffle


def template_co(p1, p2):
    """[summary]

    Args:
        p1 ([type]): [description]
        p2 ([type]): [description]

    Returns:
        [type]: [description]
    """

    return offspring1, offspring2


def single_point_crossover(p1, p2):
    """Implementation of single point crossover.

    Args:
        p1 (Individual): First parent for crossover.
        p2 (Individual): Second parent for crossover.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    co_point = randint(1, len(p1) - 1)

    offspring1 = p1[:co_point] + p2[co_point:]
    offspring2 = p2[:co_point] + p1[co_point:]

    return offspring1, offspring2


def cycle_co(p1, p2):
    offspring1 = [None for _ in range(len(p1))]
    offspring2 = offspring1.copy()

    # l = [None,None,1]

    # start new cycle as long as there are Nones in the offspring
    while None in offspring1:
        # choose random pos in offspring where value is None
        pos = sample([i for i in range(len(offspring1)) if offspring1[i] is None], 1)[0]

        val1 = p1[pos]
        val2 = p2[pos]
        offspring1[pos] = val1
        offspring2[pos] = val2

        # continue cycle as long as vals differ
        while val1 != val2:
            pos = p1.index(val2)
            val1 = p1[pos]
            val2 = p2[pos]
            offspring1[pos] = val1
            offspring2[pos] = val2

    return offspring1, offspring2


def arithmetic_co(p1, p2):
    # init offspring with None
    offspring1 = [None for _ in range(len(p1))]
    offspring2 = offspring1.copy()

    # set alpha val within [0,1]
    a = 0.4

    #
    # use loop to be prepared to exec operation on a subset of parents only
    for i in range(len(p1)):
        offspring1[i] = a * p1[i] + (1 - a) * p2[i]
        offspring2[i] = (1 - a) * p1[i] + a * p2[i]


if __name__ == '__main__':
    p1 = list(range(10))
    shuffle(p1)
    p2 = list(range(10))
    shuffle(p2)

    res = arithmetic_co(p1, p2)
    res




