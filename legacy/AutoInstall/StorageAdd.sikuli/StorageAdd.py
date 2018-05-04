import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def success():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    Storage add complete!\n")
    f.close()  

def failed():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    "+status+" fail!\n")
    f.close()  

def ConfToolLoading(): #ConfTool에 설정 적용 wait
    while not exists("1484098904026.png"):
        click("1484098830091.png")
        type(Key.ENTER)
        wait(1)    

try:
    global status
    status = "Storage add"
    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")
    click("1486435609397.png")
    doubleClick("1486435636761.png")
    click(Pattern("1486435660958.png").similar(0.91))
    click("1486435688200.png")
    wait(1)
    type(Key.DOWN)
    type(Key.DOWN)
    click("1486435734546.png")
    click("1486435751705.png")
    click("1486435776134.png")
    while not exists(Pattern("1486435856199.png").similar(0.90)):
        wait(1)
    click("1486435894307.png")    
    Time()
    success()
    
except FindFailed:
    Time()
    failed()
    