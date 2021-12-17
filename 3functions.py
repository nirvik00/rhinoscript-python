
import rhinoscriptsyntax as rs
import random


def loop(a, b, c, p):
    for i in range(0, a):
        for j in range(0, b):
            cir=[]
            for k in range(0, c):
                x=pt(i, j, k, p)
                cir.append(x)
            rs.AddLoftSrf(cir)

def pt(x,y,z, p):
    a=[x,y,z] 
    if p ==True:
        rs.AddPoint(a)
    else:
        c=rs.AddCircle(a, random.random()*0.25+0.1)
        return c


p=False

loop(5,3,5, p)