import datetime
import string
import errorConst
import currentTime
import fileLog
import clickFunc
import existsFunc
import ConfTool
import os
import forFunc
import randomFunc

try:
    
    fileLog.cnt = 0
    fileLog.status = None 
    pane = find("1529289965951.png")
    layout = find(Pattern("1529290040773.png").similar(0.95).targetOffset(8,10))
    device = find(Pattern("device.png").similar(0.90).targetOffset(7,9))
    randomFunc.ranNumber()
    while True:
        fileLog.status = "device"
        dragDrop(device,pane)
        wait(5)
        fileLog.status = "device drag"
        if forFunc.for_click_click(Pattern("1529290607934.png").similar(0.96).targetOffset(-7,3),Pattern("1529288997453.png").targetOffset(-22,3),1) == True :    
            fileLog.status = "layout"    
            wait(randomFunc.ranTime)
            dragDrop(layout,pane)
            fileLog.status = "layout drag"

            wait(5)
            fileLog.status = "layt"
        if forFunc.for_click_click(Pattern("1529290607934.png").similar(0.96).targetOffset(-7,3),Pattern("1529288997453.png").targetOffset(-22,3),1) == True :
            fileLog.status = "pane"
            wait(randomFunc.ranTime)
            rightClick(pane)
            clickFunc.click_click("1529290226726.png","1529290237097.png")
            fileLog.status = "clear"

        fileLog.Log("PlayTab_device&layout_06.18-06.25",'a',errorConst.no_error)


except FindFailed:
    fileLog.Log("PlayTab_device&layout_06.18-06.25",'a',errorConst.error_1)   



