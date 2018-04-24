import datetime
import random
import string

        #Pattern("direction_0.png").exact()Pattern("direction_1.png").exact()Pattern("direction_2.png").exact()Pattern("direction_3.png").exact()

def RanTime():    #random 시간
    ran = "".join([random.choice(string.digits)])
    s=int(ran)
    wait(s)

def Time():    #get current time
    global s
    today = datetime.datetime.now()
    s = str(today)

def Log(filename,mode,flag):     #result log
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




def PTZ_preset():    #preset move
    click(Pattern("1487063976947.png").similar(0.84))
    click("1487063994364.png")
    click("1487064048721.png")
    wait(1)
    click("1487147768015.png")

def imageFind(image):    #image compare
    if exists(image):
        Time()
        f=open("c:/a/install.txt",'a')
        f.write(s+"    ok!\n")
        f.close()  
    


def PresetCheck(image):    #PTZ Action(short/Long)with image compare
    for b in range(0,4,1):
        PTZ_short("direction_%s.png" %(b))
        wait(1)
        if exists(image):            
            break
        else:
            PTZ_preset()
            wait(5)
            imageFind(image)
        PTZ_long("direction_%s.png" %(b))
        wait(1)
        if exists(image):            
            break
        else:
            PTZ_preset()
            wait(5)
            imageFind(image)

def PTZ_short(image):    #PTZ short action
    click(image)
    RanTime()

def PTZ_long(image):    #PTZ long action
    hover(image)
    mouseDown(Button.LEFT)
    RanTime()
    mouseUp(Button.LEFT)
    RanTime()


def Client_PTZ():    #main
    global status
    status = "Client focus"
    runScript("C:\sikuli\script\AutoInstall\OEM_Client")
    status = "Client Init"
    runScript("C:\sikuli\script\AutoInstall\Client_Loading")
    click("1487041638105-1.png")
    status = "Device DragDrop"
    runScript("C:\sikuli\script\AutoInstall\Client_Device_DragDrop")
    rightClick()
    click("1487063512377.png")


    click("1487063527153.png")
#    PresetCheck("1487064164064.png")
#    PresetCheck(Pattern("1487140889600.png").similar(0.94))
    PresetCheck(Pattern("1487143148467.png").similar(0.90))
#    PresetCheck(Pattern("1487205652187.png").exact())
    runScript("C:\sikuli\script\AutoInstall\PaneClear")

try : 

    Client_PTZ()
    Log("TestResult",'a',errorConst.no_error)

except FindFailed:
    Log("TestResult",'a',errorConst.error_1)    