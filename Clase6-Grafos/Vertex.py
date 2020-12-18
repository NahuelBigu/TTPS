from sys import stdin, stdout
#Vertex UVA - 280
#Accepted


def dfs(v):
    if v in adyacentes:
        for w in adyacentes[v]: 
            if (not(visited[w])):
                visited[w] = True
                dfs(w)

        
n = int(stdin.readline().strip())
while (n != 0): 
    adyacentes= {}
    line = stdin.readline().strip()
    while (line !="0"):
        line = [int(l) for l in line.split()]
        adyacentes[line[0]]= line[1:]
        line = stdin.readline().strip()
    check = stdin.readline().strip()
    check = [int(l) for l in check.split()]
    for x in range(1, check[0]+1):
        visited = [False] * 110 
        dfs(check[x])
        res = ""
        cant = 0
        for x in range(1,n+1):
            if (not(visited[x])):
                res += " " + str(x)
                cant += 1
        stdout.write(str(cant) + res + "\n")
    n = int(stdin.readline().strip())