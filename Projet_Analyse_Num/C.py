from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import os

if not os.path.isdir("outC"):
	os.mkdir("outC")


# region question 1-2
def g_ab(x, y):
	global a, b
	return np.sqrt(x ** 2 / a + y ** 2 / b)


def h(x, y):
	return np.cos(x) * np.sin(y)


fig_g = plt.figure()
ax_g = fig_g.gca(projection='3d')

fig_h = plt.figure()
ax_h = fig_h.gca(projection='3d')

xlim_g = (-4, 4)
ylim_g = (-4, 4)

xlim_h = (-4, 4)
ylim_h = (-4, 2)
# creation des données.
X_g = np.arange(xlim_g[0], xlim_g[1], 0.25)
Y_g = np.arange(ylim_g[0], ylim_g[1], 0.25)
X_h = np.arange(xlim_h[0], xlim_h[1], 0.25)
Y_h = np.arange(ylim_h[0], ylim_h[1], 0.25)
XX_g, YY_g = np.meshgrid(X_g, Y_g)
XX_h, YY_h = np.meshgrid(X_h, Y_h)

a, b = 2, 2 / 7

# Calcul de la valeur de la fonction pour les points du plan X,Y
Z_g = g_ab(XX_g, YY_g)
Z_h = h(XX_h, YY_h)

# Plot la surface.
ax_g.plot_surface(XX_g, YY_g, Z_g, cmap=cm.coolwarm, alpha=0.4)
ax_h.plot_surface(XX_h, YY_h, Z_h, cmap=cm.coolwarm, alpha=0.4)
# Lignes de Champ
# lignes projetées
ax_g.contour(XX_g, YY_g, Z_g, 20, offset=0, zdir='z', cmap=cm.coolwarm)  # 20 = nombre de lignes de champs
ax_h.contour(XX_h, YY_h, Z_h, 20, offset=-1, zdir='z', cmap=cm.coolwarm)  # 20 = nombre de lignes de champs
# lignes flotantes
ax_g.contour(XX_g, YY_g, Z_g, 20, zdir='z', cmap=cm.coolwarm)  # 20 = nombre de lignes de champs
ax_h.contour(XX_h, YY_h, Z_h, 20, zdir='z', cmap=cm.coolwarm)  # 20 = nombre de lignes de champs

fig_g.suptitle("Graph de $g_{2,2/7}(x,y)$")
ax_g.set_xlabel("x")
ax_g.set_ylabel('y')
ax_g.set_zlabel('z')
ax_g.set_xlim(xlim_g[0], xlim_g[1])
ax_g.set_ylim(ylim_g[0], ylim_g[1])

fig_h.suptitle("Graph de $h(x,y)$")
ax_h.set_xlabel("x")
ax_h.set_ylabel('y')
ax_h.set_zlabel('z')
ax_h.set_xlim(xlim_h[0], xlim_h[1])
ax_h.set_ylim(ylim_h[0], ylim_h[1])

fig_g.savefig('./outC/Question1-2g.png')
fig_h.savefig('./outC/Question1-2h.png')


# endregion question1-2


# region question 3
def grad_g_ab(x, y):
	global a, b
	return 2 * x / a, 2 * y / b


def grad_h(x, y):
	return -np.sin(x) * np.sin(y), np.cos(x) * np.cos(y)


def norme(V):
	somme_quad = 0
	for xi in V:
		somme_quad += xi ** 2
	return somme_quad ** 0.5


# endregion question 3
print("norme", norme(grad_h(1, 1)))

# region question 4
P0 = (0, 0)
P1 = (1, 0)
P2 = (0, -1)
P3 = (1, 1)
P = [P0, P1, P2, P3]

string = ""
string += "Question 4" + '\n'
for p in P:
	string += "grad_g_ab" + str(p) + " = " + str(grad_g_ab(p[0], p[1])) + '\n'
	string += "grad_h" + str(p) + " = " + str(grad_h(p[0], p[1])) + '\n'

file = open('./outC/Question4.txt', 'w')
file.write(string)
file.close()


# endregion question 4


# region question 5

