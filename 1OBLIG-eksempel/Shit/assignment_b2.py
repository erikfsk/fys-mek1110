from matplotlib import pyplot as plt
from numpy import *

def retning(x,y):
	return x*y,y

x = linspace(-6.5,6.5,40)

ax = plt.subplot(111)
# Plot scatter of points
for C in [-5,-1,0,1,5,10,17]:
	y_list = []
	for x_i in x:
		y_i = (x_i**2 - C)/2.0
		y_list.append(y_i)
		x_retning,y_retning = retning(x_i,y_i)
		ax.quiver(x_i,y_i,(x_i+x_retning),(y_i+y_retning),color="k")
	ax.plot(x,y_list,label="C = "+str(C),linewidth=2)
plt.xlim(-8,7)
plt.ylim(-10,10)
plt.xlabel("test",fontsize=20)
plt.ylabel("test",fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid("on")
plt.tight_layout()
plt.legend(loc="best")
plt.savefig("2b.png" ,bbox_inches="tight")
plt.show()

