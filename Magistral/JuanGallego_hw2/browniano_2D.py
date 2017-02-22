#importa librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
import sys

#numero de pasos
n=int(sys.argv[1])

xy=np.linspace(0,n,n+1)

#genero coordenadas iniciales
xx=0.
yy=0.
zz=0.


dist=[0.]#distancia desde el origen que llega a tener la particula

#mueve la particula n veces grabando su posicion en cada movimiento
for i in range (n):
    
    ph=np.random.random(1)*2*np.pi
    th=(np.random.random(1))*np.pi
    x=np.cos(ph[0])*np.sin(th[0])
    y=np.sin(ph[0])*np.sin(th[0])
    z=np.cos(th[0])
    xx=xx+x
    yy=yy+y
    zz=zz+z
    dis=np.sqrt(xx**2+yy**2+zz**2)
    dist.append(dis)
    

#genera la imagen
plt.plot(xy,dist)

ax = plt.axes()
ax.set_xlabel("$pasos$",fontsize=20)
ax.set_ylabel("$distancia$",fontsize=20)
ax.set_title("$\mathrm{Distancia\ vs\ Numero\ de\ pasos}$", fontsize=20)
filename = 'browniano_2d_'
f2 = str(sys.argv[1])
plt.savefig(filename + f2 + '.pdf',format = 'pdf', transparent=True)

