# -*- coding: utf-8 -*-
#! python
#import os
#import sys
import datetime
import errorConst
import ConfigConst


def click_type(image,data):
    click(image)
    type(data)


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

def if_exists_click(image,time):
    if exists(image,time):
        click(image)

def click_click(image1,image2):
    click(image1)
    click(image2)

def click_click_click(image1, image2, image3):
    click(image1)
    click(image2)
    click(image3)
    

def doubleClick_type(image,str):    
    doubleClick(image)
    type(str)

def click_exists_click(clickImage1,showImage,clickImage2):    
    click(clickImage1)
    if exists(showImage):
        click(clickImage2)

def Login(image):
    if exists(image):
        while exists(image,10):
            type(image,Key.TAB+"12345678"+Key.ENTER)          
            wait(1)

def STM_Init():    #Key_const 
    global LoadBalance
    global Fixed
    global current
    global serviceCount
    global virtualINT_status
    global deviceStatus
    global firstCheck
    global deviceCharge
    global serviceRunning_count
    
    serviceRunning_count = ConfigConst.Single
    deviceCharge = ConfigConst.Default
    firstCheck = ConfigConst.Default    
    deviceStatus=ConfigConst.Default
    virtualINT_status=ConfigConst.Default
    serviceCount = ConfigConst.Single
    current = "Fixed"
    LoadBalance=Key.HOME
    Fixed = Key.END


def multiStreaming_Set():    #streaming 복사 후 server ip 및 service port 변경
    global status
    status = "service manager setting"
    run("C:\Sikuli\CopyBat.bat")    
    openApp("C:\STM\ServiceManager.exe")
    if_exists_click(Pattern("1487752803706.png").similar(0.92).targetOffset(0,8),60)
    click_click(Pattern("1487640159144.png").targetOffset(8,-3),Pattern("1487640207079.png").targetOffset(-4,-11))
    doubleClick_type(Pattern("1487640243411.png").similar(0.90),ConfigConst.Server_IP)
    click_exists_click("1487640536058.png","1487640563367.png","1487640591377.png")
    click_click(Pattern("1487640159144.png").targetOffset(8,-3),Pattern("1487640207079.png").targetOffset(-3,10))
    doubleClick_type(Pattern("1487640673858.png").similar(0.90),ConfigConst.Service_Port)
    click_exists_click("1487640536058.png","1487640563367.png","1487640591377.png")

def statusChange_to(status_):
    global status
    global current
    statusConst="LoadBalance"
    if statusConst==status_:
        status = "status change to loadbalance"
        
        click_type(Pattern("1487644776254.png").exact(), LoadBalance)
        if_exists_click("1487647119862.png",2)
        click()
        current = "LoadBalance"
        deviceAssign()
    else:
        status = "status change to Fixed"
        click_type(Pattern("1487644776254.png").exact(), Fixed)
        if_exists_click("1487647119862.png",2)
        click()
        current ="Fixed"
        deviceAssign()        

def statusChange_toFixed():
    global status
    status = "status change to Fixed"
    global current
    click_type(Pattern("1487644776254.png").exact(), Fixed)
    if_exists_click("1487647119862.png",2)
    click()
    current ="Fixed"
    deviceAssign()

def statusCheck():
    global status
    status = "status Check"
    if current =="LoadBalance":
        click_type(Pattern("1487644776254.png").exact(), LoadBalance)
        if exists("1487647119862.png",2):
            click("1487647119862.png")
            Log("TestResult",'a',errorConst.error_1)             
        else:
            click()
    else:
        click_type(Pattern("1487644776254.png").exact(), Fixed)
        if exists("1487647119862.png",2):
            click("1487647119862.png")
            Log("TestResult",'a',errorConst.error_1)             
        else:
            click()
                                                

def statusChange():    #Fixed 면 Loadbalance로 Loadbalance 면 Fixed로
    global current
    global deviceCharge
    if current == "Fixed":
        click_type(Pattern("1487644776254.png").exact(), LoadBalance)
        current = "LoadBalance"
        if_exists_click("1487647119862.png",2)
        
    else:
        click_type(Pattern("1487644776254.png").exact(), Fixed)
        current = "Fixed"
        if_exists_click("1487647119862.png",2)
    deviceCharge = ConfigConst.Default        

        
def deviceAssign():
    global status
    global deviceCharge
    status = "Device Assign"
    if deviceCharge == ConfigConst.Default:
        
        click_type((),Key.HOME)
        click_click_click("1487647351040.png",Pattern("1487647445539.png").targetOffset(-25,0),"1487647479902.png")
        wait(2)
        deviceCharge = ConfigConst.Running
        
