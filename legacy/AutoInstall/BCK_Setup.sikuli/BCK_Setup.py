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

def click_click(image1,image2):
    click(image1)
    click(image2)       

def click_click_click(image1,image2,image3):
    click(image1)
    click(image2)
    click(image3)

def waitVanish_click(image1,image2):
    while not exists(image1):
        wait(1)
    click(image2)

def BCK_Setup():
    global status
    status = "BackupSetup Enter"
    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")
    click("1484028992465.png")
    wait(1)
    doubleClick("1484029034988.png")
    waitVanish_click("1486438226974.png","1484029119976.png")
    status = "BackupSetup_SiteSetup"
    click_click("1484029150212.png",Pattern("1484029173037.png").targetOffset(-38,-2))
    click_click(Pattern("1484029203546.png").exact().targetOffset(-57,1),Pattern("1484029240476.png").targetOffset(-41,-1))    
    waitVanish_click(Pattern("1484029277359.png").targetOffset(25,30),Pattern("1484029277359.png").targetOffset(25,30))

    status = "BackupSetup_TimeSetup"
    click_click(Pattern("1484029349565.png").targetOffset(167,73),Pattern("1484029382020.png").targetOffset(-53,-13))
    doubleClick("1484029416250.png")
    click(Pattern("1484029438876.png").targetOffset(-35,1))
    status = "BackupSetup_Target"
    click_click_click(Pattern("1484029463734.png").targetOffset(171,31),Pattern("1484029491300.png").similar(0.96).targetOffset(-33,-35),Pattern("1484029529925.png").targetOffset(-47,2))   
    status = "BackupSetup_Storage"
    click_click(Pattern("1484029574945.png").targetOffset(167,30),"1484029597521.png")
    wait(1)
    type(Key.DOWN)
    type(Key.DOWN)
    click_click_click("1484012731288.png","1484029731994.png","1484030159947.png")
    waitVanish_click("1484030722944.png","1484030610390.png")   
    click("1484030265938.png")

try:

    BCK_Setup()
    Log("TestResult",'a',errorConst.no_error)

except FindFailed:
    Log("TestResult",'a',errorConst.error_1)  
    