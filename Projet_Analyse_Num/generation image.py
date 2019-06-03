import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

from matplotlib.animation import FFMpegWriter

def f(x):
	return 1 + (x - 1) ** 2


def fp(x):
	return 2 * (x - 1)


fig,ax = plt.subplots()

xlim = (-0.2, 3)

X = np.linspace(-0.2, 3, 1000)
Y = f(X)
plt.plot(X, Y,label="$y=(x-1)^2+1$")
plt.grid()
plt.xlim(xlim)
plt.ylim(-0.2, 3)
plt.title("Valeurs consecutives de $x_n$")
plt.legend()
u = -0.15
xo=0
for i in range(10):
	ax.quiver(xo,f(xo),u*fp(xo),0,scale=3)
	x1 = xo
	xo+=u*fp(xo)
	plt.plot([xo, xo], [f(x1),0],color="green")
	plt.savefig("./outFig/anim"+str(i)+'.png')
