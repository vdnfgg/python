def wstawianie(tab, a):

    for i in range(len(tab)):
        if tab[i] > a:
            index = i
            break

    if index == len(tab):
        tab = tab[:index] + [a]
    else:
        tab = tab[:index] + [a] + tab[index:]
    return tab

tab = [1, 2, 3, 5, 6]
print(wstawianie(tab, 4))
