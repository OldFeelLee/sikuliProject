import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)


def Log(filename,mode,flag):
    global flagCheck
    flagCheck=0
    f=open(filename+".txt",mode)
    Time()
    if flagCheck==int(flag):
        f.write(s+"    "+status+" pass\n")
        f.close()
    else:
        f.write(s+"    "+status+" fail\n")
        f.close()       

def ScheduleEnter():
    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")     
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")
    global status
    status = "REC ScheduleEnter"

    click("1486436377626.png")
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
    global status
    status = "Timelapse Schedule"
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
    global status
    status = "MotionEvent Schedule"
    click(Pattern("1484015497155.png").similar(0.87).targetOffset(128,16))
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
    
  
    click(Pattern("1455173451451-1.png").targetOffset(57,14))
    wait(1)
#    click(Pattern("1455173491577-1.png").targetOffset(-47,3))
#    wait(1)

def TextInEventREC():  #TextIn 이벤트 녹화설정   
    global status
    status = "TextInEventREC Schedule"
    click(Pattern("1484015497155.png").similar(0.86).targetOffset(128,16))
    doubleClick(AddCondition)
    wait(1)
    click("1486446856819.png")
    type("TextIn")
    click(Pattern("1486446959027.png").similar(0.96).targetOffset(-11,17))
    while not exists(Pattern("1486447076069.png").similar(0.85),1):
        click(Pattern("1486448536969.png").similar(0.93).targetOffset(-38,-20))
        wait(1)
    click(Pattern("1486447138978.png").targetOffset(-33,0))
    click("1486447173897.png")
    click("1486447192906.png")  
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
    TextInEventREC()
    Log("TestResult",'a',errorConst.no_error)

except FindFailed:
    Log("TestResult",'a',errorConst.error_1)  
