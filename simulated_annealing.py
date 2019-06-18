from time import time
from numpy import empty, arange, exp, copy, argmin, amin, amax, int64, std, mean
from numpy.random import choice, rand
from matplotlib.pyplot import plot, boxplot, hlines, legend, grid, savefig, title
from re import sub
from sys import argv


def read_data():
    if len(argv) == 1:
        return
    with open(argv[1] + ".dat") as file:
        quantity = int(file.readline())
        Flow = empty([quantity, quantity], int64)
        file.readline()  # ERASED
        for i in range(quantity):
            line = file.readline()
            line = line.strip(' \n')
            line = sub(' +', ' ', line)
            line = line.split(' ')
            for j in range(quantity):
                Flow[i][j] = int(line[j])
        Distance = empty([quantity, quantity], int64)
        file.readline()  # ERASED
        for i in range(quantity):
            line = file.readline()
            line = line.strip(' \n')
            line = sub(' +', ' ', line)
            line = line.split(' ')
            for j in range(quantity):
                Distance[i][j] = int(line[j])
    return quantity, Flow, Distance


quantity, Flow, Distance = read_data()


def read_solution():
    with open(argv[1] + ".sln") as file:
        line = file.readline()
        line = line.strip(' \n')
        line = sub(' +', ' ', line)
        line = line.split(' ')
        known_value = int(line[1])
    return known_value


known_value = read_solution()
print("Known Value: ", known_value)


def evaluate(solution):
    value = 0
    for i in range(quantity):
        for j in range(quantity):
            value = value + Flow[i][j] * Distance[solution[i], solution[j]]
    return value


def generate_neighbor(solution):
    neighbor = copy(solution)
    positions = choice(quantity, 2, False)
    pivot = neighbor[positions[0]]
    neighbor[positions[0]] = neighbor[positions[1]]
    neighbor[positions[1]] = pivot
    return neighbor


def generate_neighborhood(solution, neighbors):
    neighborhood = empty([neighbors, quantity], int64)
    for i in range(neighbors):
        neighbor = generate_neighbor(solution)
        neighborhood[i] = copy(neighbor)
    return neighborhood


def local_search(solution, neighbors):
    neighborhood = generate_neighborhood(solution, neighbors)
    values = empty(neighbors, int64)
    for i in range(neighbors):
        values[i] = evaluate(neighborhood[i])
    return neighborhood[argmin(values)], values[argmin(values)]


def simulated_annealing(iterations, stability, temperature):
    # evaluations = empty(iterations * stability)
    fitness = empty(iterations * stability)
    # solution = arange(quantity)
    solution = choice(quantity, quantity, False)
    value = evaluate(solution)
    delta = .98
    boltzmann = empty(1)
    probability = empty(1)
    start = time()
    for i in range(iterations):
        for j in range(stability):
            solution_, value_ = local_search(solution, neighbor_quantity)
            error = value_ - value
            if error < 0:
                value = value_
                solution = solution_
            else:
                boltzmann[0] = exp(-error/temperature)
                probability[0] = rand()
                if probability[0] < boltzmann[0]:
                    value = value_
                    solution = solution_
            fitness[(i * stability) + j] = value
        temperature = delta * temperature
    end = time()
    computation_time = end - start
    # if False:
    #     plot(fitness, label="fitness")
    #     hlines(known_value, 0, iterations * stability, 'g', label="optimum")
    #     grid(True)
    #     legend()
    #     savefig("test.png", dpi=200)
    return solution, value, computation_time


neighbor_quantity = 4
stability = 15
iterations = 2000
temperature = quantity * quantity * amax(Flow) * amax(Distance)


def test(length):
    # solutions = empty([length, quantity], int64)
    values = empty(length, int64)
    errors = empty(length)
    computation_times = empty(length)
    for i in range(length):
        print("Iteracion: ", i)
        temp = temperature
        solution, value, computation_time = simulated_annealing(iterations, stability, temp)
        # solutions[i] = copy(solution)
        print("Solution: ", solution)
        values[i] = value
        errors[i] = (value - known_value) * 100 / known_value
        computation_times[i] = computation_time
    print("Values: ", values)
    print("Proportional error: ", errors)
    print("Computation Times: ", computation_times)

    # boxplot(errors)
    # grid(True)

    # savefig("box.png", dpi=200)


test(11)
