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

def Client_RECIcon():
    global status
    status = "Client focus"
    runScript("C:\sikuli\script\AutoInstall\OEM_Client")
    status = "Client Init"
    runScript("C:\sikuli\script\AutoInstall\Client_Loading")
    click("1487041638105.png")
    status = "Device DragDrop"
    runScript("C:\sikuli\script\AutoInstall\Client_Device_DragDrop")
    status = "REC_Icon"
    if not exists(Pattern("1487041725635.png").similar(0.90)):
        Log("TestResult",'a',errorConst.error_1)
        
    else:
        status = "PaneClear"
        runScript("C:\sikuli\script\AutoInstall\PaneClear")                    
        Log("TestResult",'a',errorConst.no_error)      
        
try:          
    Client_RECIcon()
    

except FindFailed:
    Log("TestResult",'a',errorConst.error_1)
