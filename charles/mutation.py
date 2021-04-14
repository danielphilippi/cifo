from random import randint


def binary_mutation(individual):
    """
    Bin mutation for GA individual
    :param individual: A GA ind from the charles lib
    :return: Mutated Individual
    """
    mut_point = randint(0, len(individual) - 1)

    if individual[mut_point] == 0:
        individual[mut_point] = 1
    elif individual[mut_point] == 1:
        individual[mut_point] = 0
    else:
        raise Exception(f'Trying to do binary mutation on individual {individual}. But it is not binary')

    return individual
