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
        
        type(Pattern("1486516726920.png").similar(0.90),"ExportTest"+Key.ENTER)
        status = "DBExporting"
    if exists(Pattern("1486516821324.png").similar(0.77),600):
        type(Key.ENTER)
    wait(1)
    Log("DBExport",'a',errorConst.no_error)
    wait(5)
try:
    global cnt 


    cnt = 0
    Log("DBExport",'a',errorConst.no_error)
    while True : 
        DBExport()    
    
except FindFailed:
    Log("DBExport",'a',errorConst.error_1) 
run("C:\sikuli\gr1mailtest.bat")