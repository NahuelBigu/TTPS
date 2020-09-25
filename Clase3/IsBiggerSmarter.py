#Is Bigger Smarter? UVA - 10131 
from sys import stdin,stdout

DP=[-1]*1000
prev=[-1]*1000

def lis(idx):
    global DP,prev
    if (DP[idx] != -1): 
        return DP[idx]
    DP[idx] = 1
    prev[idx] = -1
    # Mínimo LIS = 1
    for i in range(idx):
        if ((seq2[i][1] > seq2[idx][1]) and (DP[idx] < (lis(i) + 1))):
            DP[idx] = lis(i) + 1
            prev[idx] = i
    return DP[idx]

seq=[]

for index,line in enumerate(stdin):
    elephant=line.strip().split()
    elephant2=[]
    for i in range(2):
        elephant2.append(int(elephant[i]))
    elephant2.append(index+1)

    elephant=tuple(elephant2)
    seq.append(elephant)

seq2 = sorted(seq, key=lambda x: (x[0], x[1],-x[2]))
maxi=-1
maxiPos=-1
for i in range(len(seq2)):
    aux=lis(i)
    if(aux>=maxi): 
        maxi=aux
        maxiPos=i
        
print(maxi)
#PARA OBTENER LA LIS GRACIAS A PREV



aux=maxiPos
auxList=[]
while(aux!=-1):
    auxList.insert(0,seq2[aux][2])
    aux=prev[aux]

for X in auxList:
    print(X)
