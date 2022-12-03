from random import *

def plecak(W, C, waga):
    n = len(W)
    wynik = 0
    global K
    K = [0] * n
    for i in range(n):
        K[i] = waga // C[i]
        waga -= K[i] * C[i]
        wynik += K[i] * W[i]
    print(f"Wartość plecaka: {wynik}")
    print(f"Krotności z jakimi bierzemy przedmioty: {K}")

W = [8, 3, 1, 2, 1] # wartosc
C = [4, 3, 2, 4, 7] # masa

waga = 11
plecak(W, C, waga)

"""
3. Napisz program, który: wypełnia tablicę wartości (W) I masy (C) 
przedmiotów liczbami losowymi i sortuje obie tablice równolegle wg kryterium opłacalności (stosunek
wartość/masa). Sprawdź działanie programów z zadań 1,2.

4. Napisz program do rozwiązywania problemu plecakowego, którego wynikiem będzie wypisanie na ekranie:

a. w pierwszym wierszu-elementów umieszczonych w plecaku
b. w drugim wierszu- elementów, które się w plecaku nie znalazły
"""


# K - ilosci
# W - wartosci
# i jeszcze 'global K'
def umieszczone():
    print("Elementy umieszczone w plecaku (wartosc - ilosc): ", end="")
    x = -1
    for z in K:
        x += 1
        if z > 0:
            print(W[x], " - ", z, end=", ")
    print()

def nieumieszczone():
    print("Elementy nieumieszczone w plecaku: ", end="")
    x = -1
    for z in K:
        x += 1
        if z == 0:
            print(W[x], end=", ")
    print()

umieszczone()
nieumieszczone()

def zad31(a, b):
    x = len(W)
    W.clear()
    for z in range(x):
        W.append(randint(1, 20))
    a = []
    a.append(W)

    y = len(C)
    C.clear()
    for c in range(y):
        C.append(randint(1, 20))
    b = []
    b.append(C)
    return a, b

zad31(W, C)
