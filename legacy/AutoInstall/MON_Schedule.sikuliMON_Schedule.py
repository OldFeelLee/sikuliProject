import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def ScheduleCondition(): #변수 정의
    global AddTime, AddCondition, AddAction, AddTarget
    AddTime = find("1484014960003.png")
    AddCondition = find("1484015958935.png")
    AddAction = find("1484015971069.png")
    AddTarget = find("1484015982266.png")

def EVT_ScheduleEnter():
    App.focus("iNEX Setup")
    App.focus("IDIS Solution Suite Setup")
    click(Pattern("1484018041097.png").similar(0.81))
    click(Pattern("1484014813363.png").similar(0.82))
    wait(1)
    ScheduleCondition()
    doubleClick(AddTime)
    wait(1)
    doubleClick("1484018242397.png")
    doubleClick(AddCondition)
    doubleClick("1484018292430.png")
    doubleClick(AddAction)
    click("1484018340088.png")
    click("1484018352228.png")
    click(Pattern("1484025667318.png").exact().targetOffset(-2,14))
    wait(1)
    doubleClick(AddTarget)
    click(Pattern("1484018449712.png").targetOffset(-45,-1))
    click("1484018481247.png")
    click("1484018494731.png")

try:
    EVT_ScheduleEnter()
    
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    MON Scehdule complete!\n")
    f.close()  
  
except FindFailed:
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    MON Scehdule fail!\n")
    f.close()    
 