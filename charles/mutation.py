from random import randint, sample

def template_mutation(individual):
    """[summary]

    Args:
        individual ([type]): [description]

    Returns:
        [type]: [description]
    """
    return individual


def binary_mutation(individual):
    """Binary muation for a GA individual

    Args:
        individual (Individual): A GA individual from charles libray.py

    Raises:
        Exception: When individual is not binary encoded.py

    Returns:
        Individual: Mutated Individual
    """
    mut_point = randint(0, len(individual) - 1)

    if individual[mut_point] == 0:
        individual[mut_point] = 1
    elif individual[mut_point] == 1:
        individual[mut_point] = 0
    else:
        raise Exception(f'Trying to do binary mutation on individual {individual}. But it is not binary')

    return individual


def swap_mutation(individual):
    idx1, idx2 = sample([i for i in range(len(individual))], 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

    return individual

def inversion_mutation(individual):
    """

    :param individual:
    :return: inplace modification of individual
    """
    i = individual #.copy()
    # find mutation upper and lower fence and sort it
    mut_points = sample(range(len(i)), 2)
    mut_points.sort()
    i[mut_points[0]:mut_points[1]] = i[mut_points[0]:mut_points[1]][::-1]
    return i


if __name__ == '__main__':
    ind = list(range(10))
    res = inversion_mutation(ind)
    res

