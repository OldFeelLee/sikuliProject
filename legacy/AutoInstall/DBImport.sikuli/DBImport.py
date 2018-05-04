import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def success():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    ServiceDB Import complete!\n")
    f.close()  

def failed():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    "+status+" fail!\n")
    f.close() 

def DBImport():
    global status
    status = "DBImport Setting"
    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")
    click("1486459824465.png")
    click("1486520432534.png")
    type("12345678"+Key.ENTER)
    if exists("1486520506917.png",100):
        click("1486520506917.png")
    if exists("1486520977451.png",10):
        click("1486520995446.png")
        type("1486521012624.png","ExportTest.iexp"+Key.ENTER)
        wait(1)
        type(Key.ENTER)
    while exists(Pattern("1486521497087.png").similar(0.95)):
        wait(1)
try:

    DBImport()    
    Time()
    success()

except FindFailed:
    Time()
    failed()
