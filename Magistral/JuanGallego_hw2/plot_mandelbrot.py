#importa librerias necesarias
import numpy as np
import sys
import matplotlib.pyplot as plt

#numero maximo de iteraciones por pixel
n=int(sys.argv[1])

#Genera malla, y los ejes coordenados
Man = np.zeros((1024,1024))
Y=np.linspace(-2,1,1024)
X=np.linspace(-1.5,1.5,1024)

#determina si un pixel pertenece o no al conjunto de Mandelbrot
for i in range(1024):
    for j in range(1024):
        c= Y[i]+1.j*X[j]
        z=c
        for k in range(n):
            z=z**2+c
            if ((np.conjugate(z)*z)>4):#decide si el pixel puede o no portenecer antes de iterar n veces
                break
	
        if ((np.conjugate(z)*z)<4):
            Man[j,i]=1
    print i

#genera pdf del set de Mandelbrot
plt.imshow(Man)
ax = plt.axes()
ax.set_xlabel("$x$",fontsize=20)
ax.set_ylabel("$y$",fontsize=20)
ax.set_title("$\mathrm{Mandelbrot\ set}$", fontsize=20)
filename = 'Mandelbrot_'
f2 = str(sys.argv[1])
plt.savefig(filename + f2 + '.pdf',format = 'pdf', transparent=True)

