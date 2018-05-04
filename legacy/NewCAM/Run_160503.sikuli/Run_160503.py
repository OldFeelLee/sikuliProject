import random
import string


    

def RanTime():    #random 시간
    ran = "".join([random.choice(string.digits)])
    s=int(ran)
    wait(s)

def Live_tab():
    if exists(Pattern("1455609384135.png").similar(0.57)):
        click(Pattern("1455609384135.png").similar(0.62).targetOffset(-61,-63))

def DevicePaneDefine(): #device, pane 변수 정의 및 pane에 device 추가
    global pane
    global device
    if exists(Pattern("1455170393643.png").similar(0.98).targetOffset(18,13)):
        wait(1)
        device = find(Pattern("1455170393643.png").similar(0.98).targetOffset(18,13))
        pane = find(Pattern("1455258060501.png").similar(0.59))
        dragDrop(device,pane)
        wait(3)
    else:        
        click(Pattern("1455170236648.png").similar(0.85).targetOffset(-41,-1))
        wait(1)
        device = find(Pattern("1455170393643.png").similar(0.98).targetOffset(18,13))
        pane = find(Pattern("1455258060501.png").similar(0.62))
        dragDrop(device,pane)
        wait(3)

def LayoutChange():    #layout 변경
    RanTime()
    click(Pattern("1455170817026.png").targetOffset(-144,-1))
    RanTime()
    click(Pattern("1455170817026.png").targetOffset(-120,-1))
    RanTime()
    click(Pattern("1455170817026.png").targetOffset(-96,0))
    RanTime()
    click(Pattern("1455170817026.png").targetOffset(-72,-1))
    RanTime()
    click(Pattern("1455170817026.png").targetOffset(-48,-1))
    RanTime()
    click(Pattern("1455170817026.png").targetOffset(-24,0))
    RanTime()
    click(Pattern("1455170817026.png").targetOffset(0,-1))
    RanTime()
    click(Pattern("1455170817026.png").targetOffset(24,0))
    RanTime()
    click(Pattern("1455170817026.png").targetOffset(48,-1))
    RanTime()
    click(Pattern("1455170817026.png").targetOffset(71,-1))
    RanTime()
    click(Pattern("1455170817026.png").targetOffset(95,-1))
    RanTime()
    click(Pattern("1455170817026.png").targetOffset(120,0))
    RanTime()
    click(Pattern("1455170817026.png").targetOffset(144,0))
    RanTime()
    click(Pattern("1455170817026.png").targetOffset(-144,-1))

def MultiStreamLive(): # 멀티스트림_live

    click(Pattern("1455170817026-1.png").targetOffset(-144,-1))
    wait(1)
    keyDown(Key.CTRL+Key.SHIFT+Key.ALT)
    rightClick(pane)
    keyUp(Key.CTRL+Key.SHIFT+Key.ALT)
    wait(1)
    rightClick(pane)
    hover(Pattern("1455255611112.png").targetOffset(-12,20))
    click(Pattern("1455527545395.png").targetOffset(-34,-9))
    RanTime()
    rightClick(pane)
    hover(Pattern("1455255611112.png").targetOffset(-12,20))
    click(Pattern("1455527545395.png").targetOffset(-31,13))
    RanTime()
    rightClick(pane)
    hover(Pattern("1455255611112.png").targetOffset(-12,20))
    click(Pattern("1455527545395.png").targetOffset(-35,-9))
    RanTime()

def PTZ_Check():#PTZ hoverToolbar 활성화
    rightClick(pane)
    if exists(Pattern("1455602298583.png").exact()):
        click(Pattern("1455258268564.png").targetOffset(-32,-33))
        wait(1)
        click(Pattern("1455257719963.png").targetOffset(-160,1))
        wait(1)
        popup(unicode("PTZ step 동작 및 preset 저장을 확인해주세요.","utf-8"),"PTZ_step")
        PTZ_short()
        popup(unicode("PTZ continue 동작 및 preset 저장을 확인해주세요.","utf-8"), "PTZ_continue")
        PTZ_long()
        popup(unicode("저장된 preset을 확인해주세요.","utf-8"),"PTZ_Preset_View")
        PTZ_Preset_View()   
    else:
        popup(unicode("PTZ를 지원하지 않습니다.","utf-8"),"PTZ")

