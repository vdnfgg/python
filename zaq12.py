def moveTower(n, A, B, C):
    if n >= 1:
        moveTower(n - 1, A, B, C)

        moveDisk(A, C)

        moveTower(n - 1, B, C, A)

def moveDisk(fp, tp):
    print("moving disk from ", fp, " to ", tp)

moveTower(3, "A", "B", "C")
