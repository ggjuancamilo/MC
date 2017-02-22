import matplotlib.pyplot as plt
import numpy as np
import csv, operator


data = np.loadtxt("tAnual.txt")
es = np.loadtxt("est.txt")

aa=[]
bb=[]
xx=[]
yy=[]

for i in range (0,36):
    for j in range (0,1205):
        if(data[j,0] == es[i]):
            aa.append(data[j,1])
            bb.append(data[j,2])
xx.append(aa)
yy.append(bb)
#while len(aa)>0:
 #   aa.pop()  

       

bbb=0
counter = 0
for j in range(0,36):
    for i in range(0,50):
        if(aa[i-1+counter] < aa[i+counter]):
            plt.plot(aa[i+counter],bb[i+counter], label = es[j])
            plt.legend()
            plt.title("Temperatura vs Ano", fontsize=16, fontweight='bold')
            plt.xlabel("ano")
            plt.ylabel("temperatura")
           
            bbb = bbb+1
    counter = counter + bbb
    bbb=0
plt.show()
