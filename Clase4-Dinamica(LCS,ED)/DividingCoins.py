from sys import stdin, stdout
# Dividing coins UVA - 562

def maxdif():
    """Metodo que puede servir para obtener que tan cerca de K podes llegar sumando las entradas"""
    aux=set([0])
    for i in range(cant):
        temp_aux=aux.copy()
        for j in temp_aux:
            acumulado=j+coins[i]
            if(acumulado<=K):
                if(acumulado==K):
                    return K
                else:
                    aux.add(acumulado)
    listaux=sorted(list(aux))
    return listaux[-1]

cases = int(stdin.readline().strip())
for _ in range(cases):
    cant = int(stdin.readline().strip())
    coins = []
    maxCoins = 0
    for index, coin in enumerate(stdin.readline().strip().split()):
        coins.append(int(coin))
        maxCoins += int(coin)
    K=maxCoins//2 + ( 0 if maxCoins%2==0 else 1)
    
    coinsDiv=maxdif()
    output = str(abs(maxCoins-coinsDiv-coinsDiv))
    stdout.write(output+"\n")
