import datetime
import errorConst

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def Serial(filename):
    global setSerial 
    fr=open(filename+".txt").read()
    setSerial=str(fr)

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

def licenseDel():
    global status
    status = "License Delete"
    App.open("C:\sikuli\licenseDel.bat")    
    wait(5)

def if_exists_click(image1,time,image2):
    if exists(image1,time):
        click(image2)


    

def click_click(image1,image2):
    click(image1)
    click(image2)

def inputSerial():

    global setSerial
    setSerial=input(unicode("Serial Key를 입력하세요.","utf-8")) 

    
def OEM():
    oem=open("c:/sikuli/TestResult.txt").read(1)
    if oem == "I":
        App.open("C:\sikuli\IDIS_License.bat")    
    else:
        App.open("C:\sikuli\Type1_License.bat")  


def OEM_Fake():
    oem=open("c:/sikuli/TestResult.txt").read(1)
    if oem == "I":
        App.open("C:\sikuli\IDIS_License_Fake.bat")    
    else:
        App.open("C:\sikuli\Type1_License_Fake.bat")  
    

def LicenseTool():
    global status
#    inputSerial()

    status = "LicenseTool Run"
#    while not exists("1486615721253.png"):
#        wait(1)
#    click(Pattern("1486616289494.png").targetOffset(36,-2))
    OEM()
    
    status = "License auth_offline"    
    if_exists_click("1486608642625.png",600,Pattern("1486608659482.png").similar(0.90))     
    click_click("1489134203303.png","1489134248155.png")
    type(setSerial)
#    type("NH52CPOLX4BTRCGNARF3GZOZT6MLRW")
    click()    
    click("1489134350950.png")
    wait(1)
    type("D:\LT\license.ixl")
    click(Pattern("1489137332602.png").targetOffset(-5,-12))
    
    if_exists_click("1486609670798.png",60,"1486609034849-1.png")                   
    if_exists_click("1486608964816.png",5,"1486608983013.png")
    wait(20)
    OEM()
    status = "License auth confirm_offline"
    if_exists_click(Pattern("1489137826573.png").similar(0.80),60,"1486609034849-1.png")
    wait(5)
def LicenseTool_FakeConfirm():
    global status
    status = "License Active_Fake Confirm_offline"
    OEM_Fake()
    status = "License Fake_auth confirm_offline"

    if_exists_click("1489137951260.png",90,"1489137951260.png")
    click("1486609034849-1.png")
    wait(5)

def LicenseTool_Fake():
    global status

    status = "LicenseTool Run"    
    OEM_Fake()
    
    status = "License Fake_auth_offline"    
    if_exists_click("1486608642625.png",600,Pattern("1486608659482.png").similar(0.97))     
    click_click("1489134203303.png","1489134248155.png")
    type(setSerial)
    click()    
    click("1489134350950.png")
    wait(1)
    type("D:\LT\license.ixl")
    click(Pattern("1489137332602.png").targetOffset(-5,-12))
 
    if_exists_click(Pattern("1489138062076.png").similar(0.88),20,"1486609034849.png")  

try:
    licenseDel()
    Serial("serial")

    LicenseTool()
    Log("TestResult",'a',errorConst.no_error)

    LicenseTool_FakeConfirm()   
    Log("TestResult",'a',errorConst.no_error)    
    licenseDel()
    Log("TestResult",'a',errorConst.no_error)
    LicenseTool_Fake()
    Log("TestResult",'a',errorConst.no_error)
except FindFailed:
    Log("TestResult",'a',errorConst.error_1)     

 