import sys

cantidades=[0]*10
for lines in sys.stdin:
    line= lines.strip()
    numero=int(line[0])
    cantidades[numero]+=1

for i,x in enumerate(cantidades[0:-1]):
    print(str((i+1) % 10) + " - " + str(x))