# -*- coding: utf-8 -*-
#! python


import datetime
import errorConst
import ConfigConst

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def Log(filename,mode,flag):
    global flagCheck
    flagCheck=0
    f=open(filename+".txt",mode)
    Time()
    if flagCheck==int(flag):
        f.write(s+"    "+status+" pass\n")
        f.close()
    else:
        f.write(s+"    "+status+" fail\n")
        f.close()

def untilShow_hover_click(clickImage,hoverImage, showImage):
    click(clickImage)
    while True:
        hover(hoverImage)
        if exists(clickImage,FOREVER): 
            
            if exists(showImage,1):
                click(showImage)
                break
            else:                
                click(clickImage)


def waitVanish_click(image):
    wait(image, 10)
    try:
        while exists(image, 10):
            type(image,Key.TAB+"12345678"+Key.ENTER)          
            wait(1)
    except:
        wait(1)

def Login(image):
    if exists(image):
        while exists(image,10):
            type(image,Key.TAB+"12345678"+Key.ENTER)          
            wait(1)

def wait_click(image):
    wait(1)
    click(image)


def if_exists_click(image1, time, image2):
    if exists(image1, time):
        click(image2)



def ConfToolStart():    #ConfTool login 및 device tab 이동
    global status
    status = "ConfTool Login"
    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
    Login("1486617801030.png")          
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")

    

def ScanMode(): # Scan mode 진입 및 IP Scan 선택
    global status 
    status = "Device Scan & Add"
    click("1454380361915.png")
    if_exists_click("1484099067019.png",FOREVER,Pattern("1454380412860.png").similar(0.94).targetOffset(108,-25))      
    if exists(Pattern("1454380987835.png").exact(),2):
        wait_click(Pattern("1454380525571.png").similar(0.91))
        wait_click(Pattern("1454380563437.png").similar(0.84).targetOffset(-70,-1))
        ip()
        auto()
        runScript("C:\sikuli\script\AutoInstall\Conf_Loading")

    else:   
        ip()
        auto()
        runScript("C:\sikuli\script\AutoInstall\Conf_Loading")


def ip(): # ip 입력    
    wait(1)
    doubleClick(Pattern("1454380633509.png").targetOffset(-36,0))
    type(ConfigConst.PEARL_IP)
    wait(1)
    
def auto(): # DeviceScan 및 ID/PW 입력
    untilShow_hover_click("1454380656889.png","1484101583287.png", Pattern("1454381253425.png").exact().targetOffset(8,-10))
    wait_click("1454381290995.png")
    wait("1486602350491.png",10)
    type(ConfigConst.PEARL_ID+Key.TAB) #ID!
    wait(1)
    type(ConfigConst.PEARL_PW) # PW
    wait_click("1461749295384.png")
    wait_click("1455166085100.png")


try:
    ConfToolStart()
    ScanMode()
    Log("TestResult", 'a', errorConst.no_error)
    exit(errorConst.no_error)
except FindFailed:    
    
    Log("TestResult",'a',errorConst.error_1)
    exit(errorConst.error_1) 
#print a