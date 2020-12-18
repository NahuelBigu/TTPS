
from sys import stdin, stdout
from math import sqrt
N=10000000
def criba():
    for i in range (2, int(sqrt(N))):
        if (isPrime[i]):
            for j in range(i*i, N, i):
                isPrime[j] = False

isPrime = [True] * N 

def Goldbach(n,prev):
    f=True
    i=2
    while (f and i<=n/2):
        if(isPrime[i]):
            if (isPrime[n-i]):
                prev+="{} {}\n".format(i,n- i)
                f=False
        i+=1
    if f:
        stdout.write('Impossible.\n')
    else:
        stdout.write(prev)


criba()

for line in stdin.readlines():
    x = int(line)
    if (x < 8):
        stdout.write('Impossible.\n')
    else:
        prev = ''
        if (x % 2 == 0):
            prev = prev + '2 2 '
            x = x - 4
        else: 
            prev = prev + '2 3 '
            x = x - 5
        Goldbach(x,prev)