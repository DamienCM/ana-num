from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')

fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')

# creation des données.
X = np.arange(-8, 8, 0.25)
Y = np.arange(-8, 8, 0.25)
X, Y = np.meshgrid(X, Y)
a, b = 2, 2 / 7

Z = np.sqrt(X ** 2 / a + Y ** 2 / b)
Zp = np.cos(X) * np.sin(Y)

# Plot la surface.
surf1 = ax1.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.6)
surf2 = ax2.plot_surface(X, Y, Zp, cmap=cm.coolwarm, alpha=0.6)
# Lignes de Champ
ax1.contour(X, Y, Z, 20, offset=0, zdir='z', cmap=cm.coolwarm)
ax1.contour(X, Y, Z, 20, zdir='z', cmap=cm.coolwarm)
ax2.contour(X, Y, Zp, 20, offset=-1, zdir='z', cmap=cm.coolwarm)
ax2.contour(X, Y, Zp, 20, zdir='z', cmap=cm.coolwarm)


fig1.suptitle("Graph de $g_{2,2/7}(x,y)$")
ax1.set_xlabel("x")
ax1.set_ylabel('y')
ax1.set_zlabel('z')

fig2.suptitle("Graph de $h(x,y)$")
ax2.set_xlabel("x")
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.set_xlim(-8,8)
ax2.set_ylim(-8,8)


fig1.savefig('./outC/figure1.png')
fig2.savefig('./outC/figure2.png')


# Question4
def g_ab(x, y, a=2, b=2 / 7):
    return np.sqrt(x ** 2 / a + y ** 2 / b)


def h(x, y):
    return np.cos(x) * np.sin(y)


def grad_g_ab(P, a=2, b=2 / 7):
    x, y = P
    return 2 * x / a, 2 * y / b


def grad_h(P):
    x, y = P
    return -np.sin(x) * np.sin(y), np.cos(x) * np.cos(y)


def norme(V):
    somme_quad = 0
    for xi in V:
        somme_quad += xi ** 2
    return somme_quad ** 0.5
    

P0 = (0, 0)
P1 = (1, 0)
P2 = (0, -1)
P3 = (1, 1)

print(norme(grad_g_ab(P1)))


# Question5-6 à finir....


def grad_pc(eps, m, u, xo, yo,
            df):  # methode pas ameliorée j'ai pas compris a quoi conrespondais les entrees df1,df2=df[0],df[1] = grad f
    n = 0
    while norme(df((xo, yo))) > eps or n > m:
        df1, df2 = df((xo, yo))
        df1 *= u
        df2 *= u
        xo += df1
        yo += df2
        n += 1
        ax2.scatter([xo], [yo], [h(xo, yo)], color='green', linewidth=1, alpha=1)

    if n > m:
        return None
    return xo, yo


Mi = (7, 1.5)
Mf = (grad_pc(10 ** -2, 10 ** 3, 10 ** -1, Mi[0], Mi[1], grad_h))
ax2.scatter([Mi[0]], [Mi[1]], [h(Mi[0], Mi[1])], color='yellow', linewidth=3, alpha=1)
ax2.scatter([Mf[0]], [Mf[1]], [h(Mf[0], Mf[1])], color='black', linewidth=3, alpha=1)

plt.show()
