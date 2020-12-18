from sys import stdin, stdout

monedas=100
monedasMaximo=100
cajas = int(stdin.readline().strip())
for x in range(cajas):
    valor = int(stdin.readline().strip())
    monedas= monedas+valor
    monedasMaximo= max(monedas,monedasMaximo)
stdout.write(str(monedasMaximo)+"\n")