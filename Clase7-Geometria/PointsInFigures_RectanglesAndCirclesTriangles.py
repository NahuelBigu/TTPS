import math
from sys import stdin,stdout
#Points in Figures: Rectangles, Circles, Triangles UVA - 478 
#Accepted

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distancia_entre (self,point):
        return math.sqrt((point.x - self.x) * (point.x - self.x) + (point.y - self.y) * (point.y - self.y)) 

class Circles:
    def __init__(self,x,y,radius):
        self.center=Point(x,y)
        self.radius=radius

    def point_inside (self,p):
        return self.center.distancia_entre(p) < self.radius

class Rectangle:
    def __init__(self,xUpperLeft,yUpperLeft,xLowerRight,yLowerRight):  #Ojo recibe puntos de abajo der y arriba izq , este codigo invierte para tener arriba derecha  y abajo izq
        self.UpperRight=Point(xLowerRight,yUpperLeft)
        self.LowerLeft=Point(xUpperLeft,yLowerRight)
    
    def point_inside (self,p):
        return( (p.x > min(self.LowerLeft.x,self.UpperRight.x)) and (p.x < max(self.LowerLeft.x,self.UpperRight.x)) and (p.y > min(self.LowerLeft.y,self.UpperRight.y)) and (p.y < max(self.LowerLeft.y,self.UpperRight.y)) )

class Triangle:
    def __init__(self,xLowerLeft,yLowerLeft,xUpperCenter,yUpperCenter,xLowerRight,yLowerRight):
        self.LowerRight=Point(xLowerRight,yLowerRight)
        self.UpperCenter=Point(xUpperCenter,yUpperCenter)
        self.LowerLeft=Point(xLowerLeft,yLowerLeft)

    def sign (self,p1,p2,p3):
        return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)
           
    def point_inside (self,p):
        d1 = self.sign(p, self.LowerLeft, self.UpperCenter)
        d2 = self.sign(p, self.UpperCenter, self.LowerRight)
        d3 = self.sign(p, self.LowerRight, self.LowerLeft)

        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

        return not (has_neg and has_pos)


figuras=[]
line=stdin.readline().strip()

while line != '*':
    line=line.split(' ')
    if (line[0] == "c"):
        figuras.append(Circles(float(line[1]),float(line[2]),float(line[3])))
    elif (line[0] == "r"):
        figuras.append(Rectangle(float(line[1]),float(line[2]),float(line[3]),float(line[4])))
    else:
        figuras.append(Triangle(float(line[1]),float(line[2]),float(line[3]),float(line[4]),float(line[5]),float(line[6])))
    line=stdin.readline().strip()

count=1
line=stdin.readline().strip()
while(line!="9999.9 9999.9"):
    line=line.split(' ')
    p=Point(float(line[0]),float(line[1]))   
    find=False 
    for i,f in enumerate(figuras):
        if(f.point_inside(p)):
            find=True
            stdout.write("Point {} is contained in figure {}\n".format(count,i+1))
    if (not find):
        stdout.write("Point {} is not contained in any figure\n".format(count))
    count+=1
    line=stdin.readline().strip()
