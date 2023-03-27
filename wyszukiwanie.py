def szukaj(tekst, wzorzec):
    dlT, dlW = len(tekst), len(wzorzec)
    T = []
    if dlW > dlT:
        return False
    for i in range(dlT-dlW+1):
        for j in range(i, i+dlW):
            if tekst[j]!=wzorzec[j-i]:
                break
            if j+1 == i+dlW:
                T.append(i)
    if T == []:
        return False
    return T

print(szukaj("karykatura", "ka"))


def szukaj2(tekst, wzorzec):
    dlT, dlW = len(tekst), len(wzorzec)
    T = []
    if dlW > dlT:
        return False
    for i in range(dlT-dlW+1):
        for j in range(i, i+dlW):
            if tekst[j]!=wzorzec[j-i]:
                break
            if j+1 == i+dlW:
                T.append(i)
    if T == []:
        return False
    l = len(T)
    return l

print(szukaj2("karykatura", "ka"))


def szukaj3(tekst, wzorzec):
    dlT, dlW = len(tekst), len(wzorzec)
    T = []
    if dlW > dlT:
        return False
    for i in range(dlT-dlW+1):
        for j in range(i, i+dlW):
            if tekst[j]!=wzorzec[j-i]:
                break
            if j+1 == i+dlW:
                T.append(i)
    if T == []:
        return False
    return T[0]

print(szukaj3("karykatura", "ka"))


def szukaj4(tekst, wzorzec):
    dlT, dlW = len(tekst), len(wzorzec)
    T = []
    if dlW > dlT:
        return False
    for i in range(dlT-dlW+1):
        for j in range(i, i+dlW):
            if tekst[j]!=wzorzec[j-i]:
                break
            if j+1 == i+dlW:
                T.append(i)
    if T == []:
        return False
    return T[-1]

print(szukaj4("karykatura", "ka"))


def szukaj5(tekst, wzorzec):
    dlT, dlW = len(tekst), len(wzorzec)
    if dlW > dlT:
        return False
    for i in range(dlT-dlW+1):
        for j in range(i, i+dlW):
            if tekst[j]!=wzorzec[j-i]:
                break
            if j+1 == i+dlW:
                print(i, end=", ")

print(szukaj5("Karykatura", "ka"))