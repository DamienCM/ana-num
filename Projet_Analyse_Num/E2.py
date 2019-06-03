
import numpy as np
N=10
L=1
dx=L/(N+1)
fo=500
fn=350
eps=0.0001
c=10
A=(2+c*dx**2)*np.eye(N+1)
u=-np.ones(N)
U=np.diag(u,1)
V=np.diag(u,-1)
A=A+V+U
A=A*(1/(dx**2))
b=[]
f=3000
for t in range(1,N+1):
  if(t==1):
    b=np.array([b,(fo/(dx**2))+f])
  elif(t==N):
    b=np.array([b,(fn/(dx**2))+f])
  else:
    b=np.array([b,f])

yo=np.zeros(N)
m=100

yk=np.zeros(N)
i=0
ord=[]

def norme(M):
    return np.linalg.norm(M)

def nozero(M):
    taille = M.shape[0]
    for i in range(taille):
        for j in range(taille):
            if M[i][j] == 0:
                return False
    return True

def gradopt(A,b,y0,eps,m):
    n = 0
    g = 2*(A*y0-b)
    ro=(norme(g)**2)/(2*g.T*A*g)
    y1 = y0 - ro*g
    while(n<m and norme(y1-y0)>=eps):
        y0=y1
        g=2*(A*y0-b)
        if(nozero(g)):
            ro = ro=(norme(g)**2)/(2*g.T*A*g)
        else:
            ro=0
        y1=y0-ro*g
        n = n + 1
    return y1
yy=gradopt(A,b,yo,eps,m)
print(yy)