def PTZ_short(): 
    #PTZ_short
    click(Pattern("1455257755424.png").targetOffset(-21,0))
    RanTime()
    click(Pattern("1455257755424.png").targetOffset(20,1))
    RanTime()
    click(Pattern("1455257755424.png").targetOffset(-2,-20))
    RanTime()
    click(Pattern("1455257755424.png").targetOffset(-2,20))
    RanTime()
    click(Pattern("1455257719963.png").targetOffset(-103,-1))
    RanTime()
    click(Pattern("1455257719963.png").targetOffset(-79,-1))
    RanTime()
    click(Pattern("1455257719963.png").targetOffset(64,1))
    wait(2)
    click(Pattern("1455259621742.png").targetOffset(3,-98))
    type(Pattern("1455259397675.png").targetOffset(15,0),"short")
    click(Pattern("1455259712448.png").targetOffset(-40,4))
    wait(1)
    click(Pattern("1455259677162.png").targetOffset(28,38))
def PTZ_long():
    #PTZ_long
    hover(Pattern("1455257755424.png").targetOffset(-21,0))
    mouseDown(Button.LEFT)
    RanTime()
    mouseUp(Button.LEFT)
    hover(Pattern("1455257755424.png").targetOffset(20,1))
    mouseDown(Button.LEFT)
    RanTime()
    mouseUp(Button.LEFT)
    hover(Pattern("1455257755424.png").targetOffset(-2,-20))
    mouseDown(Button.LEFT)
    RanTime()
    mouseUp(Button.LEFT)
    hover(Pattern("1455257755424.png").targetOffset(-2,20))
    mouseDown(Button.LEFT)
    RanTime()
    mouseUp(Button.LEFT)
    RanTime()
    hover(Pattern("1455257719963.png").targetOffset(-103,-1))
    mouseDown(Button.LEFT)
    RanTime()
    mouseUp(Button.LEFT)
    RanTime()
    hover(Pattern("1455257719963.png").targetOffset(-79,-1))
    mouseDown(Button.LEFT)
    RanTime()
    mouseUp(Button.LEFT)
    RanTime()
    click(Pattern("1455257719963.png").targetOffset(64,1))
    wait(2)
    click(Pattern("1455259621742.png").targetOffset(3,-78))
    type(Pattern("1455259397675.png").targetOffset(15,0),"long")
    click(Pattern("1455259712448.png").targetOffset(-40,4))
    wait(1)
    click(Pattern("1455259677162.png").targetOffset(28,38))
    wait(1)

def PTZ_Preset_View(): #PTZ_Preset_View
    click(Pattern("1455257719963.png").targetOffset(90,0))
    wait(2)
    click(Pattern("1455259621742.png").targetOffset(3,-98))
    click(Pattern("1455259712448.png").targetOffset(-40,4))
    click(Pattern("1455257719963.png").targetOffset(90,0))
    wait(2)
    click(Pattern("1455259621742.png").targetOffset(3,-78))
    click(Pattern("1455259712448.png").targetOffset(-40,4))
    wait(1)

def ClientClose():    #client 종료
    click(Pattern("1455247054722.png").targetOffset(58,-19))
    wait(1)
    click(Pattern("1455247091651.png").targetOffset(30,41))



def DeviceDelete(): #장치 삭제
    click("1454380361915.png")
    wait(1)
    click(Pattern("1455166888313.png").exact().targetOffset(16,18))
    wait(1)
    keyDown(Key.CTRL+"a")
    wait(1)
    keyUp(Key.CTRL+"a")
    click(Pattern("1455166568291.png").targetOffset(92,-2))
    wait(1)
    click("1455166600239.png")

