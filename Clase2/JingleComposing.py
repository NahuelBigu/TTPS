#Jingle Composing UVA - 12195 
from sys import stdin, stdout

notes={'W':1 , 'H':1/2 ,'Q':1/4 , 'E':1/8, 'S':1/16 , 'T':1/32 ,'X':1/64}

#110ms ACCEPTED
composition=stdin.readline().strip()
while (composition!="*"):
    composition=composition.split("/")[1:-1]
    rightDuration=0
    for measure in composition:
        timeMeasure=0
        for note in measure:
            if(timeMeasure<1):
                timeMeasure+=notes[note]
            else:
                timeMeasure=-1
                break
        if(timeMeasure==1):
            rightDuration+=1
    stdout.write(str(rightDuration)+"\n")   
    composition=stdin.readline().strip()


"""
#120ms ACCEPTED
composition=stdin.readline().strip()
while (composition!="*"):
    composition=composition.split("/")[1:-1]
    rightDuration=0
    for measure in composition:
        timeMeasure=0
        for note in measure:
            timeMeasure+=notes[note]
        if(timeMeasure==1):
            rightDuration+=1
    stdout.write(str(rightDuration)+"\n")   
    composition=stdin.readline().strip()


#140ms ACCEPTED
composition=stdin.readline().strip()
while (composition!="*"):
    rightDuration=0
    timeMeasure=0
    for note in composition[1:]:
        if(note!="/"):
            timeMeasure+=notes[note]
        else:
            if(timeMeasure==1):
                rightDuration+=1
            timeMeasure=0
    stdout.write(str(rightDuration)+"\n") 
    composition=stdin.readline().strip()

"""
