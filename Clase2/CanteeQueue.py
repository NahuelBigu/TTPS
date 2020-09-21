from sys import stdin, stdout

# 1069 - Canteen Queue   www.urionlinejudge.com.br
# Accepted 
cases=int(stdin.readline().strip())
for case in range(cases):
    studentsNro=int(stdin.readline().strip())
    students=[int(n) for n in stdin.readline().strip().split()]
    count=0
    grades=list(enumerate(students))
    order=grades[:]    
    order.sort(key = lambda x: x[1],reverse=True)
    order=list(filter(lambda x: x[0]==order[x[0]][0] ,grades))
    print (order)
    stdout.write(str(len(order))+"\n")