def ip(): # ip 입력
    
    doubleClick(Pattern("1454380633509.png").targetOffset(-36,0))
    type(CameraIP)
    wait(1)
def auto(): # DeviceScan 및 ID/PW 입력
    global CameraID
    global CameraPW
    click("1454380656889.png")
    wait(1)
    while True:    
        if exists("1454380688887.png"):
            click("1454380656889.png")      
        else:
            break
    click(Pattern("1454381253425.png").exact().targetOffset(8,-10))
    wait(1)
    click("1454381290995.png")
    CameraID=input(unicode("카메라 id를 입력하세요.","utf-8"))
    CameraPW=input(unicode("카메라 pw를 입력하세요.","utf-8"))
    type(CameraID+Key.TAB) #ID!
    type(CameraPW) # PW
    wait(1)
    click("1461749295384.png")
    wait(1)
    while True:        
        if exists("1462260905317.png"):
            click("1462260915394.png")
            wait(1)
            CameraID=input(unicode("카메라 id를 입력하세요.","utf-8"))
            CameraPW=input(unicode("카메라 pw를 입력하세요.","utf-8"))
            doubleClick(Pattern("1462260932006.png").similar(0.64).targetOffset(23,-6))
            type(CameraID+Key.TAB) #ID!
            type(CameraPW) # PW 
            wait(1)
            click("1461749295384.png")
            wait(1)
        else:
            break
    click("1455166085100.png")
def ScanMode(): # Scan mode 진입 및 IP Scan 선택
    global CameraIP

    click(Pattern("1454380412860.png").similar(0.94).targetOffset(108,-25))
    wait(1)
    if idis==1:
        if exists(Pattern("1454380987835.png").exact()):
            wait(1)
            click(Pattern("1454380525571.png").similar(0.91))
            wait(1)
            click(Pattern("1454380563437.png").similar(0.84).targetOffset(-70,-1))
            wait(1)
            CameraIP=input(unicode("카메라 ip를 입력하세요.","utf-8"))
    
            ip()
            auto()
            wait(3)   
        else:
            CameraIP=input(unicode("카메라 ip를 입력하세요.","utf-8"))
            ip()
            auto()
            wait(3) 
    elif idis==2: #onvif
        click(Pattern("1462255789802.png").similar(0.72).targetOffset(164,-16))
        wait(1)
        type("o")
        click(Pattern("1462255789802.png").similar(0.72).targetOffset(165,17))
        type(Key.DOWN)
        wait(1)
        CameraIP=input(unicode("카메라 ip를 입력하세요.","utf-8"))
        ip()
        auto()
        wait(3)
    elif idis==3: #axis
        click(Pattern("1462255789802.png").similar(0.72).targetOffset(164,-16))
        wait(1)
        type("a")
        click(Pattern("1462255789802.png").similar(0.72).targetOffset(165,17))
        type(Key.DOWN)
        wait(1)
        CameraIP=input(unicode("카메라 ip를 입력하세요.","utf-8"))
        ip()
        auto()
        wait(3)
    else:
        click(Pattern("1462255789802.png").similar(0.72).targetOffset(164,-16))
        wait(1)
        type("s")
        click(Pattern("1462255789802.png").similar(0.72).targetOffset(165,17))
        type(Key.DOWN)
        wait(1)
        CameraIP=input(unicode("카메라 ip를 입력하세요.","utf-8"))
        ip()
        auto()
        wait(3)

def ConfToolSite():

    click(Pattern("1462252806457.png").similar(0.96).targetOffset(90,-1))
    wait(1)
    click("1462252874103.png")

    type(SiteAddress+Key.TAB)
    wait(1)
    type(SiteAddress+Key.ENTER)
    wait(1)
    

