import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def success():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    PosSim Run complete!\n")
    f.close()  

def failed():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    "+status+" fail!\n")
    f.close() 


def PosSimRun():
    global status
    status = "PosSimApp Run"
    if App.open("C:\sikuli\PosSim.exe"):
        status = "PosSim setting"
        doubleClick(Pattern("1486515396083.png").similar(0.79).targetOffset(-43,19))
        type("10.0.127.222")
        click("1486515453310.png")
        wait(1)
        doubleClick(Pattern("1486515552168.png").targetOffset(8,-2))
        type("30")
        click("1486515615428.png")

try:
    PosSimRun()
    Time()
    success()

except FindFailed:
    Time()
    failed()
