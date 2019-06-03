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
eps = 0.000000001
nmax = 10 ** 6


def dichotomie1D(limites, eps, m, f, df):
	xlim=(-0.2,3)
	ylim=(-0.2,3)
	a, b = limites
	c = (a + b) / 2
	n = 0
	X=np.linspace(-0.2,3,1000)
	Y=f(X)
	err = max(abs(f(a) - f(c)), abs(f(c) - f(b)))
	while n < m and err > eps:
		c = (a + b) / 2

		fig, ax = plt.subplots()
		plt.gca()
		plt.gcf()
		ax.plot(X,Y,color='blue',label="$y = 3x^2 - 6x + 2$")
		plt.title("Evolution de $x_n$")

		ax.grid()
		fig.legend()
		plt.legend()

		m=max(f(a),f(b),f(c))
		ax.plot([a,a,b,b],[0,m,m,0],color='green')
		ax.plot([c,c],[0,m],color='red')
		plt.savefig("./outF/dicho1D"+str(n)+'.png')
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


print(dichotomie1D(limites, eps, nmax, f, fp))
print(gradient_1D(limites[0], nmax, eps))


def dichotomie3D(P,ecart, m, f, grad_f):
	n = 0
	J = []
	A=(P[0]-ecart,P[1]+ecart)
	B=(P[0]+ecart,P[1]+ecart)
	C=(P[0]+ecart,P[1]-ecart)
	D=(P[0]-ecart,P[1]-ecart)
	index_changement_equal_4 = (0, 0)
	plt.grid()
	X = [p[0] for p in J]
	Y = [p[1] for p in J]


	K = np.linspace(-7, 3, 30)
	L = np.linspace(-2, 8, 30)
	KK, LL = np.meshgrid(K, L)
	ZZ = f(KK, LL)
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

		plt.clf()
		plt.cla()
		fig, ax = plt.subplots()
		CS = ax.contourf(KK, LL, ZZ, levels=100, cmap="inferno")
		CS = ax.contour(KK, LL, ZZ, levels=20, linewidths=1, colors='black')
		plt.xlim(-7, 3)
		plt.ylim(-2, 8)
		plt.plot([A[0],B[0],C[0],D[0],A[0]],[A[1],B[1],C[1],D[1],A[1]],color='green')
		plt.plot([AB[0],CD[0]],[AB[1],CD[1]],color='green')
		plt.plot([DA[0],BC[0]],[DA[1],BC[1]],color='green')
		if len(J)>1:
			plt.scatter([J[-1][0]],[J[-1][1]],color='black')
			for h in range(len(J)-1):
				plt.plot([J[h][0],J[h+1][0]],[J[h][1],J[h+1][1]],color='blue')
		plt.scatter((2),(1),color='black',marker='+')
		fig.savefig('./outF/dicho3D'+str(n)+'.png')






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


J = dichotomie3D((-2,3),4.9, 10, f, grad_f) # point de epart, ecart initial, n, f,gra_f





