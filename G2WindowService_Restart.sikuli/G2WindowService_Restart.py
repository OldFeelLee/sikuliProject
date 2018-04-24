import datetime
import string
import errorConst
import currentTime
import fileLog
import clickFunc
import existsFunc


def keyHold(key1,key2):
    keyDown(key1)
    type(key2)
    keyUp(key1)
    wait(2)

def type_Enter(str1):
    type(str1)
    wait(2)
    type(Key.ENTER)
    wait(2)
    
def Restart():

#    keyHold(Key.WIN,"r")
#    type_Enter("cmd")
    wait(2)
    for i in range(0,2,1):
        type_Enter("cd..")
        wait(2)
    type_Enter('cd "IDIS Solution Suite"\Server"')
    while True:
        if fileLog.status == errorConst.Running:
            type_Enter('G2WindowService.exe stop')
            fileLog.status = errorConst.Stopping
            wait(1)
            fileLog.Log_flagCheck("G2WindowRestart_03.19-03.26",'a',errorConst.no_error)    
            wait(240)            
        else:
            type_Enter('G2WindowService.exe start')
            fileLog.status =errorConst.Running
            wait(1)
            fileLog.Log_flagCheck("G2WindowRestart_03.19-03.26",'a',errorConst.no_error)    
            wait(240)



try :
    fileLog.cnt = 0
    fileLog.status = errorConst.Running  
    fileLog.Log_flagCheck("G2WindowRestart_03.19-03.26",'a',errorConst.no_error)     
    Restart()
except FindFailed:
    fileLog.Log_flagCheck("G2WindowRestart_03.19-03.26",'a',errorConst.error_1) 