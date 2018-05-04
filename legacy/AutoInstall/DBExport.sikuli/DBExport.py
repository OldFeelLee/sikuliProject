from sikuli import errorConst
import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def success():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    ServiceDB Export complete!\n")
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


def DBExport():
    global status
    status = "DBExport Setting"
    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")
    click("1486459824465.png")
    click("1486459847185.png")
    type("12345678"+Key.ENTER)

    if exists("1486516622854.png",600):
        click("1486516654143.png")
        
        type(Pattern("1486516726920.png").similar(0.90),"ExportTest"+Key.ENTER)
        status = "DBExporting"
    if exists(Pattern("1486516821324.png").similar(0.92),600):
        type(Key.ENTER)


try:

    DBExport()    
    Time()
    success()
    exit(errorConst.no_error)
except FindFailed:
    Time()
    failed()
    exit(errorConst.error_1)