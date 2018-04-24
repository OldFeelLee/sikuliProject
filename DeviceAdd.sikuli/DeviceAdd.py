import datetime
import string
import errorConst
import currentTime
import fileLog

def Time():    #get current time
    global s
    today = datetime.datetime.now()
    s = str(today)

def Log(filename,mode,flag):     #result log
    global cnt    

    cntstr =str(cnt)
#    statusStr = str(status) 
    f=open(filename+".txt",mode)
    currentTime.Time()
    if cnt==0:
        f.write(currentTime.s+"    "+" start\n")
        f.close()
        cnt = cnt + 1
    else:
        if flag==errorConst.no_error: 
            f.write(currentTime.s+"    "+"    "+cntstr+" pass\n")
            f.close()
            cnt = cnt + 1
        else:
            f.write(currentTime.s+"    "+"    "+cntstr+" fail\n")
            f.close()
def keyDownUp(key1):
    keyDown(key1)
    wait(5)
    keyUp(key1)


            
def DeviceScan():
    while True:
        click(Pattern("1519378094663.png").exact().targetOffset(16,10))
        fileLog.Log("DeviceAdd",'a',errorConst.no_error) 
        keyDown(Key.SHIFT+Key.CTRL+Key.ALT)
        wait(5)
        click(Pattern("1519378179664.png").similar(0.87))
        keyUp(Key.SHIFT+Key.CTRL+Key.ALT)
        for a in range(0,7,1):
            type(Key.TAB)
            wait(1)
        type("100")
        wait(1)
        type(Key.ENTER)
        wait(30)
        click("1519378732715.png")
        wait(120)
        click("1519378767672.png")
        wait(2)
        keyDown(Key.CTRL+"a")
        wait(2)
        keyUp(Key.CTRL+"a")
        wait(2)
        type(Key.DELETE)
        click("1519378879062.png")  
        wait(60)
#        fileLog.Log("DeviceAdd",'a',errorConst.no_error) 
try :
    global cnt 
    global status
    fileLog.cnt = 0
    fileLog.status = None
    status = errorConst.Running
#    cnt = 0
    fileLog.Log("DeviceAdd",'a',errorConst.no_error)     
    DeviceScan()
except FindFailed:
    fileLog.Log("DeviceAdd",'a',errorConst.error_1) 
