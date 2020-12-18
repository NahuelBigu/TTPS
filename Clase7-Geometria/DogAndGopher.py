import math
from sys import stdin,stdout

#Accepted

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distancia_entre (self,point):
        return math.sqrt((point.x - self.x) * (point.x - self.x) + (point.y - self.y) * (point.y - self.y)) 


primeravez=True

while True:
    if primeravez:
        primeravez=False
    else:
        line=stdin.readline()
        if(not line): 
            break
    n,xG,yG,xD,yD=[x for x in stdin.readline().strip().split(' ')]
    n=int(n)
    gopher= Point(float(xG),float(yG))
    dog= Point(float(xD),float(yD))
    escape=False
    for _ in range(n):
        x,y=[float(x) for x in stdin.readline().strip().split(' ')]
        if(not escape):
            point= Point(x,y)
            if (point.distancia_entre(gopher) <= (point.distancia_entre(dog)/2)):
                escape=True
                stdout.write("The gopher can escape through the hole at ("+"{:.3f},{:.3f}".format(point.x,point.y)+").\n")
    if (not escape):
        stdout.write("The gopher cannot escape.\n")
  
  

    