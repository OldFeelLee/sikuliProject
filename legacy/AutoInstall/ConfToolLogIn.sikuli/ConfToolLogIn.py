
#def ConfToolStart():    #ip 복사 및 ConfTool 실행
doubleClick("1483686728732.png")
global a
a= 1
wait(2)
type("12345678"+Key.ENTER)
wait(1)
if exists("1455775002971.png"):
    click("1455775002971.png")
wait(1)
click("1454380361915.png")
wait(1)

def ScanMode(): # Scan mode 진입 및 IP Scan 선택
    a= 2

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
        wait(3)   
    else:

        ip()
        auto()
        wait(3) 


def ip(): # ip 입력
    
    doubleClick(Pattern("1454380633509.png").targetOffset(-36,0))
    type("10.0.127.114")
    wait(1)
    
def auto(): # DeviceScan 및 ID/PW 입력

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

    type("admin"+Key.TAB) #ID!
    type("pylon") # PW
    wait(1)
    click("1461749295384.png")
    wait(1)
    click("1455166085100.png")



#ConfToolStart()

#ScanMode()

#print a