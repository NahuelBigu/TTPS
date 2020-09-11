import sys
# ACCEPTED


def JollyJumpers(numbers):
    differences= set()
    for i in range(1,int(numbers[0])):
        difference= abs(int(numbers[i]) - int(numbers[i+1]))
        #if(difference<int(numbers[0])):
        differences.add(difference)
    for x in range(1,int(numbers[0])):
        if(x not in differences):
            return "Not jolly"   
    return "Jolly"


for lines in sys.stdin:
    numbers= lines.strip().split()

    sys.stdout.write(JollyJumpers(numbers)+ "\n")