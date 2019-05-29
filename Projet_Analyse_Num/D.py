import numpy as np



def G(A,y0, b):
    return 2 * (A * y0 - b)

def GradMat(A, y0, b, n):
    i = 0
    while i < n:
        if nozero(G(A,y0, b)):
            ro = (Norme(G(A,y0,b)) ** 2)/ (2 * G(A,y0, b).T * A * G(A,y0, b))
            print(ro)
        else:
            ro = 0
        y0 = y0 - ro * G(A,y0,b)
        i += 1
    return y0


def Norme(M):
    taille=M.shape[0]
    s = 0
    for i in range(taille):
        for j in range(taille):
            s = s + M[i][j]**2
    return np.sqrt(s)

def nozero(M):
    taille = M.shape[0]
    for i in range(taille):
        for j in range(taille):
            if M[i][j] == 0:
                return False
    return True


def phi(A,y,b):
    return y.T * A * y - 2 * y.T * b
print(GradMat(np.array([[4,1],[1,8]]),np.array([2,1]),np.array([1,2]),10))