def ConfToolStart():    #ip 복사 및 ConfTool 실행

    global SiteAddress
    SiteAddress=input(unicode("원격지 주소를 입력해주세요.","utf-8"))
    App.open("C:\IDIS Solution Suite\Client\G2ConfTool.exe")    
    wait(2)
    ConfToolSite()
    type(Key.TAB+Key.TAB)
    type("admin"+Key.TAB)
    type("12345678"+Key.ENTER)
    wait(1)
    if exists("1455775002971.png"):
        click("1455775002971.png")
    wait(1)
    click("1454380361915.png")
    wait(1)

def ClientFocus():
    App.focus("IDIS Solution Suite Client")



def ClientStart():   
    App.open("C:\IDIS Solution Suite\Client\G2Client.exe")    
    wait(10)
    type("admin"+Key.TAB)
    wait(1)
    type("12345678"+Key.ENTER)
    while True:
        if exists(Pattern("1455170137679.png").targetOffset(150,48)):
            click(Pattern("1455170137679.png").targetOffset(150,48))
            wait(1)
            while True:
                if exists("1455608640830.png"):
                    wait(1)
            
                else:
                    break
            break
        else:
            wait(1)

####################################################################################
#                        REC                                                       #
####################################################################################
def ScheduleRemove(): # 타임커버리지 스케쥴 삭제
    click(Pattern("1455171706961.png").similar(0.91).targetOffset(37,-17))
    wait(1)
    click(Pattern("1455171762169.png").targetOffset(96,45))
def ScheduleRemoveConfirm(): #녹화 스케쥴 삭제 후 확인
    wait(1)
    click(Pattern("1455173491577.png").targetOffset(-47,3))
    wait(1)
    click(Pattern("1455181784487.png").targetOffset(88,50))
def ConfToolFocus(): # ConfTool focus
    App.focus("IDIS Solution Suite Setup")
    
    
def ScheduleEnter(): #녹화 스케쥴 진입

    click(Pattern("1455173842358-1.png").similar(0.79))
    wait(1)
    click(Pattern("1455171580003.png").similar(0.96))
def ScheduleTime():
    while True:
        if exists("1455171620067.png"):
            doubleClick("1455171620067.png")
            wait(1)
            break
        else:
            ScheduleRemove()
            wait(1)
            ScheduleRemoveConfirm()
            wait(40)     # Schedule 삭제 후 40초간 대기
            ScheduleEnter()
    
    click(Pattern("1455171938827.png").similar(0.97).targetOffset(-100,4))
    wait(1)
    click(Pattern("1455171985702.png").exact().targetOffset(-1,-16))
    wait(1)

def ScheduleCondition(): #변수 정의
    global AddCondition, AddAction, AddTarget
    AddCondition = find(Pattern("1455172485495-1.png").similar(0.91))
    AddAction = find("1455173045077-1.png")
    AddTarget = find("1455173364880-1.png")
def Timelapse():
    doubleClick(AddCondition)
    wait(1)
    doubleClick("1455172850705.png")
    wait(1)
    doubleClick(AddAction)
    wait(1)
    doubleClick(Pattern("1455173093607.png").targetOffset(-1,-2))
    wait(1)
    doubleClick(AddTarget)
    wait(1)
    click(Pattern("1455173395787.png").targetOffset(-33,-1))
    wait(1)
    click(Pattern("1455173451451.png").targetOffset(57,14))
    wait(1)
    click(Pattern("1455173491577.png").targetOffset(-47,3))
    wait(30)

