from numpy import empty, arange, exp, copy, argmax
from numpy.random import choice, rand
from matplotlib.pyplot import plot, legend, grid, savefig
from re import sub
from sys import argv


def read_file():
    if len(argv) == 1:
        return
    with open(argv[1]) as file:
        quantity = int(file.readline())
        Flow = empty([quantity, quantity])
        file.readline()  # ERASED
        for i in range(quantity):
            line = file.readline()
            line = line.strip(' \n')
            line = sub(' +', ' ', line)
            line = line.split(' ')
            for j in range(quantity):
                Flow[i][j] = int(line[j])
        Distance = empty([quantity, quantity])
        file.readline()  # ERASED
        for i in range(quantity):
            line = file.readline()
            line = line.strip(' \n')
            line = sub(' +', ' ', line)
            line = line.split(' ')
            for j in range(quantity):
                Distance[i][j] = int(line[j])
    return quantity, Flow, Distance


def evaluate(quantity, Flow, Distance, solution):
    value = 0
    for i in range(quantity):
        for j in range(quantity):
            value = value + Flow[i][j] * Distance[solution[i], solution[j]]
    return value


def swap(quantity, solution):
    positions = choice(quantity, 2, False)
    pivot = solution[positions[0]]
    solution[positions[0]] = solution[positions[1]]
    solution[positions[1]] = pivot
    return solution


def generate_neighbor(quantity, solution):
    solution_ = copy(solution)
    positions = choice(quantity, 2, False)
    pivot = solution_[positions[0]]
    solution_[positions[0]] = solution_[positions[1]]
    solution_[positions[1]] = pivot
    return solution_


def generate_neighborhood(quantity, solution, neighbors):
    neighborhood = empty([neighbors, quantity])
    values = empty(neighbors)
    # print(neighborhood)
    row = arange(quantity)
    # print(row)
    for i in range(neighbors):
        neighbor = generate_neighbor(quantity, solution)
        neighborhood[i] = copy(neighbor)
        values[i] = evaluate(quantity, Flow, Distance, neighbor)
    return neighborhood, values


def simulated_annealing(quantity, Flow, Distance, iterations, temperature):
    evaluations = empty(iterations * 10)
    fitness = empty(iterations * 10)
    solution = arange(quantity)
    # solution = choice(quantity, quantity, False)
    delta = .95
    boltzmann = empty(1)
    probability = empty(1)
    value_ = evaluate(quantity, Flow, Distance, solution)
    for i in range(iterations):
        # print(temperature)
        for j in range(10):
            swap(quantity, solution)
            value = evaluate(quantity, Flow, Distance, solution)
            evaluations[(i * 10) + j] = value
            error = value - value_
            if error < 0:
                value_ = value
                solution_ = solution
            else:
                boltzmann[0] = exp(-error/temperature)
                probability[0] = rand()
                if probability[0] < boltzmann[0]:
                    value_ = value
                    solution_ = solution
            fitness[(i * 10) + j] = value_
        temperature = delta * temperature
    plot(evaluations, label="evaluations")
    plot(fitness, label="fitness")
    grid(True)
    legend()
    savefig("test.png")
    return solution_, value_


quantity, Flow, Distance = read_file()
# solution, value = simulated_annealing(quantity, Flow, Distance, 1000, 3000000)
# print()
# print(solution, value)

solution = arange(26)
for i in range(26):
    neighborhood, values = generate_neighborhood(26, solution, 3)
    index_ = argmax(values)
    print(neighborhood[index_])
    # solution = neighborhood[index_]
