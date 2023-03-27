#zad 1

#1
def nwdzodejmowaniem(a, b):
    while a != b:
        if a < b:
            b = b - a
        else:
            a = a - b
    return a

print(nwdzodejmowaniem(1071, 1029))

#2 - definicja rekurencyjna
def nwd1(a, b):
    if a == b:
        return a
    if a > b:
        return nwd1(a - b, b)
    return nwd1(a, b - a)

print(nwd1(1071, 1029))


#3
def nwdzdzieleniem(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    else:
        return a

print(nwdzdzieleniem(1071, 1029))

#4
def nwdrekurencyjne(a, b):
    if b > 0:
        return nwdrekurencyjne(b, a%b)
    return a

print(nwdrekurencyjne(1071, 1029))

#5 nww
def nww(a, b):
    ab = a * b
    while b != 0:
        r = a % b
        a = b
        b = r
    ab /= a
    return int(ab)

print(nww(32, 44))


#zad 2
def ulamki(licznik, mianownik):
    if licznik < mianownik:
        return "Nie da sie skrocic"
    if licznik % mianownik == 0:
        return licznik // mianownik

    jednosci = licznik // mianownik

    licznik2 = licznik
    for i in range(licznik // mianownik):
        licznik2 -= mianownik

    a = licznik2
    b = mianownik
    while b > 0:
        r = a % b
        a = b
        b = r
    dzielnik = a

    return f"{jednosci} i {int(licznik2 / dzielnik)}/{int(mianownik / dzielnik)}"

print(ulamki(20, 10))
print(ulamki(2058, 1071))