def StorageAdd():
    click(Pattern("1461825239518.png").similar(0.84))
    wait(1)
    doubleClick(Pattern("1455517382205.png").similar(0.86).targetOffset(2,9))
    wait(2)
    click(Pattern("1455517421567.png").targetOffset(-107,-17))
    wait(1)
    if exists("1455517778924.png"):
        click("1455517926695.png")
    else:        
        click(Pattern("1455517462613.png").similar(0.91).targetOffset(-101,-4))
        wait(1)
        doubleClick("1455517493970.png")
        wait(1)
        type("40"+Key.ENTER)
        wait(1)
        click(Pattern("1455517537753.png").targetOffset(37,54))
        while True:
            if exists("1455517592926.png"):
                wait(1)
            else:
                break
        click("1455517926695.png")                            


def MultiStreamREC():     #녹화스트림 설정 (멀티스트림)
    click("1455256519427.png")
    wait(1)
    click(Pattern("1455166888313-1.png").exact().targetOffset(16,18))
    wait(1)
    keyDown(Key.CTRL+"a")
    wait(1)
    keyUp(Key.CTRL+"a")
    click(Pattern("1455166568291-1.png").targetOffset(131,-2))
    wait(1)
    click(Pattern("1455256741013.png").similar(0.89).targetOffset(35,16))
    wait(1)
    type(Pattern("1455256780200.png").targetOffset(138,32),Key.DOWN)
    wait(1)
    type(Key.TAB)
    wait(1)
    click(Pattern("1455257029092.png").similar(0.94).targetOffset(-32,15))
    wait(1)



def MotionEventREC():  #모션 이벤트 녹화설정   
    doubleClick(AddCondition)
    wait(1)
    doubleClick("1455179326544.png")
    wait(1)
    doubleClick(AddAction)
    wait(1)
    click(Pattern("1455173093607-1.png").targetOffset(-1,-2))
    wait(1)
    type("1455180983505.png","5"+Key.ENTER)
    wait(1)
    click(Pattern("1455181038281.png").targetOffset(2,-14))
    doubleClick(AddTarget)
    
    wait(1)
    click(Pattern("1455173451451-1.png").targetOffset(57,14))
    wait(1)
    click(Pattern("1455173491577-1.png").targetOffset(-47,3))
    wait(1)

    

def PreEventREC():
    click(Pattern("1455241298474.png").exact().targetOffset(-19,-79))
    wait(1)
    
    doubleClick(AddAction)
    wait(1)
    click(Pattern("1455241904922.png").targetOffset(-111,16))
    wait(1)
    type("1455180983505.png","10"+Key.ENTER)
    wait(1)
    click(Pattern("1455181038281.png").targetOffset(2,-14))
    doubleClick(AddTarget)
    
    wait(1)
    click(Pattern("1455173451451-1.png").targetOffset(-163,-22))
    wait(1)
    click(Pattern("1455173451451-1.png").targetOffset(57,14))
    wait(1)
    
    doubleClick(AddCondition)
    wait(1)
    doubleClick(Pattern("1455241582641.png").targetOffset(-6,0))
    #프리이벤트설정 끝
    
    click(Pattern("1455173491577-1.png").targetOffset(-47,3))
    wait(1)

def TargetREC():  #연동녹화설정   
    doubleClick(AddCondition)
    wait(1)
    doubleClick("1455179326544.png")
    wait(1)
    doubleClick(AddAction)
    wait(1)
    click(Pattern("1455173093607-1.png").targetOffset(-1,-2))
    wait(1)
    type("1455180983505.png","10"+Key.ENTER)
    wait(1)
    click(Pattern("1455181038281.png").targetOffset(2,-14))
    doubleClick(AddTarget)
    wait(1)
    
    click(Pattern("1455173451451-2.png").targetOffset(-163,-22))
    wait(1)
    
    click(Pattern("1455173395787-1.png").targetOffset(-33,-1))
    wait(1)
    click(Pattern("1455173451451-2.png").targetOffset(58,13))
    wait(1)
    click(Pattern("1455173491577-1.png").targetOffset(-47,3))
    wait(1)

#########################################################################
#            Event                                                      #
#########################################################################

