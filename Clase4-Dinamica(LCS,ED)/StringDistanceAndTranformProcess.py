from sys import stdin,stdout
#String Distance and Transform Process UVA - 526 



def ED(s, t, cost_delete, cost_insert,  cost_replace):
    for i in range(n): memo[i][0]= i* cost_delete
    for j in range(m): memo[0][j]= j* cost_insert
    for i in range(1,n):
        for j in range(1,m):
            memo[i][j] = memo[i-1][j-1] + (int(s[i-1] != t[j-1])* cost_replace)
            prev[i][j]= (i-1,j-1)
            if(memo[i][j] > memo[i-1][j] + cost_delete):
                memo[i][j]=memo[i-1][j] + cost_delete
                prev[i][j]= (i-1,j)
            if ( memo[i][j] > memo[i][j-1] + cost_insert):
                memo[i][j]=memo[i][j-1] + cost_insert
                prev[i][j]= (i,j-1)
    return memo[n-1][m-1]

def imprimirCamino2():
    for i in range(1,n): prev[i][0]= (i-1,0)
    for j in range(1,m): prev[0][j]= (0,j-1)
    for k in prev: print(k)
    operaciones=[]
    i=n-1
    j=m-1
    while(i+j != 0 ):
        print(prev[i][j])
        print(i)
        print(j)
        if (i==0):
            #insersion
            operaciones.append(" Insersion "+str(j)+","+stringB[j-1])
            j-=1  
        elif (j==0):
            #delete
            operaciones.append(" Delete "+str(i))  
            i-=1
        else:      
            if(prev[i][j][0]!=i and prev[i][j][1]!= j):
                #fue en diagonoal pudo remplazar o era igual
                if(stringA[i-1] != stringB[j-1]):
                    operaciones.append(" Remplace "+str(prev[i][j][0]-1)+","+stringB[prev[i][j][1]])
            elif(prev[i][j][0]==i):
                #fue hacia la izq Inserto
                operaciones.append(" Insersion "+str(prev[i][j][1]+1)+","+stringB[j-1]) 
            elif(prev[i][j][1]==j):
                #fue hacia arriba Elimino
                operaciones.append(" Delete "+str(i))  
            aux=prev[i][j][0]
            j=prev[i][j][1]
            i=aux
    for i,op in enumerate(reversed(operaciones)):
        print(str(i+1)+op)
def imprimirCamino():
    operaciones=[]
    i=n-1
    i2=0
    j=m-1
    while(i != 0) or (j != 0):
        print("i: "+str(i)+"- j: "+str(j))
        if (i==0):
            #insersion
            j-=1
            operaciones.append(" Insersion "+str(i+i2+1)+","+stringB[j])
            i2+=1
        elif (j==0):
            #delete
            operaciones.append(" Delete "+str(i))  
            i-=1
        else:
            minimo = min(memo[i-1][j-1],memo[i-1][j],memo[i][j-1])
            if(minimo == memo[i-1][j-1] and memo[i][j] == memo[i-1][j-1]):
                i-=1
                j-=1
            elif (minimo == memo[i-1][j]):
                i-=1
                operaciones.append(" Delete "+str(i))  
            elif (minimo == memo[i][j-1]):
                j-=1
                operaciones.append(" Insersion "+str(i+i2+1)+","+stringB[j])
                i2+=1
            elif (minimo == memo[i-1][j-1] and memo[i][j] != memo[i-1][j-1]):
                i-=1
                j-=1
                operaciones.append(" Remplace "+str(i)+","+stringB[j])
    for i,op in enumerate(reversed(operaciones)):
        print(str(i+1)+op)

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
        for fila in memo:
            print(str(fila))
        for fila in prev:
            print(str(fila))   
        print(minMov)
        imprimirCamino()
        imprimirCamino2()
        cant=0
    else:
        stringA=line.strip()