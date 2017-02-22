import matplotlib.pyplot as plt
import numpy as np
l = input("Ingrese la longitud de la varilla: ")


x=np.linspace(0,l/2,1000)
y=np.sqrt(-(2*x)**2+l**2)/2
plt.plot(x,y, label = "Pos. Centro de masa")
plt.legend()
plt.title("Posicion centro de masa varrilla", fontsize=16, fontweight='bold')
plt.xlabel("m")
plt.ylabel("m")
plt.show()
quit()
