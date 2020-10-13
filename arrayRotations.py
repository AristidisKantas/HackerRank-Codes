def rotationLeft(a, d):
    for i in range(d):
        removed = a.pop(0)
        a.append(removed)
    return a

def rotationRight(A, K):

    aL = len(A) - 1
    for i in range(K):
        removed = A.pop(aL)
        A.insert(0,removed)
    return A
