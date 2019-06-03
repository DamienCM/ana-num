import numpy as np


def G(A, y0, b):
    return 2 * (A * y0 - b)


def NormeMatrice(M):
    taille = M.shape[0]
    s = 0
    for i in range(taille):
        for j in range(taille):
            s = s + M[i][j] ** 2
    return np.sqrt(s)


def norme(M):
    return np.linalg.norm(M)


def nozero(M):
    taille = M.shape[0]
    for i in range(taille):
        for j in range(taille):
            if M[i][j] == 0:
                return False
    return True


def gradopt(A, b, y0, eps, m):
    n = 0
    g = 2 * (A * y0 - b)
    ro = (norme(g) ** 2) / (2 * g.T * A * g)
    y1 = y0 - ro * g
    while n < m and norme(y1 - y0) >= eps:
        y0 = y1
        g = 2 * (A * y0 - b)
        if nozero(g):
            ro = ro = (norme(g) ** 2) / (2 * g.T * A * g)
        else:
            ro = 0
        y1 = y0 - ro * g
        n = n + 1
    return y1
