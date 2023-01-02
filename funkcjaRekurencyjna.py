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
    return silniaIteracja(n) / (silniaIteracja(k) * silniaIteracja(n - k))

print(newton(4, 3))
