from sys import stdin, stdout

stdout.write('Enter two numbers: \n')

a, b = [int(n) for n in stdin.readline().strip().split()]

# También es válido
# a, b = map(int, stdin.readline().split())

stdout.write('The sum of the two numbers is: ' + str(a + b) + '\n')

# Podemos usar f (python 3.6 <) para formatear el texto de forma más comoda(pero esto tal vez impacte en el TE)
# stdout.write(f'The sum of the two numbers is: {a+b} \n')
