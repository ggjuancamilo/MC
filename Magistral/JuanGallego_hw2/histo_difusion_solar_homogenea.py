#importa librerias necesarias

import numpy as np
import matplotlib.pyplot as plt
import sys

#cantidad de particulas desplazandose
n=int(sys.argv[1])

#Radio del sol
rs= 10**5

#genera posicion incial para cada particula en un sitio aleatorio he inicializo un array con la cantidad de pasos de cada particula
xx=[]
yy=[]
zz=[]
pas=[]
pos=[]
dis=0
ri=np.random.uniform(0,100000,size=n)
for i in range (n):

    ph=np.random.random(1)*2*np.pi
    th=(np.random.random(1))*np.pi
    

    xx.append(np.cos(ph[0])*np.sin(th[0])*ri[i])
    yy.append(np.sin(ph[0])*np.sin(th[0])*ri[i])
    zz.append(np.cos(th[0])*ri[i])
    pas.append(0)
    dist=np.sqrt(xx[i]**2+yy[i]**2+zz[i]**2)



#Mueve cada particula hasta que salga del sol contando los pasos
for i in range(n):
    while(dis<=100000):
    
        ph=np.random.random(1)*2*np.pi
        th=(np.random.random(1))*np.pi
        x=np.cos(ph[0])*np.sin(th[0])*1000
        y=np.sin(ph[0])*np.sin(th[0])*1000
        z=np.cos(th[0])*1000
        xx[i]=xx[i]+x
        yy[i]=yy[i]+y
        zz[i]=zz[i]+z
        dis=np.sqrt(xx[i]**2+yy[i]**2+zz[i]**2)
        pas[i]=pas[i]+1
        
    dis=0
    

#genero histograma
plt.hist(pas,20,(0,max(pas)))
ax = plt.axes()
ax.set_xlabel("$pasos$",fontsize=20)
ax.set_ylabel("$cantidad de particulas$",fontsize=20)
ax.set_title("$\mathrm{Pasos\ para\ salir\ vs\ particulas}$", fontsize=20)
filename = 'histo_difusion_solar_homogenea_'
f2 = str(sys.argv[1])
plt.savefig(filename + f2 + '.pdf',format = 'pdf', transparent=True)




# In[ ]:



