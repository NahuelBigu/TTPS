import math
from sys import stdin,stdout
EPSILON=1e-9

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

    def ordenada(self):
        return self.c / (-self.b)

class Segment:
    def __init__(self,puntoA,puntoB):
        self.puntoA=puntoA
        self.puntoB=puntoB

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distancia_entre (self,point):
        return math.sqrt((point.x - self.x) * (point.x - self.x) + (point.y - self.y) * (point.y - self.y)) 

    def point_in_box(self, lbPoint, rtPoint):
        return( (self.x >= min(lbPoint.getX(),rtPoint.getX())) and (self.x <= max(lbPoint.getX(),rtPoint.getX()))and (self.y >= min(lbPoint.getY(),rtPoint.getY())) and (self.y <= max(lbPoint.getY(),rtPoint.getY())) )

def PARALLEL(l1,l2):
    return (abs(l1.getA() - l2.getA()) <= EPSILON) and (abs(l1.getB() - l2.getB()) <= EPSILON)

def SAME_LINE(l1,l2):
    return PARALLEL(l1,l2) and (abs(l1.getC() - l2.getC()) <= EPSILON)
    
    
def intersection_point(l1,l2):
    ## CHECKEAR EL TEMA DE SI ES LA MISMA LINEA Y SI ES PARALELA ANTES.
    x = (l2.getB()*l1.getC() - l1.getB()*l2.getC()) / (l2.getA()*l1.getB() - l1.getA()*l2.getB())
    if (abs(l1.getB()) > EPSILON):
        y = - (l1.getA() * x + l1.getC()) / l1.getB()
    else:
        y = - (l2.getA() * x + l2.getC()) / l2.getB()
    return Point(x,y)

def segments_intersect (s1,s2):

    l1= Line.lineByPoints(s1.puntoA,s1.puntoB)
    l2= Line.lineByPoints(s2.puntoA,s2.puntoB)
    
    if (SAME_LINE(l1,l2)):
        if (s1.puntoA.point_in_box(s2.puntoA,s2.puntoB) or s1.puntoB.point_in_box(s2.puntoA,s2.puntoB) or s2.puntoA.point_in_box(s1.puntoA,s1.puntoB) or s2.puntoB.point_in_box(s1.puntoA,s1.puntoB) ):
            return "LINE" 
    if(PARALLEL(l1,l2)):
        return "NONE"
    p=intersection_point(l1,l2)
    if (p.point_in_box(s1.puntoA,s1.puntoB) and p.point_in_box(s2.puntoA,s2.puntoB)):
        return "POINT {:.2f} {:.2f}".format(p.getX(),p.getY())
    return "NONE"

cases = int(stdin.readline())
stdout.write("INTERSECTING LINES OUTPUT\n")
for _ in range(cases):
    points=[int(x) for x in stdin.readline().strip().split()]
    segemento1=Segment(Point(points[0],points[1]), Point(points[2],points[3]))
    segemento2=Segment(Point(points[4],points[5]), Point(points[6],points[7]))
    res=segments_intersect(segemento1,segemento2)
    #res=segments_intersect(Point(points[0],points[1]), Point(points[2],points[3]),Point(points[4],points[5]), Point(points[6],points[7]))
    print(res)
stdout.write("END OF OUTPUT\n")