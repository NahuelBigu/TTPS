from sys import stdin,stdout

line=stdin.readline().strip()

pl=0
pr=0
gl=0
gr=0
juega=True
winner=False
for c in line:
    if gl!=2 and gr!=2:
        if juega and c=='S':
            pl+=1
        elif juega and c=='R':
            pr+=1
            juega=False
        elif not juega and c=='S':
            pr+=1
        elif not juega and c=='R':
            pl+=1
            juega=True
        if (pl>=5 and pl-pr>=2) or pl==10:
            gl+=1
            pl=0
            pr=0
        if (pr>=5 and pr-pl>=2) or pr==10:
            gr+=1
            pl=0
            pr=0
    if c=='Q' and (gl==2 or gr==2):
        if gl==2:
            stdout.write(str(gl)+' (winner) - '+str(gr)+'\n')
        else:
            stdout.write(str(gl)+' - '+str(gr)+' (winner)\n')
    elif c=='Q':
        if juega: 
            stdout.write(str(gl)+' ('+str(pl)+'*) - '+str(gr)+' ('+str(pr)+')\n')
        if not juega: 
            stdout.write(str(gl)+' ('+str(pl)+') - '+str(gr)+' ('+str(pr)+'*)\n')