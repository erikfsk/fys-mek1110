# filename: assignment_c1.py
from matplotlib.pyplot import *
from numpy import *

def a1(t,theta = 0.2*pi,v0 = 1):
    x = v0*t*cos(theta)
    y = v0*t*sin(theta) - 0.5 * g*t**2

    #dimensjonslost
    x = x/(2*v0*v0*sin(theta)*cos(theta)/g)
    y = y/(2*v0*v0*sin(theta)*cos(theta)/g)#(0.5*(v0**2)*(sin(theta)**2)/g)
    return x,y


def lag_plot(x,y,label_text,xlabel_text="x$^*$(t) [$x_m$]",\
            ylabel_text="y$^*$(t) [$x_m$]",figfile="test.png"):
    plot(x,y,linewidth=2,label=label_text)
    xlabel(xlabel_text,fontsize=20)
    ylabel(ylabel_text,fontsize=20)
    xticks(fontsize=20)
    yticks(fontsize=20)
    xlim(min(x),max(x)+0.2)
    grid("on")


v0 = 1;     g = 1;     i = 1
for theta in [0.125*pi,0.25*pi,0.375*pi]:
    time = linspace(0,2*v0/g*sin(theta),1000)
    x,y = a1(time,theta,v0)
    lag_plot(x,y,"$\\theta = %.3f\pi$" % (0.125*i),figfile="1a.png")
    i += 1
tight_layout()
legend(loc="best",fontsize=20)
savefig("1a.png" ,bbox_inches="tight")
clf()
