from matplotlib import pyplot as plt
from numpy import *

def retning(x,y):
	return cos(x)*sin(y),-sin(x)*cos(y)


ax = plt.subplot(111)
for x_i in linspace(-10,10,25):
	for y_i in linspace(-10,10,25):
		x_retning,y_retning = retning(x_i,y_i)
		length = sqrt((x_i+x_retning)**2 + (y_i+y_retning)**2)
		if x_i == 0:
			ax.quiver(x_i,y_i,(x_i+x_retning),(y_i+y_retning),color="r",scale=75)
		elif y_i == 0:
			ax.quiver(x_i,y_i,(x_i+x_retning),(y_i+y_retning),color="r",scale=75)

plt.xlabel("x [m]",fontsize=20)
plt.ylabel("y [m]",fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid("on")
plt.tight_layout()
plt.savefig("3c.png" ,bbox_inches="tight")
plt.show()
