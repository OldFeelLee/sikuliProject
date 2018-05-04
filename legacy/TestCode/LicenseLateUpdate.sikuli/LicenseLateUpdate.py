#App.open("C:/IDIS Solution Suite/Server/AdministrationService.exe")
import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)



       
while True:
    f= open("c:/a/LicenseTest.txt",'a')

    type("1460014672303.png","AdministrationService.exe start\n"+Key.ENTER)
    Time()
    f.write(s+"    Admin Start!\n")
    f.close()
    wait(60)
    while True:
        
        if exists(Pattern("1460020188018.png").similar(0.92)):
            f= open("c:/a/LicenseTest.txt",'a')
            Time()
            f.write(s+"    ImportDB...\n")
            f.close()
            wait(1)
        else:
            wait(50)
            break                        
        
    
    click(Pattern("1460014538553.png").similar(0.89).targetOffset(29,-18))
    f= open("c:/a/LicenseTest.txt",'a')
    Time()
    f.write(s+"    LogUpdate\n")
    f.close()
    wait(5)
    if exists(Pattern("1460014573256.png").similar(0.92)):
        f= open("c:/a/LicenseTest.txt",'a')
        Time()
        f.write(s+"    Valid License\n")
        f.close()
        click("1460014411613.png")
        keyDown(Key.CTRL)
        type("c")
        keyUp(Key.CTRL)
    else:
        f= open("c:/a/LicenseTest.txt",'a')
        Time()
        f.write(s+"    Invalid License\n")
        f.close()
        App.open("C:\IDIS Solution Suite\Client\G2ConfTool.exe")
        wait(3)
        type(Key.ENTER)        
        break
  