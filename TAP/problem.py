from sys import stdin, stdout

grilla = [[False] * 10 for i in range(10)]
barcos = int(stdin.readline().strip())
fail=False
for _ in range(barcos):
    d,l,r,c=[int(x) for x in stdin.readline().strip().split(' ')]  # 
    c-=1
    r-=1
    if(d==0):
        #horizontal
        if (((c+l-1) >=10) or grilla[r][c]  ):
            fail=True
        else:
            for i in range(l):
                if(grilla[r][c+i]):
                    fail=True
                grilla[r][c+i]=True  
    else:
        #vertical
        if ((r+l-1 >=10) or grilla[r][c]):
            fail=True
        else:
            for i in range(l):
                if(grilla[r+i][c]):
                    fail=True
                grilla[r+i][c]=True  
stdout.write("N\n" if (fail ) else "Y\n")
