def wydawanie(R):
    N = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    G = [50, 20, 10, 5, 2, 1]
    i = 0

    for y in N:
        y = int(input("Podaj niedostepny nominal(zl): "))
        if y == 0:
            break
        N.remove(y)
    for x in G:
        x = int(input("Podaj niedostepny nominal(gr): "))
        if x == 0:
            break
        G.remove(x)

    R_zl = int(R)
    R_gr = int(round((R - R_zl) * 100, 0))

    while R_zl > 0:
        if R_zl >= N[i]:
            L = R_zl // N[i]
            R_zl = R_zl - L * N[i]
            print(N[i], L, sep="->", end=", ")
        i += 1
    print()

    i = 0
    while R_gr > 0:
        if R_gr >= G[i]:
            L = R_gr // G[i]
            R_gr = R_gr - L * G[i]
            print(G[i], L, sep="->", end=", ")
        i += 1


try:
    wydawanie(146.29)
except:
    print("Error")
