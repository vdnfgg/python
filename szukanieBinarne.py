# Zad 1
def binarySearch(array, target):
    max = len(array) - 1
    #print(max)
    min = 0
    #print(min)
    i = 0
    while max >= min:
        i += 1
        x = min + max
        guess = x // 2
        print("Index sprawdzaniej liczby: " + str(guess))
        if array[guess] == target:
            print("Liczba porónań: " + str(i))
            return f"Guess: {guess}"
        else:
            if array[guess] < target:
                min = guess + 1
            else:
                max = guess - 1
    return -1

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(f"Primes: {primes}")
print(binarySearch(primes, 11))
print()


# Zad 2
from random import *

def binarySearch2(array, target):
    array.sort()
    max = len(array) - 1
    #print(max)
    min = 0
    #print(min)
    i = 0
    while max >= min:
        i += 1
        x = min + max
        guess = x // 2
        print("Index sprawdzaniej liczby: " + str(guess))
        if array[guess] == target:
            print(f"Liczba porównań: {i}")
            z = 0
            for i in array:
                if i == array[guess]:
                    z += 1
            return f"Wartość guess: {guess}, ilość: {z}"
        else:
            if array[guess] < target:
                min = guess + 1
            else:
                max = guess - 1
    return "Szukana liczba nie została odnaleziona."

def losuj(n):
    tab = []
    seed()
    for i in range(n):
        tab.append(randint(1, 10))
    return tab


tab = losuj(20)
print(tab)

print(binarySearch2(tab, 2))
