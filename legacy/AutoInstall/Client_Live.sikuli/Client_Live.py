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


def Live():
    global status
    runScript("C:\sikuli\script\AutoInstall\OEM_Client")      

    status = "Layout Change"
    runScript("C:\sikuli\script\AutoInstall\Client_Loading")
    click("1487048913641.png")
    DeviceTree()    

def DeviceTree():
    global status

    runScript("C:\sikuli\script\AutoInstall\Client_Device_DragDrop") 
    if exists("1484032115779.png",10):
        status = "Streaming_Device NotConnected"
        Log("TestResult",'a',errorConst.error_1)
    elif exists("1486536412424.png",10):
        status = "no server runnng or unknown"
        Log("TestResult",'a',errorConst.error_1)    
    else:
        status = "Live"
        Log("TestResult",'a',errorConst.no_error)                
    runScript("C:\sikuli\script\AutoInstall\PaneClear")                     

try:
    Live()  

except FindFailed:
    Log("TestResult",'a',errorConst.error_1)     