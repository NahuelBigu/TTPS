import math

def criba(n):
	primes = []
	isPrime = [True for i in range(n)]
	isPrime[0] = isPrime[1] = False

	for i in range(n):
		if isPrime[i]:
			primes.append(i)
			h = 2
			while i*h < n:
				isPrime[i*h] = False
				h += 1

	return primes, isPrime

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def gcd2(a,b):
    t=0
    while (b):
        t=a
        a=b
        b=t%b
    return -a if a < 0 else a
def lcm(a,b):
    return (a*b) / (gcd(a,b))

def lcm2(num):
    c=0
    for a in range (1,num+1):
        for b in range (1,num+1):
            c+=(a*b) / (gcd(a,b))
    return c


def LCM1 (num):
    descompuestos=[]
    numeros=set()
    for i in range (2,num+1):
        dic=descomponer(i)
        descompuestos.append(dic)
        for key in dic.keys():
            numeros.add(int(key))
    res=1
    for num in numeros:
        maxPotencia=-1
        for d in descompuestos:
            if(num in d.keys()):
                maxPotencia=max(maxPotencia,d[num])
        res*=num**maxPotencia
    return res



def descomponer(n):
    numeros={}
    if (n==1):
        return {}
    while(n>1):
        x=2
        while((n % x) != 0):
            x+=1
        n/=x
        if(x not in numeros.keys()):
            numeros[x]=0
        numeros[x]+=1    
    return numeros

print(str(LCM1(5)).strip("0")[-1:])