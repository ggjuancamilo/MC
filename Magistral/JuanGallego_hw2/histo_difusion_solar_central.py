#importa librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
import sys
 
#cantidad de particulas desplazandose
n=int(sys.argv[1])

#Radio del sol
rs= 10**5


#genera posicion incial para cada particula en (0,0,0) he inicializo un array con la cantidad de pasos de cada particula
xx=[]
yy=[]
zz=[]
pas=[]
dis=0
for i in range (n):
    xx.append(0.)
    yy.append(0.)
    zz.append(0.)
    pas.append(0)


#Mueve cada particula hasta que salga del sol contando los pasos
for i in range(n):
    while(dis<=rs):
    
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
print pas    


#genero Histograna
plt.hist(pas,20,(0,max(pas)))
ax = plt.axes()
ax.set_xlabel("$pasos$",fontsize=20)
ax.set_ylabel("$cantidad de particulas$",fontsize=20)
ax.set_title("$\mathrm{Pasos\ para\ salir\ vs\ particulas}$", fontsize=20)
filename = 'histo_difusion_solar_central_'
f2 = str(sys.argv[1])
plt.savefig(filename + f2 + '.pdf',format = 'pdf', transparent=True)



# In[ ]:



