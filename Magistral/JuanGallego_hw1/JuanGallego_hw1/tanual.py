import matplotlib.pyplot as plt
import numpy as np
import csv, operator


data = np.loadtxt("tAnual.txt")
es = np.loadtxt("est.txt")

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
popo=[]
j=[]
k=[]
l=[]
m=[]
n=[]
o=[]
p=[]
q=[]
r=[]
s=[]
t=[]
u=[]
v=[]
x=[]
y=[]
z=[]
aa=[]
bb=[]
cc=[]
dd=[]
ee=[]
ff=[]
gg=[]
hh=[]
ii=[]
jj=[]
kk=[]
ll=[]
mm=[]
nn=[]
oo=[]
pp=[]
qq=[]
rr=[]
ss=[]
tt=[]
uu=[]
vv=[]
ww=[]
xx=[]
yy=[]
zz=[]
y1=[]
x2=[]
y2=[]
x3=[]
y3=[]
x4=[]
y4=[]
x5=[]
y5=[]
x6=[]
y6=[]
x7=[]
y7=[]
x8=[]
y8=[]
x9=[]
y9=[]
x10=[]
y10=[]
x11=[]
y11=[]
x12=[]
y12=[]	
for i in range(0,1205):
	if(data[i,0]==es[0]):	
		a.append(data[i,1])
		b.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[1]):	
		c.append(data[i,1])
		d.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[2]):	
		e.append(data[i,1])
		f.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[3]):	
		g.append(data[i,1])
		h.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[4]):	
		popo.append(data[i,1])
		j.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[5]):	
		k.append(data[i,1])
		l.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[6]):	
		m.append(data[i,1])
		n.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[7]):	
		o.append(data[i,1])
		p.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[8]):	
		q.append(data[i,1])
		r.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[9]):	
		s.append(data[i,1])
		t.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[10]):	
		u.append(data[i,1])
		v.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[11]):	
		x.append(data[i,1])
		y.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[12]):	
		z.append(data[i,1])
		aa.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[13]):	
		bb.append(data[i,1])
		cc.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		dd.append(data[i,1])
		ee.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		ff.append(data[i,1])
		gg.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		hh.append(data[i,1])
		ii.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		jj.append(data[i,1])
		kk.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		ll.append(data[i,1])
		mm.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		nn.append(data[i,1])
		oo.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		pp.append(data[i,1])
		qq.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		rr.append(data[i,1])
		ss.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		tt.append(data[i,1])
		uu.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		xx.append(data[i,1])
		yy.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		zz.append(data[i,1])
		y1.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		x2.append(data[i,1])
		y2.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		x3.append(data[i,1])
		y3.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		x4.append(data[i,1])
		y4.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		x5.append(data[i,1])
		y5.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		x6.append(data[i,1])
		y6.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		x7.append(data[i,1])
		y7.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		x8.append(data[i,1])
		y8.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		x9.append(data[i,1])
		y9.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		x10.append(data[i,1])
		y10.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		x11.append(data[i,1])
		y11.append(data[i,2])
for i in range(0,1205):
	if(data[i,0]==es[14]):	
		x12.append(data[i,1])
		y12.append(data[i,2])


plt.plot(a,b, label = es[0])
plt.plot(c,d, label = es[1])
plt.plot(c,d, label = es[1])
plt.plot(e,f, label = es[2])
plt.plot(g,h, label = es[3])
plt.plot(popo,j, label = es[4])
plt.plot(k,l, label = es[5])
plt.plot(m,n, label = es[6])
plt.plot(o,p, label = es[7])
plt.plot(q,r, label = es[8])
plt.plot(s,t, label = es[9])
plt.plot(u,v, label = es[10])
plt.plot(x,y, label = es[11])
plt.plot(z,aa, label = es[12])
plt.plot(bb,cc, label = es[13])
plt.plot(dd,ee, label = es[14])
plt.plot(ff,gg, label = es[15])
plt.plot(hh,ii, label = es[16])
plt.plot(jj,kk, label = es[17])
plt.plot(ll,mm, label = es[18])
plt.plot(nn,oo, label = es[19])
plt.plot(pp,qq, label = es[21])
plt.plot(rr,ss, label = es[22])
plt.plot(tt,uu, label = es[23])
plt.plot(xx,yy, label = es[24])
plt.plot(zz,y1, label = es[25])
plt.plot(x2,y2, label = es[26])
plt.plot(x3,y3, label = es[27])
plt.plot(x4,y4, label = es[28])
plt.plot(x5,y5, label = es[29])
plt.plot(x6,y6, label = es[30])
plt.plot(x7,y7, label = es[31])
plt.plot(x8,y8, label = es[32])
plt.plot(x9,y9, label = es[33])
plt.plot(x10,y10, label = es[34])
plt.plot(x11,y11, label = es[35])
plt.plot(x12,y12, label = es[20])
plt.legend(fontsize=12, loc=0, title="Estacion")
plt.title("Temperatura vs Year", fontsize=16, fontweight='bold')
plt.xlabel("Year")
plt.ylabel("Temperatura(C)")
plt.show()