def EventScheduleEnter():
    click(Pattern("1455520876672.png").similar(0.90))
    wait(1)
    click(Pattern("1455171580003-1.png").similar(0.96))
    wait(1)
    while True:
        if exists("1455171620067.png"):
            doubleClick("1455171620067.png")
            wait(1)
            break
        else:
            ScheduleRemove()
    
    click(Pattern("1455171938827.png").similar(0.95).targetOffset(-100,4))
    wait(1)
    click(Pattern("1455171985702.png").exact().targetOffset(-1,-16))
    wait(1)

def EventScheduleAdd():
    doubleClick(AddCondition)
    wait(1)
    click(Pattern("1455521242599.png").targetOffset(-9,-108))
    wait(1)
    type("Event")
    wait(1)
    click(Pattern("1461813785740.png").similar(0.96).targetOffset(-10,-24))
    wait(1)
    click(Pattern("1455521624129.png").targetOffset(-63,-16))
    wait(1)
    doubleClick(Pattern("1455521654531.png").targetOffset(126,58))
    wait(1)
    doubleClick(Pattern("1455521654531.png").targetOffset(126,58))
    wait(1)
    click(Pattern("1461813984996.png").targetOffset(-64,48))
    wait(1)
    click(Pattern("1455521890545.png").targetOffset(-34,0))
    wait(1)
    if exists("1455528931080.png"):
        click(Pattern("1455528931080.png").targetOffset(151,54))
        wait(1)
        click(Pattern("1455521890545.png").targetOffset(49,0))
        wait(1)
        click(Pattern("1455529082085.png").similar(0.94))
        click(Pattern("1455521965823.png").targetOffset(-8,-13))
    else:
        click(Pattern("1455521965823.png").targetOffset(-8,-13))

def EventAck():
    doubleClick(AddAction)
    wait(1)
    click(Pattern("1455522070019.png").targetOffset(139,-38))
    wait(1)
    type(Key.UP+Key.TAB+Key.ENTER)
    wait(1)
    doubleClick(AddTarget)
    wait(1)
    click(Pattern("1455522226522.png").similar(0.79).targetOffset(-27,12))
    wait(1)
    click(Pattern("1455522306548.png").exact().targetOffset(3,37))
    wait(1)
    click(Pattern("1455522343110.png").similar(0.84).targetOffset(-43,18))

#play

def EventSearch():  #Event Search
    click(Pattern("1455247174956.png").targetOffset(-32,-3))
    wait(1)
    click("1455247229883.png")
    wait(2)
    
def Play(): #Play button 변수 정의 및 play
    PlayButton = find(Pattern("1455247337212.png").similar(0.91).targetOffset(-122,-1))
    
    click(Pattern("1455247288196.png").similar(0.93))
    wait(1)
    click(PlayButton)
    wait(20)
    click(Pattern("1455247288196.png").similar(0.93))
    type(Key.DOWN)
    click(PlayButton)
    wait(20)
    click(Pattern("1455247174956.png").targetOffset(28,-1))
    wait(1)
    click("1461808663115.png")
    wait(5)
    click(PlayButton)
    wait(30)

def Play_tab():
    click(Pattern("1455244535740.png").targetOffset(8,18))


#try:
#    ConfToolStart()
#except FindFailed:
#    popup ("notepad or ConfTool Not Find")



ConfToolStart()

# 장치 등록 및 Live(MultiStream)
popup(unicode("camera가 검색되며, 등록되는지 확인해주세요. ","utf-8"), unicode("장치등록과정","utf-8"))

items = ("idis","Onvif", "Axis", "Sony")
selected = select(unicode("Please select an item from the list","utf-8"),"Protocol", options = items)
if selected == items[0]:
    popup(unicode("idis를 선택함","utf-8"))
    idis = 1
elif selected == items[1]:
    popup(unicode("onvif 선택","utf-8"))
    idis = 2
elif selected == items[1]:
    popup(unicode("axis 선택","utf-8"))
    idis = 3
