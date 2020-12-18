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

cases=1
n,m=[int(n) for n in stdin.readline().strip().split()]
while (n!=0 and m!=0):
    p=[]
    rank=[]
    for i in range(n):   
        p.append(i)
        rank.append(0)

    for _ in range(m):
        i,j=[int(n) for n in stdin.readline().strip().split()]
        union_set(j-1,i-1)
    
    cant=0
    for i in range(n):
        if(p[i]==i):
            cant+=1
    stdout.write("Case "+str(cases)+": "+str(cant)+"\n")
    cases+=1
    n,m=[int(n) for n in stdin.readline().strip().split()]