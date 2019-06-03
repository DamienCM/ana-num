import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from matplotlib.animation import FFMpegWriter

# Region Etude du minimum d'une fonction reele a une seule variable

def f(x):
	return x ** 3 - 3 * x ** 2 + 2 * x + 5


def fp(x):
	return 3 * x ** 2 - 6 * x + 2


def norme(A, B):
	return ((A[0] - B[0]) ** 2 + (A[1] * B[1]) ** 2) ** 0.5


# endregion etude du minimum d'une foction reeele a une seule variable
limites = (1, 3)
eps = 10 ** -16
nmax = 10 ** 6


def dichotomie2D(limites, eps, m, f, df):
	a, b = limites
	c = (a + b) / 2
	n = 0
	err = max(abs(f(a) - f(c)), abs(f(c) - f(b)))
	while n < m and err > eps:
		c = (a + b) / 2
		if df(c) < 0:
			a = c
		else:
			b = c

		c = (a + b) / 2

		err = max(abs(f(a) - f(c)), abs(f(c) - f(b)))
		n += 1
	return n, c


def gradient_1D(xo, m, eps, dt=10 ** -4):
	err = abs(f(xo) - f(xo + dt * fp(xo)))
	n = 0
	while n < m and err > eps:
		xo = xo - dt * fp(xo)
		n += 1
		err = abs(f(xo) - f(xo + dt * fp(xo)))
	return n, xo


print(dichotomie2D(limites, eps, nmax, f, fp))
print(gradient_1D(limites[0], nmax, eps))


def dichotomie3D(P,ecart, m, f, grad_f):
	n = 0
	J = []
	#	err=10**10
	A=(P[0]-ecart,P[1]+ecart)
	B=(P[0]+ecart,P[1]+ecart)
	C=(P[0]+ecart,P[1]-ecart)
	D=(P[0]-ecart,P[1]-ecart)
	index_changement_equal_4 = (0, 0)
	while n < m:
		AB = ((A[0] + B[0]) / 2, B[1])
		BC = (B[0], (C[1] + B[1]) / 2)
		CD = ((C[0] + D[0]) / 2, D[1])
		DA = (A[0], (A[1] + D[1]) / 2)

		#		err = max([norme(I, p) for p in Points])
		I = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2)
		Points = [
			[A, AB, B],
			[DA, I, BC],
			[D, CD, C]
		]
		J.append(I)
		n += 1
		for i in range(2):
			for j in range(2):
				chgmnt = 0
				Points_cadran = [Points[i][j], Points[i][j + 1], Points[i + 1][j + 1], Points[i + 1][j]]
				grad_x, grad_y = grad_f(Points_cadran[0])
				for k in range(3):
					if grad_x * grad_f(Points_cadran[k + 1])[0] < 0:
						chgmnt += 1
					if grad_y * grad_f(Points_cadran[k + 1])[1] < 0:
						chgmnt += 1
				if chgmnt == 4:
					index_changement_equal_4 = (i, j)
		# print(chgmnt)
		A, B, C, D = Points[index_changement_equal_4[0]][index_changement_equal_4[1]], \
					 Points[index_changement_equal_4[0]][index_changement_equal_4[1] + 1], \
					 Points[index_changement_equal_4[0] + 1][index_changement_equal_4[1] + 1], \
					 Points[index_changement_equal_4[0] + 1][index_changement_equal_4[1]]
	return J


def f(x, y):
	return -(x - 2) ** 2 - (y - 1) ** 2 + 2


def grad_f(P):
	x, y = P
	return 4 - 2 * x, 2 - 2 * y


J = dichotomie3D((-2,3),5, 1000, f, grad_f)
plt.grid()
X = [p[0] for p in J]
Y = [p[1] for p in J]
plt.xlim(-3, 3)
plt.ylim(-3, 3)

A = np.linspace(-3, 3, 30)
B = np.linspace(-3, 3, 30)
AA, BB = np.meshgrid(A, B)
ZZ = f(AA, BB)
fig, ax = plt.subplots()
CS = ax.contourf(AA, BB, ZZ, levels=100, cmap="inferno")
CS = ax.contour(AA, BB, ZZ, levels=20, colors='black')


def animate(i):
	global X, Y, AA, BB, ZZ
	CS = ax.contourf(AA, BB, ZZ, levels=100, cmap="inferno")
	CS = ax.contour(AA, BB, ZZ, levels=20, linewidths=1, colors='black')
	line.set_data(X[:i+1], Y[:i+1])
	point.set_data(X[i],Y[i])

	return point,line,


line, = ax.plot((X[0], X[1]), (Y[0], Y[1]), color='red')
point,= ax.plot(X[0],Y[0],'ro',color='blue')
ani = FuncAnimation(
	fig, animate, interval=500, blit=True, frames=range(10), repeat=True)
plt.rcParams['animation.ffmpeg_path'] = '.\\ffmpeg\\bin\\ffmpeg.exe'

FFwriter = FFMpegWriter(fps=1)
ani.save('outF/animationDichotomie3D.mp4', writer = FFwriter)