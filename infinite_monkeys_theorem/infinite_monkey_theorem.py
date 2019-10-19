import matplotlib.pyplot as plt
import numpy as np

def compute_probability(starting_monkeys, odds, iterations, characters):
    for i in range(iterations):
        starting_monkeys = int(starting_monkeys * 2)
        success_probability = 1 - ((1 - (1/(odds**characters)))**starting_monkeys)
        print(starting_monkeys, success_probability)
        plt.scatter(x = i, y = success_probability)
        plt.xlabel("Number of iterations (n); Number of monkeys: $2^n$")
        plt.ylabel("Probability of randomly typing a world of {} \ncharacters with a probability of 1/{}".format(characters, odds))
    plt.show()

def main():
    odds = 27
    starting_monkeys = 1
    iterations = 40
    characters = 4
    compute_probability(starting_monkeys, odds, iterations, characters)



main()


