from sys import stdin,stdout
#Strategic Defense Initiative UVA - 497 
#ACCEPTED
def lisBU(seq):
    ans = 0
    for i in range(len(seq)):
        for j in range(i):
            if ((seq[j] < seq[i]) and (DP[i] < DP[j] + 1)):
                DP[i] = DP[j] + 1
                prev[i] = j
        if (DP[ans] < DP[i]):
            ans = i
    return ans # OJO: lo que se retorna es el índice.

cant=int(stdin.readline().strip())
if(cant!=0):
    stdin.readline()
    seq=[]
    for line in stdin:
        if(line == "\n"):
            DP=[1]*(len(seq))
            prev=[-1]*(len(seq))
            maximo=lisBU(seq)
            aux=maximo
            auxList=[]
            while(aux!=-1):
                auxList.insert(0,seq[aux])
                aux=prev[aux]
            stdout.write("Max hits: "+ str(DP[maximo])+"\n")
            for X in auxList:
                stdout.write(str(X)+"\n")
            stdout.write("\n")
            seq=[]
        else:
            latitud=int(line.strip())
            seq.append(latitud)

DP=[1]*(len(seq))
prev=[-1]*(len(seq))
maximo=lisBU(seq)
aux=maximo
auxList=[]
while(aux!=-1):
    auxList.insert(0,seq[aux])
    aux=prev[aux]
stdout.write("Max hits: "+ str(DP[maximo])+"\n")
for X in auxList:
    stdout.write(str(X)+"\n")
seq=[]







""" cant=int(stdin.readline().strip())
if(cant!=0):
    stdin.readline()
for i in range(cant):
    seq=[]
    latitud=stdin.readline()
    while(latitud != "\n" or latitud != ""):
        latitud=int(latitud.strip())
        seq.append(latitud)
        latitud=stdin.readline()
    DP=[1]*(len(seq)+5)
    prev=[-1]*(len(seq)+5)
    maximo=lisBU(seq)
    
    aux=maximo
    auxList=[]
    while(aux!=-1):
        auxList.insert(0,seq[aux])
        aux=prev[aux]
    stdout.write("Max hits: "+ str(DP[maximo])+"\n")
    for X in auxList:
        stdout.write(str(X)+"\n")
    if(i!=cant-1):
        stdout.write("\n")
 """