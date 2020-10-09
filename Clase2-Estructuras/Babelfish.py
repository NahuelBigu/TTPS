#Babelfish UVA - 10282 
#Accepted

from sys import stdin, stdout
dictonary={}
while True:
    inputs=stdin.readline().strip()
    if not inputs: break
    dictionaryEntrie=inputs.split()
    dictonary[dictionaryEntrie[1]]=dictionaryEntrie[0]

for line in stdin:
    menssage=line.strip()
    try:
        stdout.write(dictonary[menssage] + "\n")
    except:
        stdout.write("eh\n")
        
