#Hartals  UVA - 10050 
from sys import stdin ,stdout

def workingDaysLose(hartalsParametersOriginal,days):
    dayslose=0
    daysToFrSa=6
    hartalsParameters=hartalsParametersOriginal[:]
    for _ in range(days):
        hartal=False
        daysToFrSa-=1
        for hartalIndex in range(len(hartalsParameters)):
            hartalsParameters[hartalIndex]-=1
            if(hartalsParameters[hartalIndex]==0):
                #Huelga
                hartalsParameters[hartalIndex]=hartalsParametersOriginal[hartalIndex]
                if(daysToFrSa>0):
                    hartal=True
        if(hartal):
            dayslose+=1
        if(daysToFrSa==-1):
            daysToFrSa=6
    return str(dayslose)


cases=int(stdin.readline().strip())
for case in range(cases):
    days=int(stdin.readline().strip())
    politicalParties=int(stdin.readline().strip())
    hartalParameters=[]
    for politicalParty in range(politicalParties):
        hartalParameters.append(int(stdin.readline().strip()))
    stdout.write(workingDaysLose(hartalParameters,days)+"\n")
    