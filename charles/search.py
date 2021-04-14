from random import choice, uniform
from math import exp


def hill_climb(search_space, log=0):
    """Hill climbs a given search space.

    Args:
        search_space (Population): A Population of solutions
        log (int, optional): Prints info while running if set to 1. Defaults to 0.

    Raises:
        Exception: When unsure if facing maximization or minimization problem.

    Returns:
        Individual: Local optima Individual found in the search.
    """
    # Select a random solution
    start = choice(search_space)
    position = start
    # Counter to ensure we don't loop
    # infinitely if stuck in a plateu of optimas
    iter_plateu = 0
    
    if log == 1:
        print(f"Initial position: {start}")

    while True:
        # Return solution if we found same fitness
        # 5 times - to avoid infinite loop
        if iter_plateu >= 5:
            print(f"Best solution found: {position}")
            return position

        n = position.get_neighbours()
        n_fit = [i.fitness for i in n]

        if search_space.optim == "max":
            best_n = n[n_fit.index(max(n_fit))]
            if best_n.fitness > position.fitness:
                if log == 1:
                    print(f"Found better solution: {best_n}")
                iter_plateu = 0
                position = best_n
            elif best_n.fitness == position.fitness:
                if log == 1:
                    print(f"Found better solution: {best_n}")
                iter_plateu += 1
                position = best_n
            else:
                print(f"Best solution found: {position}")
                return position

        elif search_space.optim == "min":
            best_n = n[n_fit.index(min(n_fit))]
            if best_n.fitness < position.fitness:
                if log == 1:
                    print(f"Found better solution: {best_n}")
                iter_plateu = 0
                position = best_n
            elif best_n.fitness == position.fitness:
                if log == 1:
                    print(f"Found better solution: {best_n}")
                iter_plateu += 1
                position = best_n
            else:
                print(f"Best solution found: {position}")
                return position
        
        else:
            raise Exception("Problem doesn't specify if minimization or maximization.")


def sim_annealing(search_space, L, c, alpha=.95):
    # Init
    start = choice(search_space)
    # let current solution equal starting point
    position = start
    elite = position
    # Init L and C
    L, c = L, c
    # while repeat until term cond
    while c > 0.05:
        # repeat L times
        for _ in range(L):
            # generate neighbor
            # here we first generate all possible neigbors and than make a choice
            # ToDo: pass size arg to get_neigbours()
            sol = choice(position.get_neighbours())
            # if neigh is better or equal take
            if sol.fitness >= position.fitness:
                position = sol
                if position.fitness >= elite.fitness:
                    elite = position
            # elif some weired fct, take if met
            else:
                p = uniform(0,1)
                pc = exp(-abs(sol.fitness - position.fitness)/c)
                if p < pc:
                    position = sol
                pass
        # Update c and L
        c = c * alpha
    print(f'Sim returned: {position}')
    print(f'Best solution found: {elite}')
    return position