else:
    popup(unicode("sony 선택","utf-8"))
    idis = 4


ScanMode()


ClientStart()


Live_tab()

popup(unicode("실시간 영상이 표시되며, 영상의 해상도와 영상 깨짐, 영상 끊김을 확인해주세요.","utf-8"),"Live")
DevicePaneDefine()
#LayoutChange()

popup(unicode("각각의 stream 설정 시 영상이 표시되며, 영상 이상 유무를 확인해주세요.\n(스트림 설정 후 확인을 누르세요.)","utf-8"),"Multi Stream")
MultiStreamLive()

# PTZ
popup(unicode("PTZ 기능을 확인해주세요.\n(step 동작 후 continue 동작함","utf-8"),"PTZ")
PTZ_Check()


popup(unicode("이벤트 스케쥴 추가 및 (실시간 이벤트패널)이벤트 알림을 설정합니다.","utf-8"),"Event Setup")

ConfToolFocus()
EventScheduleEnter()
ScheduleCondition()
EventScheduleAdd()
EventAck()


ClientFocus()
popup(unicode("이벤트를 발생시켜 주세요.\n(이벤트 발생 후 확인을 누르세요.)","utf-8"),"Event")


# REC
popup(unicode("storage 설정 및 multistream 녹화 설정(IDIS Only), 녹화 스케쥴 설정을 시작합니다.","utf-8"),"REC Schedule Setup")
ConfToolFocus()

StorageAdd()
#popup("MultiStreamREC Setup")
if idis == 1: # idis camera면 MultiStreamREC 설정
    MultiStreamREC()
ScheduleEnter()
ScheduleTime()
ScheduleCondition()

# Timelapse

Timelapse()

ClientFocus()

multiline = '''timelapse 녹화 스케쥴이 설정되었습니다.
녹화가 시작되었는지 확인해주세요.
'''
popup(unicode(multiline,"utf-8"),"Timelapse")

# PreEvent, Event


ConfToolFocus()
ScheduleEnter()
ScheduleTime()
ScheduleCondition()

MotionEventREC()


#popup("PreEvent REC")
ScheduleEnter()
PreEventREC()
ClientFocus()
multiline = '''모션 이벤트 및 프리이벤트 녹화 스케쥴이 설정되었습니다.
이벤트를 발생시켜 주세요
(이벤트 발생 후 확인을 누르세요.)
1. 이벤트 발생 시 녹화가 시작하는지 확인
2. 녹화 스케쥴만큼 녹화 후 녹화가 정지되는지 확인
'''
popup(unicode(multiline,"utf-8"),"Event REC")
ConfToolFocus()
ScheduleEnter()
ScheduleTime()
TargetREC()
ClientFocus()
multiline = '''연동 녹화 스케쥴이 설정되었습니다.
이벤트를 발생시키고 하기 항목을 확인해주세요.
(녹화가 정지됨을 확인하고 확인버튼을 누르세요.)
1. 이벤트 발생 시 녹화가 시작하는지 확인
2. 녹화 스케쥴만큼 녹화 후 녹화가 정지되는지 확인
'''
popup(unicode(multiline,"utf-8"),"Target REC")


multiline = '''녹화된 영상이 재생되오니, 하기 내용을 확인해주세요.
1. 녹화 스케쥴 설정대로 녹화되었는지 확인
2. 이벤트 발생 구간을 기점으로 Stream 변경 확인 및 영상 이상 유/무 확인
3. 재생 중 영상깨짐 유/무 확인
'''
popup(unicode(multiline,"utf-8"),"Play Test")

Play_tab()
DevicePaneDefine()
EventSearch()
Play()

popup(unicode("장치 삭제 및 client 종료","utf-8"),"Device Delete")
wait(10)
ConfToolFocus()
DeviceDelete()
ClientClose()
wait(10)
popup(unicode("Test가 완료되었습니다.","utf-8"),"Test")


 