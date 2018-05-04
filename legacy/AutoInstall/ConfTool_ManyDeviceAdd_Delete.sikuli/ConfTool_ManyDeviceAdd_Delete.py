import datetime
import errorConst

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)
    
def Log(filename,mode,flag):
    global flagCheck
    flagCheck=0
    f=open(filename+".txt",mode)
    Time()
    if flagCheck==int(flag):
        f.write(s+"    "+status+" pass\n")
        f.close()
    else:
        f.write(s+"    "+status+" fail\n")
        f.close()
        

def Vanish_click(image):

    try:
        while exists(image, 10):
            type(image,Key.TAB+"12345678"+Key.ENTER)          
            wait(1)
    except:
        wait(1)
        
def ConfTool_ManyDeviceAdd():
    global status
    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
#    Vanish_click("1486617801030.png")           
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")
    status = "ManyDeviceAdd"
    click("1487050858920.png")
    click(Pattern("1487050882738.png").similar(0.95).targetOffset(62,-4))
    if not exists("1487053359526.png"):
        click(Pattern("1487053415818.png").targetOffset(-2,19))
        type(Key.HOME)
    keyDown(Key.SHIFT+Key.CTRL+Key.ALT)
    click("1487050915988.png")
    keyUp(Key.SHIFT+Key.CTRL+Key.ALT)
    doubleClick(Pattern("1487051108918.png").exact())
    type("1000"+Key.ENTER)
    click("1487051183723.png")
    while not exists("1487051451730.png"):
        click("1487051183723.png")
        wait(1)    

    
def ConfTool_ManyDeviceDelete():
    global status
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")
    status = "ManyDeviceDelete"    
    click("1487050858920.png")
    click("1487051671208.png")
    keyDown(Key.CTRL+"a")
    keyUp(Key.CTRL+"a")
    type(Key.DELETE)
    click(Pattern("1487051765657.png").targetOffset(-45,-3))
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")
    
try :
    ConfTool_ManyDeviceAdd()
    ConfTool_ManyDeviceDelete()
    Log("TestResult",'a',errorConst.no_error)
except FindFailed:
    Log("TestResult",'a',errorConst.error_1)