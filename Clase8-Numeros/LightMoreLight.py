from sys import stdin, stdout
from math import sqrt

lights = int(stdin.readline())
while lights != 0:  
    raiz=sqrt(lights) # Raiz , si tiene raiz es porque queda prendida sino es porque queda apagada
    if raiz.is_integer(): 
        stdout.write("yes\n")
    else:
        stdout.write("no\n")
    lights = int(stdin.readline())