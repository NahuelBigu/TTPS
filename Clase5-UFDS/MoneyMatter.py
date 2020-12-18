from sys import stdin, stdout
#Accepted
def find_set(i):
    if (i == p[i]):
        return i 
    else:
        p[i]=find_set(p[i])
        return p[i]

def same_set(i, j):
    return find_set(i) == find_set(j)

def union_set(i,j):
    if (not same_set(i, j)):
        x = find_set(i)
        y = find_set(j)
        if (rank[x] > rank[y]):
            p[y] = x
        else:
            p[x] = y
            if (rank[x] == rank[y]): rank[y]+=1


cases = int(stdin.readline().strip())
for _ in range(cases):
    size,cantFriends=[int(n) for n in stdin.readline().strip().split()]
    owes=[] # elementos de lo que puso o lo que debe
    p=[]
    rank=[]
    for i in range(size):   
        owes.append(int(stdin.readline().strip()))
        p.append(i)
        rank.append(0)
    
    for _ in range(cantFriends):
        i,j=[int(n) for n in stdin.readline().strip().split()]
        union_set(j,i)
    deudas={}
    for i in range(size): 
        father=find_set(i)
        if(father not in deudas.keys()):
            deudas[father]=0
        deudas[father]+=owes[i]
    sol=[x for x in list(deudas.values()) if x!=0]
    if (not sol):
        stdout.write("POSSIBLE\n")
    else:
        stdout.write("IMPOSSIBLE\n")