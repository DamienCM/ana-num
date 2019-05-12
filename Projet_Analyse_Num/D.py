import numpy as np

A = np.array([[1,4],[3,4]])

def G(y, b):
    return 2 * (A * y - b)

def GradMat(y, b,n):
    i = 0
    while i < n:
        if G(y, b).any != 0:
            ro = (NormeMat(y) ** 2) / (2 * G(y, b).T * A * G(y, b))
        else:
            ro = 0
        y = y - ro * G(y,b)
        i += 1
    return y

def NormeMat(M):
    return np.linalg.norm(M)

def phi(y,b):
    return y.T * A * y - 2 * y.T * b

print(GradMat([5,8],[2,4],10))