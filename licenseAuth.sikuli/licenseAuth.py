# -*- coding: utf-8 -*-


import datetime
import string
import errorConst
import currentTime
import fileLog
import clickFunc
import existsFunc
import ConfTool
import os
import typeFunc

def Serial(filename):
    global setSerial   
    os.chdir("C:\sikuli")
    fr=open(filename+".txt").read()
    setSerial=str(fr)



def licenseDel():
    global status
    status = "License Delete"
    App.open("C:\sikuli\licenseDel.bat")    
    wait(5)

   

def LicenseTool():
    fileLog.status = "LicenseTool Run"

    App.open("C:\sikuli\IDIS_License.bat")
    wait(10)    
    fileLog.status = "License auth"    
    existsFunc.exists_click_click("1486608642625.png",Pattern("1525850049206.png").similar(0.94),Pattern("1525848401646.png").similar(0.84).targetOffset(-16,-1))    
 
    #clickFunc.click_click(Pattern("1527476826252.png").similar(0.75),"1486608642625.png")
    clickFunc.click_type(Pattern("1527476826252.png").similar(0.75),setSerial)
    hover("1486608642625.png")
#    wait(3600)
#    clickFunc.click_click("1527474242658.png","1527475995704.png")
#    typeFunc.type_hover(setSerial,"1486608642625.png")
    clickFunc.click_wait_click("1525848538644.png","1525848552081.png",30)    
    click("1525848559525.png")


try:
    fileLog.cnt = 0
    fileLog.status = None 
    licenseDel()
    Serial("serial")
    while True:
        LicenseTool()
        fileLog.Log("LicenseAuth_06.04-06.11",'a',errorConst.no_error)
        licenseDel()

except FindFailed:
    fileLog.Log("LicenseAuth_06.04-06.11",'a',errorConst.error_1)
    App.open("gr1mailtest.bat")

 