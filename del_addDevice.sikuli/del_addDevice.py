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


def del_addDevice():
    clickFunc.click_click_click("1536543576750.png",Pattern("1536543590934.png").targetOffset(90,-4),"1536543616554.png")
    clickFunc.click_click(Pattern("1536543900834.png").similar(0.92).targetOffset(54,-4),"1536543918591.png")
    deviceScanCheck()    

def addDevice():
    clickFunc.click_click("1536542513998.png",Pattern("1536542583611.png").similar(0.97).targetOffset(41,-10))
    if flagCheck == 0:
        typeFunc.type_type_type(Key.TAB,Key.UP,Key.UP)
        typeFunc.type_type(Key.DOWN,Key.DOWN)
    else :
        type(Key.TAB)
        wait(2)
    typeFunc.type_type(Key.TAB,'10.0.127.35')
    typeFunc.type_type_type(Key.TAB,Key.TAB,Key.TAB)
    deviceScanCheck()

def deviceScanCheck():
    existsFunc.whileNotExists_type_wait(Pattern("1536543140085.png").targetOffset(-39,5),Key.SPACE,30)

#    if typeFunc.type_existsClick(Key.SPACE, 30, Pattern("1536543140085.png").targetOffset(-39,5)) == True: 
    clickFunc.click_click(Pattern("1536543140085.png").targetOffset(-39,5),"1536543204973.png")
    if typeFunc.type_existsClick('admin'+Key.ENTER,10,Pattern("1536543327921.png").similar(0.92)) == True:
        clickFunc.click_wait("1536543370916.png",30)
    else:
        type(Key.ENTER)
        wait(10)
        clickFunc.click_wait("1536543370916.png",30)      



try:    
    global flagCheck
    fileLog.cnt = 0
    fileLog.status = None
    flagCheck = 0    
    while True:       
        if runningCheck.running("G2ConfTool.exe") == False:
            ConfTool.Open()
            ConfTool.deviceTab() 
            addDevice()
            flagCheck = 1       
        else:
            ConfTool.deviceTab() 
            addDevice()                       
        del_addDevice()        
        fileLog.Log("deviceDel_Admin_09.10-09.17",'a',errorConst.no_error)

except FindFailed:    
    fileLog.Log("deviceDel_Admin_09.10-09.17",'a',errorConst.error_1)
    App.open("gr1mailtest.bat")