import datetime
import random
import string
import errorConst

def RanTime():    #random 시간
    ran = "".join([random.choice(string.digits)])
    s=int(ran)
    wait(s)

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
        
def ConfLogIn():
    global status
    status = "ConfTool LogIn"
    while exists(Pattern("1516587526564.png").targetOffset(26,124)):        
        exists_click(Pattern("1516587526564.png").targetOffset(26,124))
        wait(5)

    ConfToolLoading()  

def ConfToolLoading(): #ConfTool에 설정 적용 wait
    while not exists("1484098904026.png"):
        click("1484098830091.png")
        type(Key.ENTER)
        wait(1)    



def DBExport():
    global status
    status = "DBExport Setting"
    click("1486459824465.png")
    click("1486459847185.png")
    type(Key.ENTER)

    if exists("1486516622854.png",600):
        click("1486516654143.png")
        
        type(Pattern("1486516726920.png").similar(0.90),"ExportTest.iexp"+Key.ENTER)
        if exists(Pattern("1517384078551.png").targetOffset(45,32),30):
            click(Pattern("1517384078551.png").targetOffset(45,32))
        status = "DBExporting"
    if exists(Pattern("1486516821324.png").similar(0.77),600):
        type(Key.ENTER)
    wait(1)
    Log("DBExport_02.05-02.12",'a',errorConst.no_error)
    wait(5)
try:
    global cnt 
    global status
    status = "Init"
    cnt = 0
    Log("DBExport_02.05-02.12",'a',errorConst.no_error)
    while True : 
        DBExport()
        Time()
        date_temp=list(s)[8:10]
        tempInt = [int(x) for x in date_temp]
        if tempInt[0] >=1 and tempInt[1] >=2:
            break
    
except FindFailed:
    Log("DBExport_02.05-02.12",'a',errorConst.error_1) 
    App.open("C:\IDIS Solution Suite\Client\G2ConfTool.exe")
    wait(5)
    App.focus("C:\IDIS Solution Suite\Client\G2ConfTool.exe")
    wait(1)
    if exists(Pattern("1516587526564.png").targetOffset(26,124),30):
        ConfLogIn()    
run("C:\sikuli\gr1mailtest_export.bat")
Time()
date_temp=list(s)[8:10]
tempInt = [int(x) for x in date_temp]
if tempInt[0] >=1 and tempInt[1] >=2:
    runScript("C:\sikuli\script\DBImport.sikuli")
else:
    runScript("C:\sikuli\script\DBExport.sikuli")