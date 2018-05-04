import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def success():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    BackupSearch complete!\n")
    f.close()  

def failed():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    "+status+" fail!\n")
    f.close() 

def BackupSearch():
    global status
    status = "BackupSearch_device_drag&drop"
    runScript("C:\sikuli\script\AutoInstall\OEM_Client")
    runScript("C:\sikuli\script\AutoInstall\Client_Loading")
    if exists("1486540947549.png",1):
        click("1486540947549.png")
    else:
        click("1486540543012.png")
    runScript("C:\sikuli\script\AutoInstall\Client_Device_DragDrop")    
    status = "Backup_TimeTable"
    if exists("1484027262854.png",600):
        status = "Backup_ClipCopy"
    runScript("C:\sikuli\script\AutoInstall\Client_ClipCopy")     


try:
    BackupSearch()
    runScript("C:\sikuli\script\AutoInstall\PaneClear")
    Time()
    success()

except FindFailed:
    Time()
    failed()
    
    
    