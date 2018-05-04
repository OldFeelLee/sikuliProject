import random
import string

def RanTime():    #random 시간
    ran = "".join([random.choice(string.digits)])
    s=int(ran)
    wait(s)

def Live_tab():
    if exists("1455609384135.png"):
        click(Pattern("1455609384135.png").targetOffset(-61,-63))

def DevicePaneDefine(): #device, pane 변수 정의 및 pane에 device 추가
    global pane
    global device
    if exists(Pattern("1455170393643.png").similar(0.98).targetOffset(18,13)):
        wait(1)
        device = find(Pattern("1455170393643.png").similar(0.98).targetOffset(18,13))
        pane = find("1455258060501.png")
        dragDrop(device,pane)
        wait(3)
    else:        
        click(Pattern("1455170236648.png").similar(0.85).targetOffset(-41,-1))
        wait(1)
        device = find(Pattern("1455170393643.png").similar(0.98).targetOffset(18,13))
        pane = find("1455258060501.png")
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
        PTZ_short()
        PTZ_long()
        PTZ_Preset_View()    

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

def ip(): # ip 붙여넣기
    click("1454380633509.png")
    keyDown(Key.CTRL+"v")
    keyUp(Key.CTRL+"v")
    wait(1)
def auto(): # DeviceScan 및 ID/PW 입력
    click("1454380656889.png")
    wait(5)
    while True:    
        if exists("1454380688887.png"):
            click("1454380656889.png")      
        else:
            break
    click(Pattern("1454381253425.png").exact().targetOffset(8,-10))
    wait(1)
    click("1454381290995.png")
    type("admin"+Key.TAB) #ID!
    type("") # PW
    wait(1)
    click("1454381375243.png")
    wait(1)
    click("1455166085100.png")
def ScanMode(): #DeviceScan mode 진입 및 IP Scan 선택
    click(Pattern("1454380412860.png").similar(0.94).targetOffset(108,-25))
    wait(1)
    if exists(Pattern("1454380987835.png").exact()):
        wait(1)
        click(Pattern("1454380525571.png").similar(0.91))
        wait(1)
        click(Pattern("1454380563437.png").similar(0.84).targetOffset(-70,-1))
        wait(1)
        ip()
        auto()
        wait(10)
    
    else:
        ip()
        auto()
        wait(10)    
def ConfToolStart():    #ip 복사 및 ConfTool 실행

    keyDown(Key.WIN+"r")
    keyUp(Key.WIN+"r")
    wait(1)
    type("notepad"+Key.ENTER)
    wait(1)
    type("10.0.127.194")    # ip 입력부분 카메라별로 수정 필요
    keyDown(Key.CTRL+"a")
    wait(1)
    keyUp(Key.CTRL+"a")
    keyDown(Key.CTRL+"c")
    wait(1)
    keyUp(Key.CTRL+"c")
    doubleClick(Pattern("1455263103828.png").similar(0.59))
    wait(2)
    type("12345678"+Key.ENTER)
    wait(1)
    click(Pattern("1455263196292.png").targetOffset(134,48))
    wait(1)
    click("1454380361915.png")
    wait(1)
def ClientStart():   
    wait(1)
    doubleClick("1455169924492.png")
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

def ConfToolEnter(): #ConfTool 진입
    click(Pattern("1455173660011.png").targetOffset(21,11))
    wait(1)
    click("1455173674996.png")
    wait(1)
    
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


def StorageAdd():
    click("1455517351203.png")
    wait(1)
    doubleClick(Pattern("1455517382205.png").similar(0.86).targetOffset(2,9))
    wait(2)
    click(Pattern("1455517421567.png").targetOffset(52,-15))
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
    click(Pattern("1455256741013.png").similar(0.88).targetOffset(35,16))
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
    type("1455180983505.png","10"+Key.ENTER)
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
    type("1455180983505.png","20"+Key.ENTER)
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
    
    click(Pattern("1455171938827.png").similar(0.97).targetOffset(-100,4))
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
    click(Pattern("1455521392387.png").similar(0.91).targetOffset(-33,-32))
    wait(1)
    click(Pattern("1455521624129.png").targetOffset(-63,-16))
    wait(1)
    doubleClick(Pattern("1455521654531.png").targetOffset(126,58))
    wait(1)
    click(Pattern("1455521710124.png").targetOffset(-121,53))
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
    wait(10)
    click(Pattern("1455247288196.png").similar(0.93))
    type(Key.DOWN)
    click(PlayButton)
    wait(10)

def Play_tab():
    click(Pattern("1455244535740.png").targetOffset(8,18))


#try:
#    ConfToolStart()
#except FindFailed:
#    popup ("notepad or ConfTool Not Find")

#popup("ConfTool Start")
#wait(3)
#type(Key.ENTER)
#ConfToolStart()

# 장치 등록 및 Live(MultiStream)

#ScanMode()
#ClientStart()
#Live_tab()
#DevicePaneDefine()
#LayoutChange()
#MultiStreamLive()

# PTZ

PTZ_Check()


ConfToolEnter()
EventScheduleEnter()
ScheduleCondition()
EventScheduleAdd()
EventAck()


# REC
ConfToolEnter()
StorageAdd()
ScheduleEnter()
ScheduleTime()
ScheduleCondition()

# Timelapse
Timelapse()

# MultiStream, PreEvent, Event


MultiStreamREC()

ScheduleEnter()
ScheduleTime()
ScheduleCondition()

MotionEventREC()

ScheduleEnter()
PreEventREC()

ScheduleEnter()
ScheduleTime()
TargetREC()


Play_tab()
DevicePaneDefine()
EventSearch()
Play()


ConfToolEnter()
DeviceDelete()
ClientClose()


 