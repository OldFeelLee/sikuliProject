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

def if_exists_click(image1,time,image2):
    if exists(image1,time):
        click(image2)


def OEM():
    oem=open("c:/sikuli/TestResult.txt").read(1)
    if oem == "I":
        App.open("C:\sikuli\IDIS_License.bat")    
    else:
        App.open("C:\sikuli\Type1_License.bat")  

def LicenseTool():
    global status
    status = "LicenseTool Run"
#    while not exists("1486615721253.png"):
#        wait(1)
#    click(Pattern("1486616289494.png").targetOffset(36,-2))
    OEM()
    
    status = "License auth"    
    if_exists_click("1486608642625.png",600,Pattern("1486608659482.png").similar(0.90))     
    click()
    type("NH52CPOLX4BTRCGNARF3GZOZT6MLRW")
    click()    
    if_exists_click("1486609670798.png",60,"1486609034849.png")                   
    if_exists_click("1486608964816.png",5,"1486608983013.png")
                                                                
try:
    LicenseTool()
    Log("TestResult",'a',errorConst.no_error)
except FindFailed:
    Log("TestResult",'a',errorConst.error_1)     

 