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
    cantFriends=int(stdin.readline().strip())
    users={} # Friends
    cant=0
    p=[]
    fd = {}
    rank=[]
    for i in range(100001):   
        p.append(i)
        rank.append(0)
        
    
    for _ in range(cantFriends):
        i,j=[n for n in stdin.readline().strip().split()]
        if(i not in users.keys()):
            users[i]=cant
            fd[cant] = 1
            cant+=1
        if(j not in users.keys()):
            users[j]=cant
            fd[cant] = 1
            cant+=1
        ant_i = find_set(users[i])
        ant_j = find_set(users[j])   
        union_set(users[j],users[i])
        z = find_set(users[i])
        if z != ant_i:
            fd[z] += fd[ant_i]
        if z != ant_j:
            fd[z] += fd[ant_j]

        stdout.write(str(fd[z])+"\n")