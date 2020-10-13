from sys import stdin,stdout
#String Distance and Transform Process UVA - 526 



def ED(s, t, cost_delete, cost_insert,  cost_replace):
    for i in range(n): memo[i][0]= i* cost_delete
    for j in range(m): memo[0][j]= j* cost_insert
    for i in range(1,n):
        for j in range(1,m):
            memo[i][j] = memo[i-1][j-1] + (int(s[i-1] != t[j-1])* cost_replace)
            memo[i][j] = min(memo[i][j], memo[i-1][j] + cost_delete)
            memo[i][j] = min(memo[i][j], memo[i][j-1] + cost_insert)                
    return memo[n-1][m-1]

def imprimirCamino():
    stringA2=stringA[:]
    stringB2=stringB[:]
    operaciones=[]
    i=n-1
    j=m-1
    while(i > 0) or (j > 0):
        if(i > 0 and j > 0 and stringA2[i-1] == stringB2[j-1]):
            i-=1
            j-=1
        elif(i>0 and memo[i][j] == memo[i-1][j] +1):
            operaciones.append((" Delete ",i ))
            stringA2=stringA2[:i-1]+stringA2[i:]
            i-=1
        elif (j>0 and memo[i][j] == memo[i][j-1]+1):
            operaciones.append((" Insert ",i+1,stringB2[j-1]))
            stringA2=stringA2[:i]+stringB2[j-1]+stringA2[i+1:]
            j-=1
        elif (i>0 and j>0 and stringA2[i-1] != stringB2[j-1]):
            operaciones.append((" Replace ",i,stringB2[j-1]))
            stringA2=stringA2[:i-1] + stringB2[j-1] + stringA2[i:]
            i-=1
            j-=1
    ind = 0
    for i,op in enumerate(reversed(operaciones)):
    
        print(str(i+1)+op[0]+str(op[1]+ind)+ ((","+op[2])  if len(op)>2  else "" ) )
        if(op[0] == " Delete "): ind-=1
        if(op[0] == " Insert "): ind+=1
        

primero=True
cant=0
for line in stdin:
    cant+=1
    if(cant==2):
        ##analizar
        stringB=line.strip()
        n = len(stringA) + 1
        m = len(stringB) + 1
        memo = [[-1] * m for i in range(n)]
        prev = [[-1] * m for i in range(n)]
        minMov=ED(stringA,stringB,1,1,1)
        if(not primero):
            print()
        else: primero=False
        print(minMov)
        imprimirCamino()
        cant=0
        
    else:
        stringA=line.strip()