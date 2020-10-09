from sys import stdin,stdout
#Edit distance SPOJ - EDIST 
#Accepted 

memo = [[-1] * 2050 for i in range(2050)]
for i in range(2050):
    memo[i][0]= i*1
for j in range(2050):
    memo[0][j]= j*1

def ED(s, t, cost_delete, cost_insert,  cost_replace):
    n = len(s) + 1
    m = len(t) + 1
    for i in range(1,n):
        for j in range(1,m):
            memo[i][j] = memo[i-1][j-1] + (int(s[i-1] != t[j-1])* cost_replace)
            memo[i][j] = min(memo[i][j], memo[i-1][j] + cost_delete)
            memo[i][j] = min(memo[i][j], memo[i][j-1] + cost_insert)
    return memo[n-1][m-1]



cant=int(stdin.readline().strip())
for _ in range(cant):
    cadenaA=stdin.readline()
    cadenaB=stdin.readline()
    minimoOperacion=ED(cadenaA,cadenaB,1,1,1)
    stdout.write(str(minimoOperacion)+"\n")