import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def success():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    TextInSetup complete!\n")
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
   
def TextInSetup():
    global status
    status = "DeviceEdit Enter"
    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")

    click("1486445092380.png")
    doubleClick(Pattern("1486445117908.png").targetOffset(4,0))
    if exists("1486445236275.png",600):
        click("1486445148858.png")

    doubleClick("1486445304148.png")
    if exists("1486445366073.png",600):
        click(Pattern("1486445366073.png").targetOffset(-21,1))
    click(Pattern("1486446103161.png").targetOffset(-37,-1))
    type(Pattern("1486446141630.png").exact().targetOffset(16,0),"~~")
    type(Pattern("1486446176751.png").exact().targetOffset(25,0),"[]")
    click("1486446219762.png")
    click("1486446243775.png")

try:
    TextInSetup()
    Time()
    success()    

except FindFailed:
    Time()
    failed()

    