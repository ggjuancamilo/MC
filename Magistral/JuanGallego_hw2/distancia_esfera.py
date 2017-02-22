#importa librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
import sys

#permite al usuario ingresar los valores de las latitudes y longitudes
l=int(sys.argv[1])
lo=int(sys.argv[2])
l1=int(sys.argv[3])
lo1=int(sys.argv[4])

#radio de la tierra
r=6371

#Pasa los valores ingresados a coordenadas cartesianas
x=np.sin((np.pi/180)*l)*np.cos((np.pi/180)*lo)
y=np.sin((np.pi/180)*l)*np.sin((np.pi/180)*lo)
z=np.cos((np.pi/180)*l)
A=[x,y,z]#vector coordenada ciudad A


x1=np.sin((np.pi/180)*l1)*np.cos((np.pi/180)*lo1)
y1=np.sin((np.pi/180)*l1)*np.sin((np.pi/180)*lo1)
z1=np.cos((np.pi/180)*l1)
B=[x1,y1,z1]#vector coordenada ciudad B

#calculo distacia entre las dos ciudades mediante el algoritmo Dist=r*<A,B>/abs(A)*abs(B)
d=np.arccos(np.dot(A,B)/(np.linalg.norm(A)*np.linalg.norm(B)))*r
print d
