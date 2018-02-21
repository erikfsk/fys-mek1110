import matplotlib.pyplot as plt
from numpy import *

t = linspace(0,10,100)

def acc(t,a=5):
    return a

def fart(t,a=5):
    return a*t

def pos(t,a=5):
    return (a/2.)*t*t


func = [pos,fart]
ylabel = ["Position [m]","Velocity [m/s]"]

for i in range(1,3):
    plt.plot(t,func[i-1](t,1),linewidth=2,label="Isak")
    plt.plot(t,func[i-1](t,3),linewidth=2,label="Mari")
    plt.plot(t,func[i-1](t),linewidth=2,label="Erik")
    plt.xlabel("Time [s]",fontsize=20)
    plt.ylabel(ylabel[i-1],fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlim(0,10)
    plt.grid("on")
    plt.tight_layout()
    plt.legend(loc="best",fontsize=20)
    plt.savefig("advanced"+str(i)+".pdf" ,bbox_inches="tight")
    plt.clf()
    plt.plot(t,func[i-1](t),label="Erik")
    plt.plot(t,func[i-1](t,1),label="Isak")
    plt.plot(t,func[i-1](t,3),label="Mari")
    plt.legend()
    plt.savefig("standard"+str(i)+".pdf")
    plt.clf()