def grad_pc(eps, m, u, xo, yo, df):
	n = 0
	X = [xo]
	Y = [yo]
	while norme(df(xo, yo)) > eps and n < m:
		df1, df2 = df(xo, yo)
		xo += df1 * u
		yo += df2 * u
		n += 1
		X.append(xo)
		Y.append(yo)
	return n, np.array(X), np.array(Y)

# endregion question 5


# region question 6
ax_g.cla()
ax_h.cla()

xlim_g = (-4, 4)
ylim_g = (-4, 4)

xlim_h = (4.7, 8)
ylim_h = (0, 3.141592)

# creation des donees.
X_g = np.arange(xlim_g[0], xlim_g[1], 0.25)
Y_g = np.arange(ylim_g[0], ylim_g[1], 0.25)

X_h = np.arange(xlim_h[0], xlim_h[1], 0.25)
Y_h = np.arange(ylim_h[0], ylim_h[1], 0.25)

XX_g, YY_g = np.meshgrid(X_g, Y_g)
XX_h, YY_h = np.meshgrid(X_h, Y_h)

a, b = 2, 2 / 7

Z_g = g_ab(XX_g, YY_g)
Z_h = h(XX_h, YY_h)

# Lignes de Champ
ax_g.contour(XX_g, YY_g, Z_g, 30, zdir='z', cmap=cm.coolwarm)  # 30 = nombre de lignes de champs
ax_g.plot_surface(XX_g, YY_g, Z_g, cmap=cm.coolwarm, alpha=0.4)

ax_h.contour(XX_h, YY_h, Z_h, 25, zdir='z', cmap=cm.coolwarm)  # 25 = nombre de lignes de champs
ax_h.plot_surface(XX_h, YY_h, Z_h, cmap=cm.coolwarm, alpha=0.4)

fig_g.suptitle("Graph de $g_{2,2/7}(x,y)$")
ax_g.set_xlabel("x")
ax_g.set_ylabel('y')
ax_g.set_zlabel('z')
ax_g.set_xlim(xlim_g[0], xlim_g[1])
ax_g.set_ylim(ylim_g[0], ylim_g[1])

fig_h.suptitle("Graph de $h(x,y)$")
ax_h.set_xlabel("x")
ax_h.set_ylabel('y')
ax_h.set_zlabel('z')
ax_h.set_xlim(xlim_h[0], xlim_h[1])
ax_h.set_ylim(ylim_h[0], ylim_h[1])

Pg = (0, 0)
n_g, X, Y = grad_pc(0.1, 100, 0.1, Pg[0], Pg[1], grad_g_ab)
Z = g_ab(X, Y)
ax_g.scatter(X, Y, Z, color='black', linewidth=3, label="n=" + str(n_g))
fig_g.legend()

Ph = (7, 1.5)
n_h, X, Y = grad_pc(0.1, 100, 0.1, Ph[0], Ph[1], grad_h)
Z = h(X, Y)
fig_h.legend()

for i in range(len(Z)):
	ax_h.plot(X[:i], Y[:i], Z[:i], color='black', linewidth=3, label="n=" + str(n_h))
	fig_h.savefig('./outC/Q6h'+str(i)+'.png')

fig_g.savefig('./outC/Q6g.png')
file = open('./outC/Question6.txt', 'w')
file.write("Pour h on remarque que la methode gradient pas constant converge vers le sommet assez rapidement (n=" + str(
	n_h) + ") comme prevu \n"
		   "Cependant pour g_ab puisque le point de depart est (0,0) la methode s'arrete instantanement (n=" + str(
	n_g) + ") alors que le point n'est pas au 'sommet'\n"
		   "C'est normal, il s'agit d'un point d'equilibre instable grad_g_ab(0,0)=0,0")
file.close()
# endregion question 6


# region question 7
fig_q7 = plt.figure(3)
ax_q7 = fig_q7.gca()

ecarts = []
a, b = 1, 20
eps = 10 ** -5
m = 120
# On part su point suivant
xo, yo = (-4, 4)

U = np.linspace(-0.99, -0.001, 100)
for u in U:
	_, X, Y = grad_pc(eps, m, u, xo, yo, grad_g_ab)
	Z = g_ab(X, Y)
	ecarts.append(((X[-1] - 0) ** 2 + (Y[-1] - 0) ** 2) ** 0.5)

