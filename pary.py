def koszt(a):
    w = 0
    while len(a) > 1:
        x = min(a)
        a.remove(x)
        y = min(a)
        a.remove(y)

        z = x + y
        w += z
        a.append(z)

        print(a, w)
    return a, w

def minimum(a):
    mini = a[0]
    for elem in a:
        if elem < mini:
            mini = elem
    return mini

def minimum2(a):
    mini = a[0]
    for i in range(1, len(a)):
        if a[i] < mini:
            mini = a[i]
            i_mini = i
    return mini, i_mini

def sortowanie(a):
    x = len(a)
    for i in range(1, x):
        temp = a[i]
        j=i-1
        while j>=0 and a[j]>temp:
            a[j+1]=a[j]
            j = j - 1
        a[j+1]=temp


def koszt2(a):
    w = 0
    s = len(a)
    while len(a) > 1:
        x = minimum(a)




a = [3, 2, 5, 7]
print(a)
sortowanie(a)
print(a)
koszt(a)
