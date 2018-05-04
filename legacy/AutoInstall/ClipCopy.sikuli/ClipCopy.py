import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def success():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    ClipCopy complete!\n")
    f.close()  

def failed():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    "+status+" fail!\n")
    f.close()  


try:
    global status
    status = "ClipCopy_device_drag&drop"
    runScript("C:\sikuli\script\AutoInstall\OEM_Client")    
    click("1484027094439.png")
    runScript("C:\sikuli\script\AutoInstall\Client_Device_DragDrop")
    status = "REC_TimeTable"
    if exists("1484027262854.png",600):
        status = "REC_ClipCopy"
    click(Pattern("1484027311485.png").similar(0.97))
    click("1484027347052.png")
    click(Pattern("1484027382166.png").similar(0.94).targetOffset(-15,-9))
    click(Pattern("1484027382166.png").similar(0.94).targetOffset(5,-6))
    click(Pattern("1484027445851.png").similar(0.92))
    click("1484027480963.png")
    while not exists("1484027528160.png"):
        wait(1)
    click(Pattern("1484027549980.png").similar(0.95))
    while not exists("1484027583202.png"):
        wait(1)
    click(Pattern("1484027612596.png").targetOffset(127,45))
    click(Pattern("1484027640260.png").targetOffset(45,0))
    Time()
    success()

except FindFailed:
    Time()
    failed()
    