ax_q7.plot(U, ecarts)
ax_q7.grid()
fig_q7.suptitle("Ecarts en fonction de u")
fig_q7.savefig('./outC/Q7.png')
file = open('./outC/Question7.txt', 'w')
file.write("Interpretation : \n"
		   "Un pas trop faible implique que l'on peut ne pas forcement arriver à la solution avant les 120 iterations \n"
		   "Avec un pas trop grand on 'jongle' autour de la solution sans jamais sans rapprocher suffisament \n"
		   )
file.close()


# endregion question 7


# region question 8

def gradamax(eps, m, u, xo, yo, f, df):
	n = 0
	x, y = xo, yo
	while n < m and norme(df(x, y)) > eps:
		k = 1
		dfx, dfy = df(x, y)
		F1 = f(x + k * u * dfx, y + k * u * dfy)
		F2 = f(x + (k + 1) * u * dfx, y + (k + 1) * u * dfy)
		while F2 >= F1 and k < m:
			F1 = f(x + k * u * dfx, y + k * u * dfy)
			F2 = f(x + (k + 1) * u * dfx, y + (k + 1) * u * dfy)
			k += 1
		x += k * u * dfx
		y += k * u * dfy
		n += 1
	return n, x, y


def gradamin(eps, m, u, xo, yo, f, df):
	n = 0
	x, y = xo, yo
	while n < m and norme(df(x, y)) > eps:
		k = 1
		dfx, dfy = df(x, y)
		F1 = f(x - k * u * dfx, y - k * u * dfy)
		F2 = f(x - (k + 1) * u * dfx, y - (k + 1) * u * dfy)
		while F2 <= F1 and k < m:
			F1 = f(x - k * u * dfx, y - k * u * dfy)
			F2 = f(x - (k + 1) * u * dfx, y - (k + 1) * u * dfy)
			k += 1
		x = x - k * u * dfx
		y = y - k * u * dfy
		n += 1
	return n, x, y


file = open('./outC/Question8.txt', 'w')
file.write(
	"gradamax(0.1, 50, 0.1, 1, 0, g_ab, grad_g_ab) = " + str(gradamax(0.1, 50, 0.1, 1, 0, g_ab, grad_g_ab)) + "\n")
file.write("gradamax(0.1, 50, 0.1, 0, 0, h, grad_h) = " + str(gradamax(0.1, 50, 0.1, 0, 0, h, grad_h)) + "\n")

file.write(
	"gradamin(0.001, 100, 0.01, 1, 5, g_ab, grad_g_ab) = " + str(
		gradamin(0.001, 100, 0.01, 1, 5, g_ab, grad_g_ab)) + "\n")
file.write(
	"gradamin(0.001, 100, 0.01, 0, 0, h, grad_h) = " + str(gradamin(0.001, 100, 0.01, 0, 0, h, grad_h)) + "\n")
file.close()
# endregion question 8


# region Question 9
a, b = 1, 20
xo, yo = -4, 4  # on part du point suivant

U = np.linspace(-0.999, 0.001, 100)
eps = 10 ** -5
ecarts_grada = []
ecarts_gradpc = []
n_max = 1000

for u in U:
	ecarts_grada.append(gradamin(eps, n_max, -u, xo, yo, g_ab, grad_g_ab)[0])
	ecarts_gradpc.append(grad_pc(eps, n_max, u, xo, yo, grad_g_ab)[0])
print('index',U[ecarts_grada.index(min(ecarts_grada))])
fig_q9 = plt.figure()
ax_q9 = fig_q9.gca()

ax_q9.plot(U, ecarts_gradpc, label="Ecarts grad_pc")
ax_q9.plot(U, ecarts_grada, label="Ecarts grada")
fig_q9.suptitle("Nombre d'itérations en fonction de u")
ax_q9.grid()
ax_q9.set_xlabel('u')
ax_q9.set_ylabel('n')
fig_q9.legend()
fig_q9.savefig("./outC/Q9.png")
ax_q9.set_yscale('log')
fig_q9.savefig('./outC/Q9bis.png')

# endregion Question 9
