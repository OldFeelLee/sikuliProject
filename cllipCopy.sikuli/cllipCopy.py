import datetime
import string
import errorConst
import currentTime
import fileLog
import clickFunc
import existsFunc
import os
import glob

def clipCopy():
    clipCount = 0
    device = find(Pattern("1522026468764.png").similar(0.94))
    pane = find("1522026485828.png")

    while True:
        os.chdir("c:\sikuliLog")
        dragDrop(device,pane)
        wait(10)
        existsFunc.exists_click_click(Pattern("1522026553170.png").similar(0.94),"1522026628143.png",Pattern("1522029813911.png").targetOffset(-1,-12))
        clickFunc.click_click(Pattern("1522026653106.png").targetOffset(-12,0),"1522026673584.png")  
        wait(2)
        clickFunc.click_wait_click("1522026720780.png","1522026730394.png",5)
        wait("1522026752652.png",60)
        existsFunc.exists_click_click("1522026752652.png","1522026755408.png","1522026766617.png")
        rightClick(pane)
        clickFunc.click_wait_click("1522031018067.png","1522031028264.png",5)
        fileLog.Log("clipCopy_09.17-09.27",'a',errorConst.no_error)  
        wait(30)
        clipCount=clipCount +1
        if clipCount>=60:            
       
            os.chdir("E:\clip")
            files = glob.glob("*.exe")
            for a in files:   
                os.remove(a)
                wait(60)

try:

    fileLog.cnt = 0
    fileLog.status = None   
    clipCopy()    
except FindFailed:
    fileLog.Log("clipCopy_09.17-09.27",'a',errorConst.error_1) 