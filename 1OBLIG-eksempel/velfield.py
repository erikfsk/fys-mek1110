#filename: velfield.py
from numpy import *

def velfield(n=20):
    x=linspace(-0.5*pi,0.5*pi,n)
    [X,Y] = meshgrid(x,x)
    Vx,Vy = cos(X)*sin(Y),-sin(X)*cos(Y)
    return X, Y, Vx, Vy
