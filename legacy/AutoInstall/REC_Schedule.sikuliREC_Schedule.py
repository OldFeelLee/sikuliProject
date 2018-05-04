import datetime
from guide import *

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def ScheduleEnter():
    App.focus("iNEX Setup")
    App.focus("IDIS Solution Suite Setup")
    click(Pattern("1484014793116.png").similar(0.67))
    click(Pattern("1484014813363.png").similar(0.82))
    wait(1)
    click(Pattern("1484014862626.png").similar(0.86).targetOffset(28,-16))
    click("1484014891148.png")


def ScheduleCondition(): #변수 정의
    global AddTime, AddCondition, AddAction, AddTarget
    AddTime = find("1484014960003.png")
    AddCondition = find("1484015958935.png")
    AddAction = find("1484015971069.png")
    AddTarget = find("1484015982266.png")

def Timelapse():
    doubleClick(AddTime)
    wait(1)
    doubleClick("1484015441456.png")
    doubleClick(AddCondition)
    wait(1)
    doubleClick("1455172850705.png")
    wait(1)
    doubleClick(AddAction)
    wait(1)
    doubleClick(Pattern("1455173093607.png").targetOffset(-1,-2))
    wait(1)
    doubleClick(AddTarget)
    wait(1)
    click(Pattern("1455173395787.png").targetOffset(-33,-1))
    wait(1)
    click(Pattern("1455173451451.png").targetOffset(57,14))
    wait(1)
#    click(Pattern("1455173491577.png").targetOffset(-47,3))
#    wait(30)


def MotionEventREC():  #모션 이벤트 녹화설정   
    click(Pattern("1484015497155.png").exact().targetOffset(128,16))
    doubleClick(AddCondition)
    wait(1)
    doubleClick("1455179326544.png")
    wait(1)
    doubleClick(AddAction)
    wait(1)
    click(Pattern("1455173093607-1.png").targetOffset(-1,-2))
    wait(1)
    type("1455180983505.png","5"+Key.ENTER)
    wait(1)
    click(Pattern("1484016246363.png").similar(0.86))
    doubleClick(AddTarget)
    
    wait(1)
    click(Pattern("1455173451451-1.png").targetOffset(57,14))
    wait(1)
    click(Pattern("1455173491577-1.png").targetOffset(-47,3))
    wait(1)


try:    
    ScheduleEnter()
    ScheduleCondition()
    Timelapse()
    MotionEventREC()
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    REC Scehdule complete!\n")
    f.close()
except FindFailed:

    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    REC Scehdule fail!\n")
    f.close()