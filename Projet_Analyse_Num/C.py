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
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
a, b = 2, 2 / 7
Z = np.sqrt(X ** 2 / a + Y ** 2 / b)
Zp = np.cos(X) * np.sin(Y)

# Plot la surface.
surf1 = ax1.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.9)
surf2 = ax2.plot_surface(X, Y, Zp, cmap=cm.coolwarm, alpha=0.9)


#Lignes de Champ
ax1.contour(X, Y, Z,20,offset=0,zdir='z',cmap=cm.coolwarm)
ax2.contour(X, Y, Zp,20,offset=-1,zdir='z',cmap=cm.coolwarm)


plt.show()
