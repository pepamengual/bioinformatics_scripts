import random
import matplotlib.pyplot as plt

def alphabet_maker(alphabet):
    alphabet_set = set()
    for letter in alphabet:
        alphabet_set.add(letter)
    alphabet_list = list(alphabet_set)
    return alphabet_list

def monkey_writting(word, alphabet_list, monkeys):
    characters = len(word)
    for monkey in range(monkeys):
        for typed_word_number in range(100000000):
            typed_word = "".join(random.choices(alphabet_list, k=characters))
            if typed_word == word:
                print(monkey, typed_word_number, typed_word)
                plt.scatter(monkey, typed_word_number)
                break
    plt.show()

def main():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_list = alphabet_maker(alphabet)
    word = "LIDA"
    monkeys = 100
    monkey_writting(word, alphabet_list, monkeys)
    
main()
