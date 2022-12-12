from math import *

def f1(x):
    return 2*x*x + 3*x - 5

def f2(x):
    return cos(x) + 2 * sin(x)

def f3(x):
    return 2*x**3 - x*x + 3*x - 14

def biskekcja(a, b, e, f):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    while b - a > e:
        s = (a + b) / 2
        if f(s) == 0:
            return s
        if f(a) * f(s) < 0:
            b = s
        else:
            a = s
    return (a + b) / 2


print(biskekcja(-1 ,2, 0.000001, f1))

print(biskekcja(0, 4, 0.000001, f2))

print(biskekcja(0, 2, 0.000001, f3))


def fa(x):
    return x**3 + 5*x - 3

def fb(x):
    return x**3 - 8


def bisekcjaL(a, b, L, f):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    for i in range(L):
        s = (a + b) / 2
        if f(s) == 0:
            return s
        if f(a) * f(s) < 0:
            b = s
        else:
            a = s
    return (a + b) / 2

# Zad 2 a)
print(bisekcjaL(-2, 2, 10, fa))
print(bisekcjaL(-2, 2, 100, fa))

# Zad 2 b)
print(bisekcjaL(0, 4, 12, fb))
print(bisekcjaL(0, 4, 50, fb))
