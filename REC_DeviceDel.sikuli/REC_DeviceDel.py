import datetime
import string
import errorConst
import currentTime
import fileLog
import clickFunc
import existsFunc
import ConfTool



def REC_DeviceDel():
    while True:
        
        doubleClick(Pattern("1521075002526.png").similar(0.83))
        wait(2)
        clickFunc.click_click(Pattern("1521075039928.png").similar(0.91),Pattern("1521075067474.png").similar(0.88))
        type("_56")
        wait(2)
        if exists(Pattern("1521075253312.png").similar(0.88)):
            fileLog.status = "rec_Del"
            clickFunc.click_click(Pattern("1521075253312.png").similar(0.88),Pattern("1521075297394.png").similar(0.82))
            wait(2)
            clickFunc.click_wait_click("1521075324374.png","1521075339832.png",20)
            if not exists(Pattern("1521075918737.png").similar(0.81)):
                fileLog.Log_flagCheck("REC_DeviceDel_04.23-04.30",'a',errorConst.no_error)
            else:
                fileLog.Log_flagCheck("REC_DeviceDel_04.23-04.30",'a',errorConst.error_1) 
                break
                
        else:
            fileLog.status = "rec_Add"
            clickFunc.click_click("1521075591041.png",Pattern("1521075599238.png").targetOffset(-9,-11))
            clickFunc.click_wait_click("1521075324374.png","1521075339832.png",20)
            wait(20)
            if exists(Pattern("1521082064448.png").similar(0.90)):
                fileLog.Log_flagCheck("REC_DeviceDel_04.23-04.30",'a',errorConst.no_error)
            else:
                fileLog.Log_flagCheck("REC_DeviceDel_04.23-04.30",'a',errorConst.error_1)                 
                break

    
try:    
    fileLog.cnt = 0
    fileLog.status = None 
    ConfTool.Open()
    while True:
        if exists(Pattern("1521075002526.png").similar(0.83)):
            REC_DeviceDel()
        else:
            ConfTool.Open()
            REC_DeviceDel()
except FindFailed:
    fileLog.Log_flagCheck("REC_DeviceDel_04.23-04.30",'a',errorConst.error_1) 