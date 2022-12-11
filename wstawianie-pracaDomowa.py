"""
Praca domowa
Podaj specyfikację zadania i napisz program realizujący wstawianie liczby wprowadzonej z
klawiatury lub podanej jako parametr funkcji do uporządkowanego ciągu liczbowego w takie miejsce,
aby po jej wstawieniu ciąg nadal był uporządkowany. Algorytm powinien wyznaczać pozycję
wstawienia liczby do uporządkowanego zbioru. Do wstawiania możesz wykorzystać metodę insert().
"""

def sortadd(array, a):

    # szukanie miejsca do wstawienia
    for i in range(len(array)):
        if array[i] > a:
            index = i
            break

    # wstawianie do tablicy
    if index == len(array):
        array = array[:index] + [a]
    else:
        array = array[:index] + [a] + array[index:]
    return array

tab = [1, 2, 3, 5, 6]
print(sortadd(tab, 4))
