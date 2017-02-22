import matplotlib.pyplot as plt
import numpy as np

cad = input("Ingrese el nombre de la estacion: ")
data=np.loadtxt("tempvstiempo.txt")
a= 0 
b=  0
c=  0
d=  0
e=  0
h=  0
i=  0
j=  0
k=  0
l=  0
m=  0
n=  0


for i in range(0,1205):
	if(data[i,0]==data):
		a= en + data[i,2]
		b = fb + data[i,3]
		d =d+ data[i,4]
		e=e  +data[i,5]
		f=f + data[i,6]
		g =g +data[i,7]
		h =h +data[i,8]
		i =i +data[i,9]
		j =j +data[i,10]
		k = k  +data[i,11]
		m = m +data[i,12]
		n =n +data[i,13]
l=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Dicimbre']		
f=[a/12,b/12,c/12,d/12,e/12,f/12,g/12,h/12,i/12,j/12,k/12,l/12,m/12,n/12]

plt.plot(l,f, label = es[20])
plt.title("patrones de temperatura", fontsize=16, fontweight='bold')
plt.xlabel("Mes")
plt.ylabel("Temperatura(C)")
plt.show()
