from sys import stdin,stdout
#Bars UVA - 12455 
#Accepted 

def mochila (): #Consideramos N = 0 como sin elementos
    for i in range(N+1): DP[i][0] = 0
    for j in range(K+1): DP[0][j] = 0
    
    for i in range(1,N+1):
        for j in range(1,K+1):
            if (elem[i-1][0] > j):
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = max(DP[i-1][j], DP[i-1][j-elem[i-1][0]] + elem[i-1][1])
    return DP[N][K]
 

cases=int( stdin.readline().strip() )
for _ in range(cases):
   K=int(stdin.readline().strip())  #PESO MAXIMO
   N=int(stdin.readline().strip())  #CANT OBJETOS
   DP = [[-1] * (K+1) for i in range(N+1)] 

   elem2=[int(x) for x in stdin.readline().strip().split(' ')]
   elem = [[1] * 2 for _ in range(N+1)] 
   for index,e in enumerate(elem2):
       elem[index][1]=e
       elem[index][0]=e

   output= "YES" if (mochila()==K) else "NO"
   stdout.write(output+"\n")
   