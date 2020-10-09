from sys import stdin,stdout

n=int(stdin.readline().strip())
seq=[]
DP=[-1]*n
prev=[-1]*n

def lis(idx):
    global DP,prev
    if (DP[idx] != -1): 
        return DP[idx]
    DP[idx] = 1
    prev[idx] = -1
    # Mínimo LIS = 1
    for i in range(idx):
        if ((seq[i] > seq[idx]) and (DP[idx] < (lis(i) + 1))):
            DP[idx] = lis(i) + 1
            prev[idx] = i
    return DP[idx]


seq=stdin.readline().strip().split()
for i in range(len(seq)):
    seq[i]=int(seq[i])



maxi=-1
maxiPos=-1
for i in range(len(seq)):
    aux=lis(i)
    if(aux>=maxi): 
        maxi=aux
        maxiPos=i
  
print(maxi)      

      
#PARA OBTENER LA LIS GRACIAS A PREV
print(set(prev))
for X in list(set(prev)):
    if(X != -1):
        print(seq[X])
print(seq[maxiPos])

