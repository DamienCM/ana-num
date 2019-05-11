import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x ** 3 - 3 * x ** 2 + 2 * x + 5


def balayage(a, b, N):
    X = np.linspace(a, b, N + 1)
    Y = f(X)
    return min(Y)


def aleatoire(a, b, N):
    X = np.random.rand(N + 1)
    X = (b - a) * X
    X = X + a
    Y = f(X)
    return min(Y)


N = 200
a, b = 0, 3
valeur_theorique = 5 - 2 / (3 * 3 ** 0.5)

X = np.arange(10, N, 1)
ecarts_balayage = []

for i in X:
    ecarts_balayage.append(abs(valeur_theorique - balayage(a, b, i)) / valeur_theorique)

ecarts_aleatoire = []
for i in X:
    ecarts_aleatoire.append(abs(valeur_theorique - aleatoire(a, b, i)) / valeur_theorique)

plt.plot(X, ecarts_aleatoire, label='Aleatoire')
plt.plot(X, ecarts_balayage, label='Balayage')
plt.grid()
plt.title("Ecarts relatif selon le nombre de points")
plt.xlabel('N')
plt.ylabel('$\epsilon$')
plt.legend()

plt.savefig("./outB/Ecarts.png")
plt.semilogx()

plt.savefig("./outB/Ecarts_semilogx.png")

valeur_approchee = balayage(a, b, N)
txt = "Methode par balayage régulier \nValeur approchée : " + str(valeur_approchee) + '\n' + "Valeur théorique : " + str(valeur_theorique)
txt += '\n' + 'Erreur Relative : ' + str(abs(valeur_approchee - valeur_theorique) / valeur_theorique)
txt += '\n' + 'Nombre de point : ' + str(N) + '\n'

text_file = open("./outB/question4.txt", "w")
text_file.write(txt)
text_file.close()

def fp(x):
    return 3 * x ** 2 - 6 * x + 2


def gradient_1D(xo, n, dt=10 ** -6):
    for i in range(n):
        xo = xo + dt * fp(xo)
    return f(xo)

valeur_approchee = gradient_1D(1.5,N)

txt = "\nMethode par Gradient 1D \nValeur approchée : " + str(valeur_approchee) + '\n' + "Valeur théorique : " + str(valeur_theorique)
txt += '\n' + 'Erreur Relative : ' + str(abs(valeur_approchee - valeur_theorique) / valeur_theorique)
txt += '\n' + 'Nombre de point : ' + str(N) + '\n'

text_file = open("./outB/question4.txt", "a")
text_file.write(txt)
text_file.close()



def phi(t,xn):
    return f(xn+t*fp(xn))

A=1+1