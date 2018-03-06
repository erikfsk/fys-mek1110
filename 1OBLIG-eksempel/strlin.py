#filename: strlin.py
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from streamfun import *


for func in [0,1,2]:
	for pi_factor in [0.5,5]:
		for n in [5,30,300]:
			plt.figure()
			X,Y,Z = streamfun(n,func,pi_factor)
			CS = plt.contour(X, Y, Z)
			plt.clabel(CS, inline=1, fontsize=20)
			plt.xlabel("x [m]",fontsize=20)
			plt.ylabel("y [m]",fontsize=20)
			plt.xticks(fontsize=20)
			plt.yticks(fontsize=20)
			plt.grid("on")
			plt.tight_layout()
			plt.savefig("4a_"+str(func)+"_"+str(pi_factor).replace(".",",")+\
						"_"+str(n)+".png" ,bbox_inches="tight")
			plt.clf()