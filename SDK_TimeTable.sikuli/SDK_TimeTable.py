import errorConst
import fileLog
import clickFunc


def aliveCheck(imge1,imge2):
  
    click(imge1)
    wait(2)
    if not exists(imge2):
        return True
   
try:
    fileLog.cnt = 0
    fileLog.status = None 
    fileLog.Log("sdk_evt",'a',errorConst.no_error)

    while True:
        if aliveCheck("1529568159493.png",Pattern("1529568212403.png").exact().targetOffset(3,3))== True: 
            
            for i in range(0,10):
                clickFunc.click_click("1529568260274.png",Pattern("1529568212403.png").exact().targetOffset(3,3))
                wait(2)

                fileLog.Log("sdk_evt",'a',errorConst.no_error)
        else:

            fileLog.Log("sdk_evt",'a',errorConst.error_1)
            break 
            


except FindFailed:

    fileLog.Log("sdk_evt",'a',errorConst.error_1)    