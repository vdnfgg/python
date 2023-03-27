from math import sqrt

def czy_pierwsza(n):
    ile = 0
    for i in range(1, n+1):
        if n % i == 0:
            ile += 1
    if ile != 2:
        return False
    return True

#print(czy_pierwsza(11))
#print(czy_pierwsza(4))

def czy_pierwsza_2(n):
    if n < 2 or n > 2 and n % 2 == 0:
        return False
    else:
        zakr = int(sqrt(n)) + 1
        for i in range(3, zakr, 2):
            if n % i == 0:
                return False
    return True

#print(czy_pierwsza_2(11))
#print(czy_pierwsza_2(4))

def rozloz(n):
    k = 2
    while n != 1:
        while n % k==0:
            print(k, end=" ")
            n = n // k
        k += 1

#n=int(input('podaj liczbę\n'))
#rozloz(n)


def rozloz_tab(n):
    czynniki = []
    k = 2
    while n != 1:
        while n % k == 0:
            czynniki.append(k)
            n //= k
        k += 1
    return czynniki

#print(rozloz_tab(100))


# Zad 2 a)
def czy_blizniacze(n1, n2):
    if czy_pierwsza_2(n1) and czy_pierwsza_2(n2):
        if n1 - n2 == 2 or n2 - n1 == 2:
            return True
    else:
        return False

print(czy_blizniacze(11, 13))
print(czy_blizniacze(25, 27))

# Zad 2 b)
def blizniacze_w_zakresie(n):
    liczby_blizniacze = []
    for i in range(n):
        if czy_blizniacze(i, i + 2):
            liczby_blizniacze.append((i, i + 2))
    return liczby_blizniacze

print(blizniacze_w_zakresie(100))


# Zad 3
def czy_doskonla(n):
    dzielniki = [1]
    for i in range(2, n):
        if n % i == 0:
            dzielniki.append(i)

    suma_dzielnikow = 0
    for i in dzielniki:
        suma_dzielnikow += i

    return suma_dzielnikow == n

print(czy_doskonla(496))
