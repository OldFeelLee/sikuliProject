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
    existsFunc.exists_click_click("1486608642625.png","1525848389391.png",Pattern("1525848401646.png").similar(0.84).targetOffset(-16,-1))
    
    clickFunc.click_type("1525848424164.png",setSerial)
    clickFunc.click_wait_click("1525848538644.png","1525848552081.png",60)    
    click("1525848559525.png")


try:
    fileLog.cnt = 0
    fileLog.status = None 
    licenseDel()
    Serial("serial")
    while True:
        LicenseTool()
        fileLog.Log("LicenseAuth",'a',errorConst.no_error)


except FindFailed:
    fileLog.Log("LicenseAuth",'a',errorConst.error_1)     

 