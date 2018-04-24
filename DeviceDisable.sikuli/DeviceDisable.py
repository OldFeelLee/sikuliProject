import datetime
import string
import errorConst
import currentTime
import fileLog
import clickFunc
import existsFunc

def editDevice():
    while True:
        if fileLog.cnt/2 ==0:
        
            fileLog.status="Enable"
        else:
            fileLog.status=="Disable"
            
        #fileLog.status="editDevice"
        click(Pattern("1520214640364.png").similar(0.94).targetOffset(6,2))
        keyDown(Key.CTRL+"a")
        wait(2)
        keyUp(Key.CTRL+"a")
        clickFunc.click_click_click(Pattern("1520214850666.png").similar(0.90).targetOffset(143,-1),Pattern("1520214911950.png").targetOffset(-23,-2),"1520214964929.png")
        fileLog.Log("deviceDisable_03.05-03.12",'a',errorConst.no_error)
        loading()
def loading():

    fileLog.status = "loading"
    existsFunc.whileNotExists("1520303212175.png","1520303228581.png")
    wait(2)
    click("1520303381858.png")
    wait(2)


try:    
    fileLog.cnt = 0
    fileLog.status = None   
    editDevice()
    
except FindFailed:
    fileLog.Log("deviceDisable_03.05-03.12",'a',errorConst.error_1) 