from sys import stdin, stdout
# The Department of Redundancy Department UVA - 484 
# ACCEPTED 10ms 
outputDictionary={}
for lines in stdin:
    numbers=lines.strip().split()
    for nro in numbers:
        if(nro not in outputDictionary.keys()):
            outputDictionary[nro]=0
        outputDictionary[nro]+=1
for keys,values in outputDictionary.items():
    stdout.write(keys+" "+str(values)+"\n")