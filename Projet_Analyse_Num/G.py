import numpy as np
import matplotlib.pyplot as plt


# Region Etude du minimum d'une fonction reele a une seule variable

def f(x):
	return x ** 3 - 3 * x ** 2 + 2 * x + 5


def fp(x):
	return 3 * x ** 2 - 6 * x + 2


# endregion etude du minimum d'une foction reeele a une seule variable
limites = (0, 3)
eps = 10 ** -5
nmax = 10 ** 6


def methodeDichotomie(limites, eps, m, f, df):
	a, b = limites
	c = (a + b) / 2
	n = 0
	err = max(abs(f(a) - f(b)), abs(f(c) - f(b)))
	while n < m and err > eps:
		c = (a + b) / 2
		if df(c) < 0:
			a = c
		else:
			b = c

		err = max(abs(f(a) - f(c)), abs(f(c) - f(b)))
		n += 1
	return n,c


def gradient_1D(xo, m, eps, dt=10 ** -6):
	err=abs(f(xo)-f(xo+dt*fp(xo)))
	n=0
	while n < m and err > eps:
		xo = xo + dt * fp(xo)
		n+=1
		err = abs(f(xo) - f(xo + dt * fp(xo)))
	return n,xo

print(methodeDichotomie(limites,eps,10**6,f,fp))
