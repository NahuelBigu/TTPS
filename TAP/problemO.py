from sys import stdin, stdout
import math 

import numpy as np


class Point:
    
    def __init__(self, xValue, yValue):
        self.x = xValue
        self.y = yValue

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    # Distancia entre el punto y otro
    def distanceToPoint(self, otherPoint):
        dx = math.fabs(self.x - otherPoint.getX())
        dy = math.fabs(self.y - otherPoint.getY())
        return math.hypot(dx,dy)  # sqrt(x*x + y*y)

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
n = int(stdin.readline().strip())
puntos = []
primero=True
[a, b] = [int(x) for x in stdin.readline().strip().split()]
prim=Point(a,b)
ant=Point(a,b)

calor=0
for _ in range(n-1):
    [a, b] = [int(x) for x in stdin.readline().strip().split()]
    p=Point(a,b)
    an=(angle_between((a,b),(1,0)))
    dis=ant.distanceToPoint(p)
    ant=p
    calor+=an*dis

an=(angle_between((a,b),(1,0)))
dis=ant.distanceToPoint(prim)
calor+=an*dis
print(calor)


