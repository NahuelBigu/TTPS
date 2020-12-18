from sys import stdin,stdout

def LCM (num):
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

n=int(stdin.readline().strip())
while (n != 0):
    print(str(lcm(n)).strip("0")[-1:])
    n=int(stdin.readline().strip())