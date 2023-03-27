from random import *

def plecak(W, C, waga):
    n = len(W)
    wynik = 0
    global K
    K = [0]*n
    for i in range(n):
        K[i] = waga // C[i]
        waga -= K[i] * C[i]
        wynik += K[i] * W[i]
    print(f"Wartość plecaka: {wynik}")
    print(f"Krotności z jakimi bierzemy przedmioty: {K}")

def plecak_decyzyjny(W, C, waga):
    n = len(W)
    wynik = 0
    K = [0]*n
    for i in range(n):
        if C[i] <= waga:
            K[i] = 1
            waga = waga - C[i]
            wynik = wynik + W[i]
        else:
            K[i] = 0
    print(wynik)
    print(K)

W = [8, 3, 1, 2, 1]
C = [4, 2, 1, 3, 7]
waga = 11

plecak(W, C, waga)
plecak_decyzyjny(W, C, waga)

def losuj(n):
    tab = []
    seed()
    for i in range(10):
        tab.append(1, 20)
    return tab

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
print()

zad31(W,C)

def sortowanie(a, b):
  x=len(W)
  c=-1
  tak = []
  for i in range(x):
    i=a[c]/b[c]
    c+=1
    tak.append(i)
    index = tak.index(i)
    print(a[c], ", ", b[c], " wartość kryterium: ", i)
  tak.sort()
  print(tak)

sortowanie(W,C)
