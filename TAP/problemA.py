from sys import stdin, stdout

[n, a, b] = [int(x) for x in stdin.readline().strip().split()]

res = []
memo = [[-1] * (b-a+10) for i in range(n+10)]


def it(num_actual, n_paquete, iteracion):
    act = num_actual-n_paquete
    if memo[act][n_paquete] != -1:
        return memo[act][n_paquete]
    iteracion += 1
    if iteracion >= n:
        memo[act][n_paquete] = iteracion
        res.append(iteracion)
        return iteracion
    if act <= 0:
        memo[act][n_paquete] = iteracion
        res.append(iteracion)
        return iteracion
    else:
        for i in range(b-a+1):
            it(act, i+a, iteracion)



for z in range(a,b):
    it(n, z, 0)

suma = 0
for r in res:
    suma += r

print(suma/len(res))