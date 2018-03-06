from matplotlib import pyplot as plt
from numpy import *

def retning(x,y):
	return x*y,y


ax = plt.subplot(111)
# Plot scatter of points
for x_i in linspace(-10,10,25):
	for y_i in linspace(-10,10,25):
		x_retning,y_retning = retning(x_i,y_i)
		length = sqrt(x_retning**2 + y_retning**2)
		if x_i > 0 and y_i > 0:
			ax.quiver(x_i,y_i,(x_i+x_retning)/length,(y_i+y_retning)/length,color="r",scale=30)
		elif x_i < 0 and y_i > 0:
			ax.quiver(x_i,y_i,(x_i+x_retning)/length,(y_i+y_retning)/length,color="r",scale=30)
		elif x_i > 0 and y_i < 0:
			ax.quiver(x_i,y_i,(x_i+x_retning)/length,(y_i+y_retning)/length,color="r",scale=30)
		elif x_i < 0 and y_i < 0:
			ax.quiver(x_i,y_i,(x_i+x_retning)/length,(y_i+y_retning)/length,color="r",scale=30)
		else:
			ax.quiver(x_i,y_i,(x_i+x_retning)/length,(y_i+y_retning)/length,color="r",scale=30)
		#ax.quiver(x_i,y_i,(x_i+x_retning),(y_i+y_retning),color="g",scale=100)
#ax.quiver(-10,0,10,0,scale=1,color="b")
#ax.quiver(0, 0, 1, 0,color="g",scale=2)#,length=1)
plt.xlabel("test",fontsize=20)
plt.ylabel("test",fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid("on")
plt.tight_layout()
plt.show()
#savefig("1a.png" ,bbox_inches="tight")
