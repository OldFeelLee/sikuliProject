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
 
        else:
            f.write(s+"    "+statusStr+"    "+cntstr+" fail\n")
            f.close()            
def keyHold(key1,key2):
    keyDown(key1)
    type(key2)
    keyUp(key1)
    wait(2)

def type_Enter(str1):
    type(str1)
    wait(2)
    type(Key.ENTER)
    wait(2)
    
def Restart():
    global cnt
    global status

#    G2WindwosPath = 'C:\"IDIS Solution Suite"\Server\ServiceManager.exe '
#    strPath=str(G2WinidowsPath)
    keyHold(Key.WIN,"r")
    type_Enter("cmd")
    wait(2)
    for i in range(0,2,1):
        type_Enter("cd..")
        wait(2)
    type_Enter('cd "IDIS Solution Suite"\Server"')
    while True:
        if status == errorConst.Running:
            type_Enter('G2WindowService.exe stop')
            status = errorConst.Stopping
            wait(1)
            Log("G2WindowRestart",'a',errorConst.no_error)    
            wait(240)
            
        else:
            type_Enter('G2WindowService.exe start')
            status =errorConst.Running
            wait(1)
            Log("G2WindowRestart",'a',errorConst.no_error)    
            wait(240)
        cnt = cnt + 1
#    type_Enter("stop")

try :
    global cnt 
    global status
    status = errorConst.Running
    cnt = 0
    Log("CDM_RunTest",'w',errorConst.no_error)     
    Restart()
except FindFailed:
    Log("CDM_RunTest",'a',errorConst.error_1) 
