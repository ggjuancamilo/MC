import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("tempvsalt.txt")

plt.scatter(data[:,2],data[:,3])
plt.title("Temperatura vs Altura", fontsize=18, fontweight='bold')
plt.xlabel("Altura(m)")
plt.ylabel("Temperatura(C)")
plt.show()
