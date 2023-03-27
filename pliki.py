# 🤯 🤯 🤯 🤯 🤯
otworz = open("liczby.txt")
liczby = otworz.read().split()
otworz.close()

#print(liczby)

liczby2 = []
for el in liczby:
    liczby2.append(int(el))

#print(liczby2)

dane = []
text_file = open("liczby.txt", "r")
for line in text_file:
    dane.append(int(line))

text_file.close()

#print(dane)


dane2 = []
text_filE = open("dane1.1.txt", "r")
for i in text_filE:
    dane2.append(i.strip().split())

text_filE.close()

#print(dane2)


# plik = open("pliki.txt", "w")
# for i in range(1, 11):
#     plik.write(f"{i}\n")
#
# plik.close()


liczby = open("liczby(matura).txt")
pierwsze = open("pierwsze.txt")

liczby_tab = []

for i in liczby:
    liczby_tab.append(int(i))
liczby.close()

pierwsze_tab = []

for i in pierwsze:
    pierwsze_tab.append(int(i))
pierwsze.close()
#print(pierwsze_tab)
#print(liczby_tab)

from math import *

def czy_pierwsza_2(n):
    if n < 2 or n > 2 and n % 2 == 0:
        return False
    else:
        zakr = int(sqrt(n)) + 1
        for i in range(3, zakr, 2):
            if n % i == 0:
                return False
    return True

def zad41(tab):
    liczby = []
    for i in tab:
        if i >= 100 and i <= 5000:
            if czy_pierwsza_2(i):
                liczby.append(i)
    return liczby

odpowiedz41 = zad41(liczby_tab)

wynik = open("wynik4_1.txt", "w")

for i in odpowiedz41:
    wynik.write(f"{i}\n")

wynik.close()



def zad42(tab):
    odpowiedzi = []
    for i in tab:
        i = str(i)[::-1]
        i = int(i)
        if czy_pierwsza_2(i):
            odpowiedzi.append(i)
    return odpowiedzi

#print(zad42(pierwsze_tab))


def zadanie(licz):
    waga = 0
    while licz > 0:
        waga += licz % 10
        licz //= 10
    return waga

with open("pierwsze.txt") as file:
    tabela = [int(line) for line in file.readlines()]

ile = 0
for licz in tabela:
    waga = zadanie(licz)
    while waga >= 10:
        waga = zadanie(waga)
    if waga == 1:
        ile += 1


with open("wynik4_3.txt", "w") as file:
    file.write(str(ile))
