from sys import stdin, stdout

# 1069 - Diamonds and Sand    www.urionlinejudge.com.br
# ACCEPTED 0.007s
cases=int(stdin.readline().strip())
for case in range(cases):
    pilaDimonds=[]
    diamonds=0
    mine=stdin.readline().strip()
    for asd in mine:
        if(asd == '<'):
            pilaDimonds.append('<')
        elif(asd == '>'):
            if(len(pilaDimonds) >0):
                pilaDimonds.pop()
                diamonds+=1
    stdout.write(str(diamonds)+"\n")


