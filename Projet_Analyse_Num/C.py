from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')

fig2 = plt.figure()
ax2 = fig2.gca(projection='3d')

xlim1 = (-4, 4)
ylim1 = (-4, 4)

xlim2 = (-4, 4)
ylim2 = (-4, 2)
# creation des données.
X1 = np.arange(xlim1[0], xlim1[1], 0.25)
Y1 = np.arange(ylim1[0], ylim1[1], 0.25)
X2 = np.arange(xlim2[0], xlim2[1], 0.25)
Y2 = np.arange(ylim2[0], ylim2[1], 0.25)
X1, Y1 = np.meshgrid(X1, Y1)
X2, Y2 = np.meshgrid(X2, Y2)

a, b = 2, 2 / 7

Z1 = np.sqrt(X1 ** 2 / a + Y1 ** 2 / b)
Z2 = np.cos(X2) * np.sin(Y2)

# Plot la surface.
ax1.plot_surface(X1, Y1, Z1, cmap=cm.coolwarm, alpha=0.4)
ax2.plot_surface(X2, Y2, Z2, cmap=cm.coolwarm, alpha=0.4)
# Lignes de Champ
ax1.contour(X1, Y1, Z1, 20, offset=0, zdir='z', cmap=cm.coolwarm)
ax2.contour(X2, Y2, Z2, 20, offset=-1, zdir='z', cmap=cm.coolwarm)
ax1.contour(X1, Y1, Z1, 20, zdir='z', cmap=cm.coolwarm)
ax2.contour(X2, Y2, Z2, 20, zdir='z', cmap=cm.coolwarm)

fig1.suptitle("Graph de $g_{2,2/7}(x,y)$")
ax1.set_xlabel("x")
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.set_xlim(xlim1[0], xlim1[1])
ax1.set_ylim(ylim1[0], ylim1[1])

fig2.suptitle("Graph de $h(x,y)$")
ax2.set_xlabel("x")
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.set_xlim(xlim2[0], xlim2[1])
ax2.set_ylim(ylim2[0], ylim2[1])

fig1.savefig('./outC/Q1g.png')
fig2.savefig('./outC/Q2h.png')


# Question4
def g_ab(x, y):
    global a,b
    return np.sqrt(x ** 2 / a + y ** 2 / b)


def h(x, y):
    return np.cos(x) * np.sin(y)


def grad_g_ab(x, y):
    global  a,b
    return 2 * x / a, 2 * y / b


def grad_h(x, y):
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
P = [P0, P1, P2, P3]

string = ""
string += "Question 4" + '\n'
for i in range(len(P)):
    string += "grad_g_ab" + str(P[i]) + " = " + str(grad_g_ab(P[i][0], P[i][1])) + '\n'
    string += "grad_h(" + str(P[i]) + ")=" + str(grad_h(P[i][0], P[i][1])) + '\n'

file = open('./outC/Question4.txt', 'w')
file.write(string)
file.close()




def grad_pc(eps, m, u, xo, yo, df,
            f):  # methode pas ameliorée j'ai pas compris a quoi conrespondais les entrees df1,df2 je suppose df1,df2=df[0],df[1] = grad f
    n = 0
    X = [xo]
    Y = [yo]
    Z = [f(xo, yo)]
    while norme(df(xo, yo)) > eps and n < m:
        df1, df2 = df(xo, yo)
        df1 *= u
        df2 *= u
        xo += df1
        yo += df2
        n+= 1
        X.append(xo)
        Y.append(yo)
        Z.append(f(xo, yo))
    return X, Y, Z


# Question 6

ax1.cla()
ax2.cla()

xlim1 = (-4, 4)
ylim1 = (-4, 4)

xlim2 = (4.7, 8)
ylim2 = (0, 3.141592)

# creation des données.
X1 = np.arange(xlim1[0], xlim1[1], 0.25)
Y1 = np.arange(ylim1[0], ylim1[1], 0.25)

X2 = np.arange(xlim2[0], xlim2[1], 0.25)
Y2 = np.arange(ylim2[0], ylim2[1], 0.25)

X1, Y1 = np.meshgrid(X1, Y1)
X2, Y2 = np.meshgrid(X2, Y2)

a, b = 2, 2 / 7

Z1 = np.sqrt(X1 ** 2 / a + Y1 ** 2 / b)
Z2 = np.cos(X2) * np.sin(Y2)

# Lignes de Champ
ax1.contour(X1, Y1, Z1, 30, zdir='z', cmap=cm.coolwarm)
ax1.plot_surface(X1, Y1, Z1, cmap=cm.coolwarm, alpha=0.4)

ax2.contour(X2, Y2, Z2, 25, zdir='z', cmap=cm.coolwarm)
ax2.plot_surface(X2, Y2, Z2, cmap=cm.coolwarm, alpha=0.4)

fig1.suptitle("Graph de $g_{2,2/7}(x,y)$")
ax1.set_xlabel("x")
ax1.set_ylabel('y')
ax1.set_zlabel('z')
ax1.set_xlim(xlim1[0], xlim1[1])
ax1.set_ylim(ylim1[0], ylim1[1])

fig2.suptitle("Graph de $h(x,y)$")
ax2.set_xlabel("x")
ax2.set_ylabel('y')
ax2.set_zlabel('z')
ax2.set_xlim(xlim2[0], xlim2[1])
ax2.set_ylim(ylim2[0], ylim2[1])

Pg = (0, 0)
X, Y, Z = grad_pc(0.1, 100, 0.1, Pg[0], Pg[1], grad_g_ab, g_ab)
ax1.scatter(X, Y, Z, color='black', linewidth=3)

Ph = (7, 1.5)
X, Y, Z = grad_pc(0.1, 100, 0.1, Ph[0], Ph[1], grad_h, h)
ax2.plot(X, Y, Z, color='black', linewidth=3)

fig1.savefig('./outC/Q6g.png')
fig2.savefig('./outC/Q6h.png')

# question 7

fig3 = plt.figure(3)
ax3=fig3.gca()

ecarts = []
a, b = 1, 20
eps = 10 ** -5
m = 120
# On part le point suivant
xo, yo = (-4, 4)
U = np.linspace(-0.99, -0.001, 500)

for u in U:
    X, Y, Z = grad_pc(eps, m, u, xo, yo, grad_g_ab, g_ab)
    ecarts.append((X[-1] ** 2 + Y[-1] ** 2) ** 0.5)

ax3.plot(U,ecarts)
ax3.grid()
fig3.suptitle("Ecarts en fonction de u")
fig3.savefig('./outC/Q7.png')
#interpretation
# un pas trop faible implique que l'on peut ne pas forcement arriver à la solution avant les 120 iterations
# un pas trop grand peut 'jongler' a coté de la solution


plt.show()