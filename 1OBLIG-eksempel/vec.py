#filename: vec.py
from matplotlib import pyplot as plt
from numpy import *
from velfield import *

for i in [5,30]:
	x,y,u,v = velfield(i)
	ax = plt.subplot(111)
	ax.quiver(x,y,u,v,color="r")
	plt.xlabel("x [m]",fontsize=20)
	plt.ylabel("y [m]",fontsize=20)
	plt.xticks(fontsize=20)
	plt.yticks(fontsize=20)
	plt.grid("on")
	plt.tight_layout()
	plt.savefig("4b"+str(i)+".png" ,bbox_inches="tight")
	plt.show()