def deviceUnassign():
    global status
    global deviceCharge

    status = "Device Unassign"
    if exists("1487647351040.png"):    
        click_click("1487647351040.png",Pattern("1487647445539.png").targetOffset(-25,0))
        click_click(Pattern("1487728320248.png").targetOffset(-24,1),"1487647479902.png")
    else:
        click("1487653184633.png")
        click_click("1487647351040.png",Pattern("1487647445539.png").targetOffset(-25,0))       
        click_click(Pattern("1487728320248.png").targetOffset(-24,1),"1487647479902.png")
    wait(2)
    deviceCharge = ConfigConst.Default


def virtualINTSet():
    global virtualINT_status

    
    if virtualINT_status == ConfigConst.Default:
        openApp("D:\Test_Util\StrongVirtualINT\G1VirtualINT\G1VirtualINT.exe")
        if_exists_click("1487661932651.png",20)
        virtualINT_status=ConfigConst.Running
    print virtualINT_status                

def deviceReset():
    global status
    global deviceStatus
    
    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
    Login("1487643896246.png")   
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")
    status = "Device Reset"    
#    click_click("1487050858920-1.png","1487051671208.png")
    click("1487050858920-1.png")
    if deviceStatus == ConfigConst.Default:
        if exists("1487663297181.png"):
            click("1487663297181.png")
            keyDown(Key.CTRL+"a")
            keyUp(Key.CTRL+"a")
            type(Key.DELETE)
            click(Pattern("1487051765657.png").targetOffset(-45,-3))
            runScript("C:\sikuli\script\AutoInstall\Conf_Loading")
        
def deviceAdd(deviceNum):
    global status
    global deviceCount
    global deviceStatus   
    
    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
    Login("1487643896246.png")          
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")        
    status = "Device Add"
    if deviceStatus == ConfigConst.Default:
        deviceCount = int(deviceNum)
        click_click("1487050858920.png",Pattern("1487050882738.png").similar(0.95).targetOffset(62,-4))
        if not exists("1487053359526.png"):
            click(Pattern("1487053415818.png").targetOffset(-2,19))
            type(Key.HOME)
        keyDown(Key.SHIFT+Key.CTRL+Key.ALT)
        click("1487050915988.png")
        keyUp(Key.SHIFT+Key.CTRL+Key.ALT)
        doubleClick(Pattern("1487663041476.png").exact())
        type("10.0.124.58")
        doubleClick(Pattern("1487051108918.png").exact())
        type(deviceNum+Key.ENTER)
        click("1487051183723.png")
        while not exists("1487051451730.png"):
            click("1487051183723.png")
            wait(1)
        deviceStatus = ConfigConst.Running

def serviceCount_Add():
    global serviceCount
    if serviceCount == ConfigConst.Single:
        serviceCount = ConfigConst.Multi
    else:
        serviceCount = ConfigConst.Single

def serviceCount_Del():
    global serviceCount
    global deviceCharge
    if serviceCount == ConfigConst.Single:
        serviceCount = ConfigConst.Default
        deviceCharge = ConfigConst.Default
    else:
        serviceCount = ConfigConst.Single

def STM_Start():    #Streaming service start
    global firstCheck
    global serviceRunning_count
    global status
    status = "service Start"
    keyDown(Key.WIN+"r")
    keyUp(Key.WIN+"r")
    wait(1)
    type("C:\Sikuli\cmd_shortCut"+Key.ENTER)
    wait(2)
    type("C:\STM\StreamingService.exe"+Key.ENTER)
    wait(5)
    Log("TestResult",'a',errorConst.no_error)
    if serviceRunning_count == ConfigConst.Single:
        serviceRunning_count = ConfigConst.Multi    
    else:
        serviceRunning_count = ConfigConst.Single        

    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
     
def deviceAssign_check():
    global service1_device   
    global service2_device
    global serviceTotal_device
    serviceTotal_device=deviceCount
    service1_device = deviceCount/2
    deviceTemp = deviceCount%2
    if deviceTemp==0: 
        service2_device = deviceCount/2
    else:
        service2_device = deviceCount/2+1
    

