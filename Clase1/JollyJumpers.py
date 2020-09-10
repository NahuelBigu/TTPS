import sys
# WRONG ANSWER
def JollyJumpers(numbers):
    differences= set()
    for i in range(1,int(numbers[0])):
        difference= abs(int(numbers[i]) - int(numbers[i+1]))
        differences.add(difference)
    #for i in range(len(differences)):
        #if(differences[i] not in differences):
        #    return "Not Jolly"   
    return "Jolly"


for lines in sys.stdin:
    numbers= lines.strip().split()

    sys.stdout.write(JollyJumpers(numbers)+ "\n")