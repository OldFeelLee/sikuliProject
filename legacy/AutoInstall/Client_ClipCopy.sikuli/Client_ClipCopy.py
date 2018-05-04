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

def waitVanish_Click(image1,image2):
    while not exists(image1):
        wait(1)
    click(image2)

def click_click(image1, image2):
    click(image1)
    click(image2)


def Client_ClipCopy():
    global status
    status = "ClipCopy_scope"
    click_click(Pattern("1484027311485.png").similar(0.97),"1484027347052.png")
    click_click(Pattern("1484027382166.png").similar(0.90).targetOffset(-15,-9),Pattern("1484027382166.png").similar(0.90).targetOffset(5,-6))    
    click(Pattern("1484027445851.png").similar(0.92))
    if exists("1487033962541.png"):
        type(Key.ENTER)
        click_click(Pattern("1484027382166.png").similar(0.90).targetOffset(-15,-9),Pattern("1484027382166.png").similar(0.90).targetOffset(5,-14))
        click_click(Pattern("1484027382166.png").similar(0.90).targetOffset(-13,14),Pattern("1484027382166.png").similar(0.90).targetOffset(6,9))
        click(Pattern("1484027445851.png").similar(0.92))       
    click("1484027480963.png")
    status = "clip measure"
    waitVanish_Click("1484027528160.png",Pattern("1484027549980.png").similar(0.95))
    status = "clip saving"
    waitVanish_Click("1484027583202.png",Pattern("1484027612596.png").targetOffset(127,45)) 
    click(Pattern("1484027640260.png").targetOffset(45,0))


try:
    Client_ClipCopy()
#    Time()
#    success()

except FindFailed:
    Log("TestResult",'a',errorConst.error_1)  
    