#filename: assignment_b2.py
from matplotlib import pyplot as plt
from numpy import *

def retning(x,y):
	return x*y,y

def y_er_lik(x_verdi,C_verdi):
	return log(abs(x_verdi)) + C_verdi


x = linspace(-6.5,6.5,1000)

ax = plt.subplot(111)
for C in [0,5,10]:
	y_list = []
	vx_list = []
	vy_list = []
	for x_i in x:
		y_i = y_er_lik(x_i,C)
		y_list.append(y_i)
		vx_retning,vy_retning = retning(x_i,y_i)
		vx_list.append(vx_retning)
		vy_list.append(vy_retning)
		if abs(vx_retning) < 0.01+0.02*C and abs(vy_retning) < 0.01+0.02*C:
			ax.plot(x_i,y_i,"ko")
	ax.quiver(x[::100],y_list[::100],vx_list[::100],vy_list[::100],color="c")
	ax.plot(x,y_list,label="C = "+str(C),linewidth=2)
plt.xlim(-6,6)
plt.xlabel("x [m]",fontsize=20)
plt.ylabel("y [m]",fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid("on")
plt.tight_layout()
plt.legend(loc="best")
plt.savefig("2b.png" ,bbox_inches="tight")
plt.show()

