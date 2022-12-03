from random import *

def losuj(n):
    tab = []
    seed()
    for i in range(10):
        tab.append(randint(1, 20))
    return tab
tab = losuj(10)
print(tab)

"""
Skonstruuj algorytmy w postaci programu zestawem czterech 
funkcji sprawdzających, realizujących następujące operacje:

1.1 sprawdzenie, czy w ciągu wylosowanych liczb całkowitych znajduje się liczba podzielna przez 7

1.2 sprawdzenie, czy wszystkie wyrazy wylosowanego ciągu liczb calkowitych są większe od 5.

1.3 sprawdzenie, czy w n-elementowej tablicy calkowitych liczb losowych znajduje się liczba różna od 2

1.4 sprawdzenie, czy w 11-elementowej tablicy całkowitych liczb losowych z przedziału <0,33) wszystkie elementy nie są podzielne przez 4
"""


# Zad 1.1
def szukanieprzez7(tab):
    for i in tab:
        if i % 7 == 0:
            return True
    return False


print("Czy w tablicy jest liczba podzielna przez 7: ", end="")
print(szukanieprzez7(tab))


# Zad 1.2
def wiekszeod5(tab):
    for i in tab:
        if i <= 5:
            return False
    return True

print("Czy wszystkie liczby są wieksze od 5: ", end="")
print(wiekszeod5(tab))


# Zad 1.3
def czy2(tab):
    for i in tab:
        if i != 2:
            return True
    return False

print("Czy jest liczba różna od 2: ", end="")
print(czy2(tab))


# Zad 1.4
# losowanie tablicy <0, 33)
def losuj033(n):
    tab = []
    seed()
    for i in range(10):
        tab.append(randint(0, 32))
    return tab

tab033 = losuj033(11)

print("Tablica <0,33): ", end="")
print(tab033)

def przez4(tab):
    for i in tab:
        if i % 4 == 0:
            return True
    return False

print("Czy jest liczba podzielna przez 4: ", end="")
print(przez4(tab))
