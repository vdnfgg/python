from random import *

def losuj(n):
    tab = []
    seed()
    for i in range(10):
        tab.append(randint(7, 20))
    return tab

def szukaj1(a, tab):
    n = len(tab)
    i = 0
    while i < n and tab[i] != a:
        i += 1
    if i == n:
        return False
    return True

tab = losuj(20)
a = 2
print(tab)
print(a)


def szukaj2(a, tab):
    n = len(tab)
    i = 0
    tab.insert(n, a)
    while tab[i] != a:
        i += 1
    if i < n:
        return True
    return False

print(szukaj1(2, tab))
print(szukaj2(2, tab))


# Zadanie 1.1
def szukajv2(tab):
    for i in tab:
        if i % 7 == 0:
            return True
    return False

print(szukajv2(tab))

# Zadanie 1.2
def szukajv3(tab):
    for i in tab:
        if i <= 5:
            return False
    return True
