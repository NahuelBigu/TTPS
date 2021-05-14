from sys import stdin, stdout

inputs=stdin.readline().split()

listaSets=[]
listaFinal=[]
for string in inputs:
    aux= str(string).lower()
    caracteres=set(aux)
    if (caracteres not in listaSets):
        listaSets.append(caracteres)
        listaFinal.append(aux)

listaFinal.sort()
print(listaFinal)