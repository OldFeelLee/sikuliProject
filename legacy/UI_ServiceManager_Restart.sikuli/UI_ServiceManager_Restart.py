import datetime
import random
import string

def Random():
    ran = "".join([random.choice(string.digits)])
    s = int(ran)
    wait(s)
    
def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)
cnt = 0





while True:
    Random()
#    App.open("C:\IDIS Solution Suite\Server\ServiceManager.exe") 
    App.open("C:\iNEX\Server\ServiceManager.exe")
    wait(2)
    if cnt == 100:
        break
    while True:    
        if exists(Pattern("1468488104875.png").similar(0.87)):
            f= open("d:/a/261_ServiceManager.txt",'a')
            Time()
            f.write(s+"    Success!\n")
            f.close()
            
            click(Pattern("1468488141231.png").similar(0.73).targetOffset(283,-9))
            wait(1)
            click(Pattern("1468488174351.png").targetOffset(37,39))
            wait(1)
            
#            App.close("servicemanager.exe")
            break
        else:
            wait(1)
            cnt= cnt+1
            if cnt==100:                
                f= open("d:/a/ServiceManager_.txt",'a')
                Time()
                f.write(s+"    Fail!\n")
                f.close()
                break
