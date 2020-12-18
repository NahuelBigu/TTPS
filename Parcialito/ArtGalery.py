import math
from sys import stdin,stdout
#Art Galery - 10078

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    @staticmethod
    def direction(p1, p2, p3): #Realiza producto en cruz
        return "Der" if (((p2.getX() - p1.getX()) * (p3.getY() - p1.getY())) - ((p3.getX() - p1.getX()) * (p2.getY() - p1.getY())) > 0) else "Izq"

            



cant=int(stdin.readline().strip())
while(cant!=0):
    puntos=[]
    primera=True
    puntosCriticos=False
    for i,_ in enumerate(range(cant)):
        x,y=[int(x) for x in stdin.readline().strip().split()]
        puntos.append(Point(x,y))
        if (i>=2):
            direccion=Point.direction(puntos[i],puntos[i-1],puntos[i-2])
            
            if (primera):
                direccionActual=direccion
                primera=False
            elif (direccion != direccionActual) :
                # No mantiene la misma direccion , por ende genera un punto critico
                puntosCriticos=True
    if (not puntosCriticos):
        if (Point.direction(puntos[0],puntos[cant-1],puntos[cant-2]) != direccionActual): # Los ultimos 2 con el primer punto
            puntosCriticos=True
        else:
            if((Point.direction(puntos[1],puntos[0],puntos[cant-1])) != direccionActual):      # El ultimo con el primero y el segundo
                puntosCriticos=True

    if (puntosCriticos):
        stdout.write("Yes\n")
    else:
        stdout.write("No\n")
  
    cant=int(stdin.readline().strip())