import datetime
import string
import errorConst
import currentTime
import fileLog
import clickFunc
import existsFunc
import ConfTool
import os


def proxy_temp():
    for i in range(0,5):
        clickFunc.click_click(Pattern("1529030494175.png").similar(0.93).targetOffset(2,5),Pattern("1529030518871.png").targetOffset(-21,-1))    
        wait(5)
    return True

try:
    fileLog.cnt = 0
    fileLog.status = None 

    while True:
        if proxy_temp() == True :
            device = find("1529031197148.png")
            doubleClick(device)
            wait(2)
         
            dragDrop("1529030836724.png",device)
            wait(10)

        fileLog.Log("proxy",'a',errorConst.no_error)


except FindFailed:
    fileLog.Log("proxy",'a',errorConst.error_1)     
