from sys import stdin, stdout
# Accepted
# I Can Guess the Data Structure! UVA - 11995 
for line in stdin:
    cases=int(line.strip())
    stack=[]  
    isStack=1
    queue=[]
    isQueue=1
    priority=[]
    isPriority=1
    for case in range(cases): 
        operation=stdin.readline().strip().split()
        if(int(operation[0])==1):
            #Into the bag
            stack.append(int(operation[1]))
            queue.append(int(operation[1]))
            priority.append(int(operation[1]))
        else:
            #Take out from the bag
            outElement=int(operation[1])
            if(isStack):
                if(stack and stack[len(stack)-1]==outElement):
                    stack.pop()
                else:
                    isStack=0
            if(isQueue):
                if(queue and queue[0]==outElement):
                    queue.pop(0)
                else:
                    isQueue=0
            if(isPriority):
                if(priority and max(priority)==outElement):
                    priority.pop(priority.index(max(priority)))        
                else:
                    isPriority=0    
    if(isStack+isQueue+isPriority > 1):
        # Not sure
        stdout.write("not sure\n")
    elif (isStack+isQueue+isPriority == 0):
        #Imposible
        stdout.write("impossible\n")
    elif isStack == 1:
        #STACK
        stdout.write("stack\n")
    elif isPriority == 1:
        #PRIORITY
        stdout.write("priority queue\n")
    elif isQueue == 1:
        #QUEUE
        stdout.write("queue\n")