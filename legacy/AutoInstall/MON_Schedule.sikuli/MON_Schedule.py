import datetime
import errorConst

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


def ScheduleCondition(): #변수 정의
    global AddTime, AddCondition, AddAction, AddTarget
    AddTime = find("1484014960003.png")
    AddCondition = find("1484015958935.png")
    AddAction = find("1484015971069.png")
    AddTarget = find("1484015982266.png")


def untilShow_click(image,image2):
    while not exists(image):
        click(image2)
        wait(1)

def click_click(image1, image2):
    click(image1)
    click(image2)
        
def click_click_click(image1,image2,image3):
    click(image1)
    click(image2)
    click(image3)

def wait_doubleClick(image1):
    wait(1)
    doubleClick(image1)

def EVT_ScheduleEnter():
#    App.focus("iNEX Setup")
    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
    global status
    status = "EVT Schedule Enter"
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")
    click_click(Pattern("1484018041097.png").similar(0.81),Pattern("1484014813363.png").similar(0.82))   
    
    status = "EVT Schedule setup"    
    ScheduleCondition()
    wait_doubleClick(AddTime)
    wait_doubleClick("1484018242397.png")
    wait_doubleClick(AddCondition)
    click("1487127980338.png")
    type("TextInEvent")
    click(Pattern("1487128040723.png").similar(0.85).targetOffset(-13,14))
    untilShow_click("1487127567274.png",Pattern("1487127578481.png").similar(0.93))
    click_click_click(Pattern("1487129162025.png").targetOffset(-31,0),"1487128096964.png",Pattern("1487128118474.png").similar(0.85))
#    doubleClick("1484018292430.png")

    wait_doubleClick(AddAction)
    click_click_click("1484018340088.png","1484018352228.png",Pattern("1484025667318.png").exact().targetOffset(-2,14))
    wait_doubleClick(AddTarget)
    click_click_click(Pattern("1484018449712.png").exact().targetOffset(-45,-1),"1484018481247.png","1484018494731.png")

try:
    EVT_ScheduleEnter()    
    Log("TestResult",'a',errorConst.no_error)
except FindFailed:
    Log("TestResult",'a',errorConst.error_1)     

 