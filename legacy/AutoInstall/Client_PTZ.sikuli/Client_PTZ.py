import datetime
import random
import string
from guide import *

        #Pattern("direction_0.png").exact()Pattern("direction_1.png").exact()Pattern("direction_2.png").exact()Pattern("direction_3.png").exact()

def RanTime():    #random 시간
    ran = "".join([random.choice(string.digits)])
    s=int(ran)
    wait(s)

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def success():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    PTZ complete!\n")
    f.close()  


def failed():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    "+status+" fail!\n")
    f.close()  

def PTZ_preset():
    click(Pattern("1487063976947.png").similar(0.84))
    click("1487063994364.png")
    click("1487064048721.png")
    wait(1)

def PresetCheck(image):
    for b in range(0,4,1):

        PTZ_short("direction_%s.png" %(b))
        wait(1)
        
        if exists(image):
            break
#        else:
#            PTZ_preset()

        PTZ_long("direction_%s.png" %(b))
        wait(1)
        if exists(image):
            break
#        else:
#            PTZ_preset()
#
def PTZ_short(image): 
    click(image)
    RanTime()



def PTZ_long(image):
    hover(image)
    mouseDown(Button.LEFT)
    RanTime()
    mouseUp(Button.LEFT)
    RanTime()


def Client_PTZ():
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
#    click("1487063527153.png")

    click("1487063527153.png")
    PresetCheck("1487064164064.png")
    runScript("C:\sikuli\script\AutoInstall\PaneClear")

try :        
    PresetCheck("1496831554817.png")
#    Client_PTZ()
    Time()
    success()

except FindFailed:
    Time()
    failed()    