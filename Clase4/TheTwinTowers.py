from sys import stdin,stdout
#The Twin Towers UVA - 10066 
#Accepted
def LCS(s,t):
    n = len(s) + 1 
    m = len(t) + 1
    memo = [[-1] * m for i in range(n)]
    for i in range(n):
        memo[i][0]=0
    for j in range(m):
        memo[0][j]=0
    for i in range(1,n):
        for j in range(1,m):
            if(s[i-1] == t[j-1]):
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])            
    return memo[n-1][m-1]

cases=1
tamañoA,tamañoB=[int(x) for x in stdin.readline().strip().split(' ')]
while(tamañoA+tamañoB!=0):
    towerA=[int(x) for x in stdin.readline().strip().split(' ')]
    towerB=[int(x) for x in stdin.readline().strip().split(' ')]
    tiles=LCS(towerA,towerB)
    stdout.write("Twin Towers #"+str(cases)+"\n")
    cases+=1
    stdout.write("Number of Tiles : "+str(tiles)+"\n")
    tamañoA,tamañoB=[int(x) for x in stdin.readline().strip().split(' ')]
