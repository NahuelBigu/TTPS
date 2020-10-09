#Ilya and Queries  CodeForces - 313B 
#https://vjudge.net/problem/CodeForces-313B

from sys import stdout,stdin

def build_rsq():
    DP[0]=0
    for I in range(1,(n-1)):
        DP[I]=DP[I-1]
        if(string[I-1]==string[I]):
            DP[I]+=1

    DP[n-1]=DP[n-2]

def rsq(l,r):
    return DP[r-1]-DP[l-1]


string=stdin.readline().strip()
n=len(string)+1
DP=[0]*n
build_rsq()

queries=int(stdin.readline().strip())
for _ in range(queries):
    l, r = [int(n) for n in stdin.readline().strip().split()]
    stdout.write(str(rsq(l,r))+"\n")
 
