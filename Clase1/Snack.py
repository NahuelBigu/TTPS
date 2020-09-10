from sys import stdin, stdout

#ACCEPTED

# Collection of products
products = {1: 4.00, 2:4.50, 3:5.00, 4:2.00 , 5:1.50}

# Lectura de datos
n=2
productCode, quantityProduct = [int(n) for n in stdin.readline().strip().split()]

# Imprimir
stdout.write("Total: R$ {:.2f}".format(products[productCode]*quantityProduct) + '\n')