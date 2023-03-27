def generujPierwsze(n):
    T=[0]
    for i in range(1,n+1):
        T+=[1]
    i=2
    while i<=n:
        if T[i]==0:
            i=i+1
        m=2*i	#pierwsza wielokrotność (*2)
        while m<=n:
            T[m]=0
            m=m+i	#kolejna wielokrotność
        i=i+1
    for indeks, wartosc in enumerate(T):
        if wartosc==1 and indeks > 1:
            print(indeks, end=" ")

#generujPierwsze(100)


def sitoEratostenesa(n):   #interesuje nas przedział [2,n]
    primes = [True]*(n+1)  #tablica liczb pierwszych (na początku wszystkie traktujemy   #jako pierwsze)zbudowana w ten sposób, że indeks elementu jest równy rozważanej liczbie
    tab = []
    for i in range(2,n+1):      #zaczynamy od 2
        if primes[i]:           #True oznacza liczbę niewykreśloną
            for j in range(i+i,n+1,i):     #pętla usuwająca wielokrotności
                primes[j] = False          #zaznaczamy usunięcie
    for i in range(2,n+1): #wyświetlamy na ekranie wszystko, co nie zostało wykreślone
        if primes[i]:
            #print(i, end=" ")
            tab.append(i)
    return tab

#print()
#sitoEratostenesa(12)
#print()
#sitoEratostenesa(11)


# Zad 1
def czy_pierwsza(x, n):
    pierwsze = sitoEratostenesa(n)
    return x in pierwsze

#print(czy_pierwsza(13, 100))
#print(czy_pierwsza(4, 100))


# Zad 2

# def czy_pierwsza2(n):
#     ile = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             ile += 1
#     if ile != 2:
#         return False
#     return True

from math import sqrt

def czy_pierwsza2(n):
    if n < 2 or n > 2 and n % 2 == 0:
        return False
    else:
        zakr = int(sqrt(n)) + 1
        for i in range(3, zakr, 2):
            if n % i == 0:
                return False
    return True

def czy_super_pierwsza(n):
    if czy_pierwsza2(n):
        n2 = str(n)
        suma = 0
        for i in range(len(n2)):
            suma += int(n2[i-1])

        if czy_pierwsza2(suma):
            return True
        else:
            return False
    else:
        return False

def ile_super_pierwszych(x, y):
    ile_super_pierwszych = 0
    for i in range(x, y):
        if czy_super_pierwsza(i):
            ile_super_pierwszych += 1
    return ile_super_pierwszych

print(ile_super_pierwszych(2, 1000))
print(ile_super_pierwszych(100, 10000))
print(ile_super_pierwszych(1000, 100000))


def binarne(n):
    i = 0
    tab = []
    while n != 0:
        tab.append(n % 2)
        n //= 2
        i += 1
    return tab[::-1]

#print(binarne(3))
#print(binarne(12))


def ile_superb_pierwszych(x, y):
    ilosc = 0
    for i in range(x, y+1):
        if czy_pierwsza2(i):
            if czy_super_pierwsza(i):
                if czy_pierwsza2(sum(binarne(i))):
                    ilosc += 1
    return ilosc

print(ile_superb_pierwszych(2, 1000))
print(ile_superb_pierwszych(100, 10000))
print(ile_superb_pierwszych(1000, 100000))
