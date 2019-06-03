from numpy import empty, arange, exp, copy, argmin, amax, dtype, int64
from numpy.random import choice, rand
from matplotlib.pyplot import plot, legend, grid, savefig
from re import sub
from sys import argv


def read_file():
    if len(argv) == 1:
        return
    with open(argv[1]) as file:
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


quantity, Flow, Distance = read_file()


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
    evaluations = empty(iterations * stability)
    fitness = empty(iterations * stability)
    solution = arange(quantity)
    # solution = choice(quantity, quantity, False)
    value = evaluate(solution)
    delta = .99
    boltzmann = empty(1)
    probability = empty(1)
    for i in range(iterations):
        for j in range(stability):
            # print("first: ", solution)
            solution_, value_ = local_search(solution, 5)
            evaluations[(i * stability) + j] = value_
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
            # print("second: ", solution)
        temperature = delta * temperature
    plot(evaluations, label="evaluations")
    plot(fitness, label="fitness")
    grid(True)
    legend()
    savefig("test.png")
    return solution, value


print(quantity)
print(amax(Flow))
print(amax(Distance))
temperature = quantity * amax(Flow) * amax(Distance)
print(temperature)

solution, value = simulated_annealing(1000, 20, temperature)
print()
print(solution, value)
