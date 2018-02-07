import datetime
import errorConst

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)
def Log(filename,mode,flag):
    global flagCheck
    global cnt
    statusStr=str(status)
    cntstr=str(cnt)

    flagCheck=0
    f=open(filename+".txt",mode)
    Time()
    if cnt ==0:
        f.write(s+"    "+" start\n")
        f.close()
        cnt = cnt + 1
    else:
#        if flagCheck==int(flag): 
        if int(flag) == errorConst.no_error:
            f.write(s+"    "+cntstr+"    "+deviceNum+"\n")
            f.close()
            wait(2)
        else:
            f.write(s+"    "+"    "+cntstr+"    "+deviceNum+"    "+statusStr+" fail\n")
            f.close()
def waitClick(img1):
    wait(img1,300)
    click(img1)
    wait(2)

def exists_click(img,time):
    wait(1)
    if exists(img,time):
        wait(1)
        click(img)
    wait(2) 
def type_type(str1):
    wait(1)
    type(Key.F6)
    wait(1)
    type("http://10.0.127."+str1+"/admin/maintenance.shtml?id=41")
    type(Key.ENTER)
    wait(2)
#AddressFocus "1515119506911.png"

def refresh():
    wait(1)
    type(Key.F6+"http://10.0.127."+ipArr[i])
    type(Key.ENTER)
    wait(2)

def tabMove():
    keyDown(Key.CTRL)
    type(Key.TAB)
    keyUp(Key.CTRL)
    wait(2)

def setupMove():
    global status
    status = "setupMove"
    wait(2)
    exists_click("1515128420974.png",5)    
    type_type(ipArr[i])
#    hover(Pattern("1515147248753.png").similar(0.84))
    wait(2)
    exists_click("1515128420974.png",5)  
    wait(2)


def Restart():
    global cnt
    global status
    global deviceNum
    global ipArr
    global i
    global status
  #  m1113 = find("1515053209298.png") 
#    m1114 = "1515119386897.png"
#    m1124 = "1515119692140.png"
#    m5014 = "1515119867730.png"
#    q1604 = "1515120098650.png"
#    modelArr = ["m1113","m1113","m1113","m1113","m1113","m1114","m1114","m1124","m5014","q1604"]
#    ipArr = ["57","52","51","53","56","67","64","81","180","189"]    
    ipArr = ["57","52","51","53","56","67","64","81","189","199"]
    while True:
        for i in range(0,10,1):
            device = i
            deviceNum = str(device)
            exists_click("1515128420974.png",5)   
            if exists("1515119506911.png",360):
                setupMove()
                status = "restart page"
                if exists(Pattern("1515052974538.png").similar(0.85).targetOffset(-28,-1),360):
                    click(Pattern("1515052974538.png").similar(0.85).targetOffset(-28,-1))
                    waitClick("1515052998986.png")
                    tabMove()
                else:
                    status = "restart page fail_tabMove"  
                    refresh()
                    tabMove()
            else:
                status = "view page fail_tabMove" 
                exists_click("1515128420974.png",5) 
                refresh()
                tabMove()
              
            Log("AxisRestart_multi_01.29-02.05",'a',errorConst.no_error)
#            cnt = cnt + 1
            status = "login window"



#            if exists("1515141255698.png")
#            if exists("1515133309658.png",5):
#                type(Key.F5)
#                wait(10)
        exists_click("1515128420974.png",5)   
        while not exists("1515053209298.png",600):
            wait(1)
            type(Key.F6)
            wait(1)
            type("http://10.0.127."+ipArr[0])
            type(Key.ENTER)
            wait(2)
            exists_click("1515128420974.png",10) 
        cnt = cnt+1
#        wait("1515053209298.png",FOREVER)
try:
    global cnt
    global status
    status = "temp"
    cnt = 0
    Log("AxisRestart_multi_01.29-02.05",'a',errorConst.no_error)
    Restart()

except FindFailed:
    Log("AxisRestart_multi_01.29-02.05",'a',errorConst.error_1)     
#    Restart()
run("d:\sikuli\gr1mailtest.bat")
runScript("D:\sikuli\script\AxisRestart_Multi.sikuli")