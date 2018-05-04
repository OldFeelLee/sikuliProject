import random 
import string
TitleOSD = find("1449208221887.png")
FishEyeOSD = find("1449208245303.png")

flag=1

def RandomTime():
    digits = "".join( [random.choice(string.digits)] )
    wait(digits)


while True:
    if (flag==1):   
        hover(TitleOSD)
        mouseDown(Button.LEFT)
        hover(FishEyeOSD)
        RandomTime()
        mouseUp(Button.LEFT)
        wait(1)
        flag=0
    else:
        hover(FishEyeOSD)
        mouseDown(Button.LEFT)
        hover(TitleOSD)
        RandomTime()
        mouseUp(Button.LEFT)
        wait(1)
        flag=1
        
    