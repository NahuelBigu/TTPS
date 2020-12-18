
import math
from sys import stdin,stdout


#Lining Up UVA - 270 

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distancia_entre (self,point):
        return math.sqrt((point.x - self.x) * (point.x - self.x) + (point.y - self.y) * (point.y - self.y)) 

# Python program for implementation of Quicksort Sort
 
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
 
 
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and array[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]

    return high
 
 
def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
 

INFINITO= 1e1000
CERO= 1e-8
puntos=[]
def PuntLinea(n):
    array=[INFINITO]*2500
    maxPuntos=-1
    r=0
    for i in range(n-1):
        dic={}
        if (r+2 > n-i): break
        for j in range(i+1,n):
            if(puntos[i].x != puntos[j].x):
                pendiente=(puntos[i].y - puntos[j].y)/(puntos[i].x-puntos[j].x)
            else:
                pendiente= INFINITO
            if(not pendiente in dic):
                dic[pendiente]=2
            else:
                dic[pendiente]+=1
       

        for x,value in dic.items():
            maxPuntos=max(maxPuntos,value)
    return maxPuntos

primeravez=True
cases = int(stdin.readline())
if(cases!=0):
    stdin.readline()
    for _ in range(cases):
        if primeravez:
            primeravez=False
        else:
            stdout.write("\n")
        line = stdin.readline().strip()
        puntos=[]
        while line != '':
            x, y = [float(i) for i in line.split()]
            puntos.append(Point(x, y))
            line = stdin.readline().strip()
        
        stdout.write(str(PuntLinea(len(puntos)))+"\n")
        