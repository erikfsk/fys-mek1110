#filename: streamfun.py
from numpy import linspace, meshgrid, cos, pi

def streamfun(n=20,func=0,pi_factor=0.5):
    x=linspace(-pi_factor*pi,pi_factor*pi,n)
    [X,Y] = meshgrid(x,x)
    func_list = [cos(X)*cos(Y),(1-((1/2.)*X**2)-((1/2.)*Y**2)),\
    			cos(X)*cos(Y)-(1-((1/2.)*X**2)-((1/2.)*Y**2))]
    psi=func_list[func]
    return X, Y, psi