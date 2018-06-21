from sikuli import *
import clickFunc
import fileLog

def for_click_click(image1,image2,cnt):
    for i in range(0,cnt):
        fileLog.status = "for1"
        clickFunc.click_click(image1,image2)
        fileLog.status = "for2"
        wait(5)
    return True    