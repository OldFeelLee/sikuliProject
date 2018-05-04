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

def Client_EventManager():
    global status
    status = "Client Run"
    runScript("C:\sikuli\script\AutoInstall\OEM_Client")
    status = "Client Init"
    runScript("C:\sikuli\script\AutoInstall\Client_Loading")
    runScript("C:\sikuli\script\AutoInstall\PosSimRun")
    runScript("C:\sikuli\script\AutoInstall\OEM_Client")
        
    if exists("1487129357522.png",30):
        click("1487129357522.png")
    else:    
        click("1487126363757.png")
    status = "ActionAck" 
    if not exists(Pattern("1487126383051.png").similar(0.91)):

        Log("TestResult",'a',errorConst.no_error)



    else:
        Log("TestResult",'a',errorConst.error_1)    

    click(Pattern("1487128650079.png").targetOffset(30,-17))   

try:

    Client_EventManager()               

except FindFailed:
    Log("TestResult",'a',errorConst.error_1)
