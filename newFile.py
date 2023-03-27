T = [12, -4, 6]
def d(x):
    n = len(T)
    T[n] = x
    s = n
    while ((s // 2) >= 1) and (T[s] > T[s // 2]):
        pom = T[s]
        T[s] = T[s // 2]
        T[s // 2] = pom
        s = s // 2
    return T

print(d(12))
