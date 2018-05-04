import random
import string

def RanTime():    #random 시간
    ran = "".join([random.choice(string.digits)])
    s=int(ran)
    wait(s)
    global t
    t = s*10
def PTZ_short(): 
    RanTime()
    print(t)
    wait(t)
    #PTZ_short
    click(Pattern("1455257755424.png").targetOffset(-21,0))
    RanTime()
    click(Pattern("1455257755424.png").targetOffset(20,1))
    RanTime()
    click(Pattern("1455257755424.png").targetOffset(-2,-20))
    RanTime()
    click(Pattern("1455257755424.png").targetOffset(-2,20))
    RanTime()


def PTZ_long():
    #PTZ_long
    hover(Pattern("1455257755424.png").targetOffset(-21,0))
    mouseDown(Button.LEFT)
    RanTime()
    mouseUp(Button.LEFT)
    hover(Pattern("1455257755424.png").targetOffset(20,1))
    mouseDown(Button.LEFT)
    RanTime()
    mouseUp(Button.LEFT)
    hover(Pattern("1455257755424.png").targetOffset(-2,-20))
    mouseDown(Button.LEFT)
    RanTime()
    mouseUp(Button.LEFT)
    hover(Pattern("1455257755424.png").targetOffset(-2,20))
    mouseDown(Button.LEFT)
    RanTime()
    mouseUp(Button.LEFT)


PTZ_short()
PTZ_long()
        
