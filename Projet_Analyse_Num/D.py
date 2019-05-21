import numpy as np

A = np.array([[3,5],[5,3]])

def G(y, b):
    return 2 * (A * y - b)

def GradMat(y, b,n):
    i = 0
    while i < n:
        if nozero(G(y, b)):
            ro = (Norme(G(y,b)) ** 2)/ (2 * G(y, b).T * A * G(y, b))
        else:
            ro = 0
        y = y - ro * G(y,b)
        i += 1
    return y


def Norme(M):
    taille=M.shape[0]
    s = 0
    for i in range(taille):
        for j in range(taille):
            s = s + M[i][j]**2
    return np.sqrt(s)

def nozero(M):
    taille = M.shape[0]
    s = 0
    for i in range(taille):
        for j in range(taille):
            if M[i][j] == 0:
                return False
            else:
                return True


def phi(y,b):
    return y.T * A * y - 2 * y.T * b
print(GradMat(np.array([[1,2],[2,3]]),np.array([1,1]),5))


