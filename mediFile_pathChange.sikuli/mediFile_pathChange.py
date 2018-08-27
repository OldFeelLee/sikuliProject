import datetime
import string
import errorConst
import fileLog
import clickFunc
import existsFunc
import ConfTool
import os
import typeFunc
import runningCheck


def recSetup():
    global flagCheck
    clickFunc.click_type(Pattern("1534728572838.png").targetOffset(5,11),Key.ENTER)
    typeFunc.type_type_type(Key.RIGHT,Key.RIGHT,Key.RIGHT)
    if flagCheck==0:
        pathChange(Key.DOWN)
        flagCheck=1
    else:
        pathChange(Key.UP)
        flagCheck=0
    
def pathChange(driveChange):
    clickFunc.click_click("1534728025468.png",Pattern("1534728043828.png").similar(0.90).targetOffset(-16,-1))
    typeFunc.type_type_type(driveChange,Key.ENTER,Key.ENTER)
    wait(60)
    clickFunc.click_wait("1534729221449.png",120)            



try:
    
    fileLog.cnt = 0
    fileLog.status = None
    flagCheck = 0    
    while True:       
        if runningCheck.running("G2ConfTool.exe") == False:
            ConfTool.Open()
        recSetup()        
        fileLog.Log("mediaFile_pathChange_08.20-08.27",'a',errorConst.no_error)

except FindFailed:
    
    fileLog.Log("mediaFile_pathChange_08.20-08.27",'a',errorConst.error_1)
    App.open("gr1mailtest.bat")