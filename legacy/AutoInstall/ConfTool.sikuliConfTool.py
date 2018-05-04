import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def success():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    Device add complete!\n")
    f.close()  
#    run("C:\sikuli\gr1mailtest.bat")

def failed():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    Device add fail!\n")    
#    f.write(s+"    Device add fail!\n")
    f.close()  

def Loading(): #ConfTool에 설정 적용 wait
    while not exists("1484098904026.png"):
        click("1484098830091.png")
        wait(1)    

def ConfToolStart():    #ConfTool login 및 device tab 이동

    if exists("1484097196560.png",FOREVER): 
        
        type(Pattern("1484097229104.png").targetOffset(8,13),"12345678"+Key.ENTER)
    while exists("1484103078600.png"):
        doubleClick(Pattern("1484097229104.png").targetOffset(8,13))
        type(Key.DELETE)
        type(Pattern("1484097229104.png").targetOffset(8,13),"12345678"+Key.ENTER)
        
    if exists("1455775002971.png",FOREVER):    
        click("1455775002971.png")
        
    Loading()
    click("1454380361915.png")


def ScanMode(): # Scan mode 진입 및 IP Scan 선택

    if exists("1484099067019.png",FOREVER):
        click(Pattern("1454380412860.png").similar(0.94).targetOffset(108,-25))        
    if exists(Pattern("1454380987835.png").exact()):
        click(Pattern("1454380525571.png").similar(0.91))
        wait(1)
        click(Pattern("1454380563437.png").similar(0.84).targetOffset(-70,-1))
        wait(1)   
        ip()
        auto()
        Loading()

    else:   
        ip()
        auto()
        Loading()


def ip(): # ip 입력    
    doubleClick(Pattern("1454380633509.png").targetOffset(-36,0))
    type("10.0.127.114")
    wait(1)
    
def auto(): # DeviceScan 및 ID/PW 입력
    click("1454380656889.png")
    while True:
        hover("1484101583287.png")
        if exists(Pattern("1454380656889.png").similar(0.94),FOREVER): 
            
            if exists(Pattern("1454381253425.png").exact().targetOffset(8,-10),1):
                click(Pattern("1454381253425.png").exact().targetOffset(8,-10))
                break
            else:                
                click("1454380656889.png")

    click("1454381290995.png")

    type("admin"+Key.TAB) #ID!
    wait(1)
    type("pylon") # PW
    wait(1)
    click("1461749295384.png")
    wait(1)
    click("1455166085100.png")



try:
    ConfToolStart()
    ScanMode()
    Time()
    success()
except FindFailed:
    Time()
    failed()
    
#print a