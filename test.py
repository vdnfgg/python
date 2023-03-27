def minimum(a):
    mini = a[0]
    for elem in a:
        if elem < mini:
            mini = elem
    return mini
