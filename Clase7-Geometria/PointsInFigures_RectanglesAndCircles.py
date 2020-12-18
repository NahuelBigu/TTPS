import math
from sys import stdin,stdout
#Points in Figures: Rectangles and Circles UVA - 477 

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




figuras=[]
line=stdin.readline().strip()

while line != '*':
    line=line.split(' ')
    if (line[0] == "c"):
        figuras.append(Circles(float(line[1]),float(line[2]),float(line[3])))
    else:
        figuras.append(Rectangle(float(line[1]),float(line[2]),float(line[3]),float(line[4])))
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
