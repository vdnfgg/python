def silnia(n):
    if n == 0:
        return 1
    return n*silnia(n-1)

print(silnia(5))

# zad 1
def silniaIteracja(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s

print(silniaIteracja(5))

# zad 2
def newton(n, k):
    n2 = 1
    for i in range(2, n + 1):
        n2 *= i

    k2 = 1
    for i in range(2, k + 1):
        k2 *= i

        return n2 / k2

print(newton(4, 3))
