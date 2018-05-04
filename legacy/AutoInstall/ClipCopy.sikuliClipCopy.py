import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

try:

    App.focus("IDIS Solution Suite Client")
    
    click("1484027094439.png")
    if exists(Pattern("1484027139115-1.png").similar(0.89)):
        dragDrop(Pattern("1484027139115.png").similar(0.88),"1484040020186.png")

    else:    
        doubleClick("1484027117697.png")
        dragDrop(Pattern("1484027139115.png").similar(0.88),"1484040020186.png")
    while not exists("1484027262854.png"):
        wait(1)
    click(Pattern("1484027311485.png").similar(0.97))
    click("1484027347052.png")
    click(Pattern("1484027382166.png").similar(0.94).targetOffset(-15,-9))
    click(Pattern("1484027382166.png").similar(0.94).targetOffset(5,-6))
    click(Pattern("1484027445851.png").similar(0.92))
    click("1484027480963.png")
    while not exists("1484027528160.png"):
        wait(1)
    click(Pattern("1484027549980.png").similar(0.95))
    while not exists("1484027583202.png"):
        wait(1)
    click(Pattern("1484027612596.png").targetOffset(127,45))
    click(Pattern("1484027640260.png").targetOffset(45,0))
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    ClipCopy Complete!\n")
    f.close() 

except FindFailed:
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    ClipCopy fail!\n")
    f.close() 
    