def deviceAssign_filter():
    global status
    global serviceCount
    status = "Device Assign check"
    if current=="Fixed":
        serviceCount = ConfigConst.Single
        
    if serviceCount==ConfigConst.Single:
        status= "SingleService Assign check"
        type("1487667323771.png","Numbers: "+str(serviceTotal_device))
        if not exists(Pattern("1487667410732.png").exact()):
            click(Pattern("1487668615704.png").exact())
        else:
            Log("TestResult",'a',errorConst.error_1)
    else: 
        status = "MultiService_Single running Assign check"
        if not serviceRunning_count == ConfigConst.Single:
            status = "MultiService Assign check"
            type("1487667323771.png","Numbers: "+str(service1_device))
            if not exists(Pattern("1487667410732.png").exact()):
                click(Pattern("1487668615704.png").exact())
                type("1487667323771.png","Numbers: "+str(service2_device))        
                if not exists(Pattern("1487667410732.png").exact()):
                    click(Pattern("1487668615704.png").exact())
                else:
                    Log("TestResult",'a',errorConst.error_1)                    
            else:
                Log("TestResult",'a',errorConst.error_1)
        else:

            type("1487667323771.png","Numbers: "+str(serviceTotal_device))
            if not exists(Pattern("1487667410732.png").exact()):
                click(Pattern("1487668615704.png").exact())
            else:
                Log("TestResult",'a',errorConst.error_1)                

def deviceUnassign_filter():
    global status
    status = "Device Unassign check"
    if current=="Fixed":
        serviceCount = ConfigConst.Single
    if serviceCount==ConfigConst.Single:
        status= "SingleService Unassign check"
        type("1487667323771.png","Numbers: "+str(serviceTotal_device))
        if exists(Pattern("1487667410732.png").exact()):
            click(Pattern("1487668615704.png").exact())
        else:
            Log("TestResult",'a',errorConst.error_1)
    else: 
        status= "SingleService Unassign check"
        type("1487667323771.png","Numbers: "+str(service1_device))
        if exists(Pattern("1487667410732.png").exact()):
            click(Pattern("1487668615704.png").exact())
            type("1487667323771.png","Numbers: "+str(service2_device))        
            if exists(Pattern("1487667410732.png").exact()):
                click(Pattern("1487668615704.png").exact())
            else:
                Log("TestResult",'a',errorConst.error_1)                    
        else:
            Log("TestResult",'a',errorConst.error_1)        


def Kill():    #Streaming service terminate
    global serviceRunning_count 
    global status
    status = "service  terminate"
    os.system('taskkill /f /im StreamingService.exe')
    Log("TestResult",'a',errorConst.no_error)
    wait(5)
    if serviceRunning_count == ConfigConst.Multi:
        serviceRunning_count = ConfigConst.Single
    else:
        serviceRunning_count = ConfigConst.Default

def STM_Setup():    #Streaming setup enter
    global status
    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
    Login("1487643896246.png")          
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")      
    click("1487644001959.png")
    if serviceCount == ConfigConst.Multi:
        doubleClick(Pattern("1487838279403.png").exact())
    elif serviceCount == ConfigConst.Single:
        if serviceRunning_count == ConfigConst.Single:
            doubleClick(Pattern("1487838477847.png").exact())
 #    if not serviceCount == ConfigConst.Default:
#        doubleClick(Pattern("1487644398778.png").similar(0.84))
    if_exists_click("1487644512121.png",60)

def STM_setupExit():
    click("1487727013898.png")

def STM_Regist():    #Service regist
    global status
    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
    Login("1487643896246.png")          
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")   
    status = "service regist"
    click_click("1487644001959.png",Pattern("1487644015998.png").similar(0.88))
    if serviceCount == ConfigConst.Default:
        click_click(Pattern("1487828985327.png").exact().targetOffset(-154,0),"1487644093241.png")        
    else:        
        click_click(Pattern("1487644056606.png").similar(0.96).targetOffset(-7,0),"1487644093241.png")
    Log("TestResult",'a',errorConst.no_error)    
    serviceCount_Add()

def STM_Unregist():
    global status
    status = "service unregist"
    runScript("C:\sikuli\script\AutoInstall\OEM_Conf")
    Login("1487643896246.png")          
    runScript("C:\sikuli\script\AutoInstall\Conf_Loading")
    if serviceCount == ConfigConst.Multi:
        click_click_click("1487644001959.png",Pattern("1487829623043.png").exact() ,Pattern("1487731609650.png").similar(0.96))
    else:
        click_click_click("1487644001959.png",Pattern("1487644398778.png").similar(0.84),Pattern("1487731609650.png").similar(0.96))
    click_type("1487731684462.png","12345678"+Key.ENTER)
    Log("TestResult",'a',errorConst.no_error)
    serviceCount_Del()    
    
