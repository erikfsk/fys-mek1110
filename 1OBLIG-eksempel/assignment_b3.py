#filename: assignment_b3.py
from matplotlib import pyplot as plt
from numpy import *

def retning(x,y):
	return cos(x)*sin(y),-sin(x)*cos(y)

x_list = []
y_list = []
vx_list = []
vy_list = []
ax = plt.subplot(111)
for x_i in linspace(-3*pi,3*pi,37):
	for y_i in linspace(-3*pi,3*pi,37):
		if x_i == 0 or y_i == 0:
			vx_retning,vy_retning = retning(x_i,y_i)
			x_list.append(x_i)
			y_list.append(y_i)
			vx_list.append(vx_retning)
			vy_list.append(vy_retning)
ax.quiver(x_list,y_list,vx_list,vy_list,color="r")
plt.xlabel("x [m]",fontsize=20)
plt.ylabel("y [m]",fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid("on")
plt.tight_layout()
plt.savefig("3b.png" ,bbox_inches="tight")
plt.show()
