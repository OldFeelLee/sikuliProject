import datetime
import string
import errorConst
import currentTime
import fileLog
import clickFunc
import existsFunc
import typeFunc
import os
import glob



def start():
    clipCount=0    
    while True:
        fileLog.status = "G2ProblemReport"  
        App.open("C:\IDIS Solution Suite\Client\G2ProblemReporter.exe")
        wait(5)
        fileLog.status = "save file"  
        typeFunc.type_type_type(Key.ENTER,Key.TAB,Key.ENTER)
        existsFunc.whileNotExists_wait("1523843000038.png")
        typeFunc.type_type_click('E:\ProblemReporter',Key.ENTER,Pattern("1523843000038.png").targetOffset(2,-6))
        existsFunc.whileNotExists_wait("1523843210408.png")
        
        clickFunc.click_click(Pattern("1523843210408.png").targetOffset(-41,-3),"1523843231145.png")
        wait(10)
        if exists(Pattern("1523858731486.png").similar(0.86)):
            fileLog.status = "Upload"  
            click("1523858747983.png")
            clickFunc.click_click("1523845300001.png","1523845720314.png")
            fileLog.Log("G2ProblemReporter_04.16-04.23",'a',errorConst.no_error) 
        else:
            fileLog.status = None            
            existsFunc.whileNotExists_wait(Pattern("1523843985601.png").similar(0.88))
            clickFunc.click_click_click("1523845300001.png","1523845300001.png","1523845720314.png")
            typeFunc.keyDownUp(Key.CTRL,'w')
            fileLog.Log("G2ProblemReporter_04.16-04.23",'a',errorConst.no_error) 
            
        clipCount=clipCount +1

        if clipCount>=30:            
       
            os.chdir("E:\ProblemReporter")
            files = glob.glob("*.zip")
            for a in files:   
                os.remove(a)
                wait(120)

try:

    fileLog.cnt = 0
    fileLog.status = None   
    start()    
except FindFailed:
    fileLog.Log("G2ProblemReporter_04.16-04.23",'a',errorConst.error_1) 
