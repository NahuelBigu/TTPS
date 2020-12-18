import math
from sys import stdin,stdout
EPSILON=1e-9
#Intersecting Lines UVA - 378 
#ACCEPTED

class Line:
    # Retorna una recta a partir de la forma ax + by + c =0
    def __init__(self, aValue, bValue, cValue):
        self.a = aValue
        self.b = bValue
        self.c = cValue   
    # Retorna una recta que pase entre dos puntos
    @staticmethod
    def lineByPoints(aPoint, bPoint):
        if aPoint.getX() == bPoint.getX(): # Es una recta vertical
            return Line(1, 0, (0 - aPoint.getX()))
        a = -(aPoint.getY() - bPoint.getY()) / (aPoint.getX() - bPoint.getX())
        c = -(a * aPoint.getX()) - (1* aPoint.getY())
        return Line(a, 1, c)

    def getA(self):
        return self.a
        
    def getB(self):
        return self.b

    def getC(self):
        return self.c

    # Retorna la pendiente de la recta
    def pendiente(self):
        return self.a / (-self.b)
    # Retorna la ordenada al origen de la recta
    def ordenada(self):
        return self.c / (-self.b)


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def point_in_box(self, lbPoint, rtPoint):
        return( (self.x >= min(lbPoint.getX(),rtPoint.getX())) and (self.x <= max(lbPoint.getX(),rtPoint.getX()))and (self.y >= min(lbPoint.getY(),rtPoint.getY())) and (self.y <= max(lbPoint.getY(),rtPoint.getY())) )

def PARALLEL(l1,l2):
    return (abs(l1.getA() - l2.getA()) <= EPSILON) and (abs(l1.getB() - l2.getB()) <= EPSILON)

def SAME_LINE(l1,l2):
    return PARALLEL(l1,l2) and (abs(l1.getC() - l2.getC()) <= EPSILON)
    
    
def INTERSECTION_LINE(l1,l2):
    ## CHECKEAR EL TEMA DE SI ES LA MISMA LINEA Y SI ES PARALELA ANTES.
    x = (l2.getB()*l1.getC() - l1.getB()*l2.getC()) / (l2.getA()*l1.getB() - l1.getA()*l2.getB())
    if (abs(l1.getB()) > EPSILON):
        y = - (l1.getA() * x + l1.getC()) / l1.getB()
    else:
        y = - (l2.getA() * x + l2.getC()) / l2.getB()
    return Point(x,y)

def line_intersect (l1,l2):
    if (SAME_LINE(l1,l2)):
        return "LINE" 
    if(PARALLEL(l1,l2)):
        return "NONE"
    p=INTERSECTION_LINE(l1,l2)
    return "POINT {:.2f} {:.2f}".format(p.getX(),p.getY())

cases = int(stdin.readline())
stdout.write("INTERSECTING LINES OUTPUT\n")
for _ in range(cases):
    points=[int(x) for x in stdin.readline().strip().split()]
    l1= Line.lineByPoints(Point(points[0],points[1]), Point(points[2],points[3]))
    l2= Line.lineByPoints(Point(points[4],points[5]), Point(points[6],points[7]))
    res=line_intersect(l1,l2)
    
    stdout.write(res+"\n")
stdout.write("END OF OUTPUT\n")