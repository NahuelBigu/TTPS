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
    

"""
 #MAS EFICIENTE
from sys import stdin, stdout
import math

cases=int(stdin.readline())
cases_results=[]
for I in range(cases):
    days=[0] * int(stdin.readline())
    for J in range(int(stdin.readline())):
        hartal_parameter=int(stdin.readline())
        for Z in range(math.floor(len(days)/hartal_parameter)):
            days[hartal_parameter*(Z+1)-1]=1      
    for K in range(5,len(days),7):
        days[K]=0
    for K in range(6,len(days),7):
        days[K]=0
    cases_results.append(days.count(1))
for N in cases_results:
    print(str(N))
"""