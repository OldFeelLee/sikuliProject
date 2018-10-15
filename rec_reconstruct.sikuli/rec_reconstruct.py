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
    fileLog.status = 'begin'
#    fileLog.Log("untilREC_reconstruct_08.27-09.03",'a',errorConst.no_error)
    clickFunc.click_type(Pattern("1534728572838.png").targetOffset(5,11),Key.ENTER)
#    fileLog.Log("untilREC_reconstruct_08.27-09.03",'a',errorConst.no_error)
    fileLog.status = 'rec setup'
    typeFunc.type_type_click(Key.RIGHT,Key.RIGHT,"1535337017457.png")
#    fileLog.Log("untilREC_reconstruct_08.27-09.03",'a',errorConst.no_error)
    fileLog.status = 'storage setup'
    existsFunc.whileNotExists_wait(Pattern("1535336548316.png").similar(0.88))
#    fileLog.Log("untilREC_reconstruct_08.27-09.03",'a',errorConst.no_error)
    fileLog.status = 'running check'
    clickFunc.click_click(Pattern("1535336548316.png").similar(0.91),"1535336597401.png")
#    fileLog.Log("untilREC_reconstruct_08.27-09.03",'a',errorConst.no_error)
    fileLog.status = 'reconstruct start'
    clickFunc.click_click(Pattern("1535336611180.png").similar(0.86),"1535336726754.png")
#    fileLog.Log("untilREC_reconstruct_08.27-09.03",'a',errorConst.no_error)
    fileLog.status = 'close'     



try:
    
    fileLog.cnt = 0
    fileLog.status = None
    flagCheck = 0    
    while True:       
        if runningCheck.running("G2ConfTool.exe") == False:
            ConfTool.Open()
        recSetup()        
        fileLog.Log("untilREC_reconstruct_10.10-10.15",'a',errorConst.no_error)

except FindFailed:
    
    fileLog.Log("untilREC_reconstruct_10.10-10.15",'a',errorConst.error_1)
    App.open("gr1mailtest.bat")