def connectionStatus():
    global status
    status = "Device connection status"
    wait(5)

    type("1487667323771.png","disconnect")
    if exists(Pattern("1487667410732.png").exact()):
        click(Pattern("1487668615704.png").exact())
        Log("TestResult",'a',errorConst.no_error)
    else:
        Log("TestResult",'a',errorConst.error_1)         
        
  
def loadbalanceTest_deviceAssign(status_):
    global status
#    STM_Init()
    virtualINTSet()
    deviceReset()
    deviceAdd('2')
    STM_Setup()
    statusChange_to(status_)
    deviceAssign_check()
    connectionStatus()
    deviceAssign_filter()
    status = "loadbalanceTest_deviceAssign"
    Log("TestResult",'a',errorConst.no_error)     

def loadbalanceTest_serviceTerminate_Single(status_):
    global status
    loadbalanceTest_serviceUnregist(status_)
    Kill()
    STM_Start()
    STM_Setup()
    connectionStatus()
    deviceAssign_filter()   
    STM_setupExit()
    STM_Regist()
    status = "loadbalanceTest_serviceTerminate_Single"
    Log("TestResult",'a',errorConst.no_error)     

def loadbalanceTest_serviceTerminate_Multi(status_):
    global status
    loadbalanceTest_deviceAssign(status_)    
    Kill()
    connectionStatus()
    deviceAssign_filter()   
    STM_Start()
    connectionStatus()
    deviceAssign_filter()  
    STM_setupExit()
    status = "loadbalanceTest_serviceTerminate_Multi"
    Log("TestResult",'a',errorConst.no_error)     


def loadbalanceTest_deviceUnassign_status(status_):
    global status
    loadbalanceTest_deviceAssign(status_)
    deviceUnassign()    
    deviceUnassign_filter()
    STM_setupExit()
    STM_Setup()
    statusCheck()
    STM_setupExit()
    status = "loadbalanceTest_deviceUnassign_status"
    Log("TestResult",'a',errorConst.no_error)    

def loadbalanceTest_serviceUnregist(status_):
    loadbalanceTest_deviceAssign(status_)
    STM_setupExit()
    STM_Unregist()


def loadbalanceTest_serviceUnregist_Multi(status_):
    global status
    
    loadbalanceTest_serviceUnregist(status_)    
    STM_Setup()
    connectionStatus()
    deviceAssign_filter()
    STM_setupExit()
    STM_Regist()
    STM_Setup()
    connectionStatus()
    deviceAssign_filter()
    STM_setupExit()
    status = "loadbalanceTest_serviceUnregist_Multi"
    Log("TestResult",'a',errorConst.no_error)

def loadbalanceTest_serviceUnregist_Single(status_):
    global status
    STM_Unregist()
    loadbalanceTest_serviceUnregist(status_)
    
    STM_Regist()
    STM_Setup()
    connectionStatus()
    deviceUnassign_filter()
    deviceAssign()
    connectionStatus()
    deviceAssign_filter()    
    STM_setupExit()
    STM_Regist()
    status = "loadbalanceTest_serviceUnregist_Single"
    Log("TestResult",'a',errorConst.no_error)

def loadbalanceTest_statusChange(status_):
    global status
    loadbalanceTest_deviceAssign(status_)    
    statusChange()
    deviceAssign_filter()
    statusCheck()
    STM_setupExit()
    STM_Setup()
    statusCheck()
    deviceAssign()
    
    connectionStatus()
    deviceAssign_filter()
    STM_setupExit()
    STM_Setup()
    statusCheck()
    STM_setupExit()    
    status = "loadbalanceTest_statusChange"
    Log("TestResult", 'a', errorConst.no_error)



def loadbalance(status):
    loadbalanceTest_serviceTerminate_Multi(status)

    loadbalanceTest_serviceUnregist_Multi(status)

    loadbalanceTest_deviceUnassign_status(status)

    loadbalanceTest_serviceUnregist_Single(status)
    
    loadbalanceTest_serviceTerminate_Single(status)



try:
    global status      
    STM_Init()
    #multiStreaming_Set()
    STM_Start()
    STM_Regist()   
    
#    loadbalance("LoadBalance") 

    loadbalanceTest_statusChange("LoadBalance")


except FindFailed:
    Log("TestResult",'a',errorConst.error_1)    