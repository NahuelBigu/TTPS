from sys import stdin, stdout


def peso(var):
    return var[2]
def dfs(start, fin):
    global mst
    aristas=mst[start]
    visitados[start]= True
    if start== fin:
        return 0
    
    for conectado_con in aristas:
        if not visitados[conectado_con]:
            res=dfs(conectado_con,fin)
            if res >= 0:
                return max(mst[start][conectado_con], res)
               
    return -1

case=0           
entrada=stdin.readline().split()

while entrada != ["0","0","0"]:
    c=int(entrada[0])
    s=int(entrada[1])
    q=int(entrada[2])
    aristas = []

    for street in range(s):
        entrada=stdin.readline().split()
        aristas.append([int(entrada[0]),int(entrada[1]),int(entrada[2])])

    aristas.sort(key=peso)
    # stdout.write(aristas)

    mst={}
    for cross in range(1,c+1):
        mst[cross]={}
    conocidos =[ {x} for x in range(0,c+1)]


    costo_mst=0
    for ari in aristas:
        # if not ((ari[0] in mst) and (ari[1] in mst)):
        if not ari[1] in conocidos[ari[0]]:
            costo_mst = costo_mst + ari[2]
            aux= conocidos[ari[0]].union(conocidos[ari[1]])
            for setnum in aux:
                conocidos[setnum]=aux
            
            # mst.setdefault(ari[0],{})
            # mst.setdefault(ari[1],{})
            #mst[ari[0]][ari[1]]= ari[2]
            #mst[ari[1]][ari[0]]= ari[2]


    case+=1
    stdout.write("Case #"+str(case)+"\n")
    for querry in range(q):
        entrada=stdin.readline().split()
        visitados=[ False for x in range(0,c+1)]
        result= dfs(int(entrada[0]),int(entrada[1]))
        if result == -1:
            stdout.write("no path\n")
        else:
            stdout.write( str(result)+ "\n")
    entrada=stdin.readline().split()
    if entrada != ["0","0","0"]:
        stdout.write("\n")
    
    