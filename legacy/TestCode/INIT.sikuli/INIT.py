import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

while True:
    App.open("D:\INIT\Pro_1604041716\Pro INIT.exe")
       
    while True:
        if exists("1459764679056.png"):
            click("1459764692389.png")
            break
        else:
            if exists(Pattern("1459764848460.png").similar(0.90).targetOffset(51,35)):
                click(Pattern("1459764848460.png").similar(0.90).targetOffset(51,35))
            wait(1)
   
    Time()
    f= open("c:/a/d.txt",'a')
    f.write(s+"    complete!\n")
    f.close()
    wait(10)
    click(Pattern("1459765043012.png").similar(0.85).targetOffset(29,-15))
    wait(60)
