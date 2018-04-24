import datetime
import random
import string
import errorConst

def Time():    #get current time
    global s
    today = datetime.datetime.now()
    s = str(today)

def Log(filename,mode,flag):     #result log
    global cnt    

    cntstr =str(cnt)
    statusStr = str(status) 
    f=open(filename+".txt",mode)
    Time()
    if cnt==0:
        f.write(s+"    "+" start\n")
        f.close()
        cnt = cnt + 1
    else:
        if flag==errorConst.no_error: 
            f.write(s+"    "+statusStr+"    "+cntstr+" pass\n")
            f.close()
            cnt = cnt + 1
        else:
            f.write(s+"    "+statusStr+"    "+cntstr+" fail\n")
            f.close()     

def exists_click(img):
    if exists(img):
        click(img)
        wait(1)
            
def ConfToolLoading(): #ConfTool에 설정 적용 wait
    global status 
    status = "ConfTool Loading"
    while not exists("1484098904026.png"):
        click("1484098830091.png")
        type(Key.ENTER)
        wait(1)  

def serviceStatus(): # service online check
    global status
    status = "Service Status"
    while not exists(Pattern("1516758311046.png").similar(0.93)):
        wait(1)


def ConfLogIn():
    global status
    status = "ConfTool LogIn"
    while exists(Pattern("1516587526564.png").targetOffset(26,124)):        
        exists_click(Pattern("1516587526564.png").targetOffset(26,124))
        wait(5)

    ConfToolLoading()    

def DBImport():
    global status
    status = "DBImport Setting"
#    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
#    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")

    click("1486459824465.png")
    serviceStatus()    
    click("1486520432534.png")
    type(Key.ENTER)
    if exists("1486520506917.png",100):
        click("1486520506917.png")
    if exists("1486520977451.png",10):
        click("1486520995446.png")
        type("1486521012624.png","ExportTest.iexp"+Key.ENTER)
        wait(5)
        type(Pattern("1486521497087.png").similar(0.91).targetOffset(-34,3),Key.ENTER)
    while exists(Pattern("1486521497087.png").similar(0.91)):
        wait(1)
    wait(300)
try:
    global cnt 
    global status
    status = "init"
    cnt = 0
    Log("DBImport_02.12-02-19",'a',errorConst.no_error)
    while True : 
        DBImport() 
        ConfLogIn()
        Log("DBImport_02.12-02-19",'a',errorConst.no_error)
except FindFailed:
    Log("DBImport_02.12-02-19",'a',errorConst.error_1) 
    App.open("C:\IDIS Solution Suite\Client\G2ConfTool.exe")
    ConfLogIn()
run("C:\sikuli\gr1mailtest_import.bat")
Time()
date_temp=list(s)[8:10]
tempInt = [int(x) for x in date_temp]
if tempInt[0] >=1 and tempInt[1] >=2:
    runScript("C:\sikuli\script\DBImport.sikuli")
else:
    runScript("C:\sikuli\script\DBExport.sikuli")