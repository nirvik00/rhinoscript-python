import rhinoscriptsyntax as rs
import random

def fun1(c):
    div = rs.DivideCurveLength(c, 5)
    # div = [p1, p2, p3,..., p10]
    
    for pt in div:
        rs.AddPoint(pt)
        x=pt[0]
        y=pt[1]
        z=pt[2]
        circs=[]
        for j in range(0, 10):
            pt2=[x,y,j]
            r=random.randint(2,3)
            c=rs.AddCircle(pt2, r)
            circs.append(c)
        rs.AddLoftSrf(circs)

C=rs.GetObjects("pick")

for c in C:
    fun1(c)
