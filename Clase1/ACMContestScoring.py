import sys


#ACCEPTED


wrongs={}
score=0
solves=0
for lines in sys.stdin:
    line= lines.strip().split()
    if(len(line)==1):
        print(solves,score)
        wrongs={}
        score=0
        solves=0
    else:
        if(line[1] not in wrongs.keys()):
            wrongs[line[1]]=0
        if(line[2]=="right"):
            #ProblemaResuelto
            solves+=1
            score+=wrongs[line[1]]+int(line[0])
        else:
            wrongs[line[1]]+=20
