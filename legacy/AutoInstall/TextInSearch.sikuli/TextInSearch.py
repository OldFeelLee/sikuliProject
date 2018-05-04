
import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def success():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    TextInSearch complete!\n")
    f.close()  

def failed():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    "+status+" fail!\n")
    f.close() 
    

def TextInSearch():
    global status
    status = "TextIn_device_drag&drop"
    runScript("C:\sikuli\script\AutoInstall\OEM_Client")
    runScript("C:\sikuli\script\AutoInstall\Client_Loading")
    click("1484027094439.png")
    runScript("C:\sikuli\script\AutoInstall\Client_Device_DragDrop")
    if exists("1484027262854.png",600):
        status = "TextIn_TimeTable"

try:

    TextInSearch()
    runScript("C:\sikuli\script\AutoInstall\PaneClear")     
    Time()
    success()
except FindFailed:
    Time()
    failed()
    