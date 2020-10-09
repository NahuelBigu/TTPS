from sys import stdin,stdout
#Candy UVA - 12146 
#Accepted
m=0
n=0

def candy():
    memo = [[-1] * m for i in range(n)]
    for i in reversed(range(n)):
        j=m-1
        while(j>=0):
            if(j<m-2):
                #misma fila busco max
                memo[i][j]=boxes_candy[i][j]+max(memo[i][j+2] if (j+2<m) else 0 ,memo[i][j+3] if (j+3<m) else 0 )
            else:
                #busco en 2 filas abajo el maximo entre los 2 primeras columnas.
                memo[i][j]=boxes_candy[i][j]+max(memo[i+2][0] if (i+2<n) else 0, #Primera pos , fila i+2 
                                                 memo[i+2][1] if (i+2<n and 1<m) else 0, #Segunda pos , fila i+2 
                                                 memo[i+3][0] if (i+3<n) else 0 , #Primera pos , fila i+3 
                                                 memo[i+3][1] if (i+3<n and 1<m) else 0 #Segunda pos , fila i+3 
                                                 )
            j-=1
    return max(memo[0][0], #Primera pos , fila 1 
               memo[0][1] if (1<m) else 0, #Segunda pos , fila 1 
               memo[1][0] if (1<n) else 0 , #Primera pos , fila 2 
               memo[1][1] if (1<n and 1<m) else 0 #Segunda pos , fila 2 
               )    

n,m=[int(x) for x in stdin.readline().strip().split(' ')]
while (n!=0 and m!=0):
    boxes_candy = [[-1] * m for i in range(n)]
    for i in range(n):
        boxes_candy[i]=[int(x) for x in stdin.readline().strip().split(' ')]
    
    print(candy())
    n,m=[int(x) for x in stdin.readline().strip().split(' ')]