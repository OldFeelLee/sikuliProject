import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

while True:

    App.open("D:\INIT\Pro_1604041716\Pro INIT.exe")
    while True:
        if exists("1459764127992.png"):
            click("1459764132370.png")
            break
        else:
            wait(1)
            
    Time()
    f= open("c/a/d.txt,'a'")
    f.write(s+"    complete!")
    f.close()
    keyDown(Key.ALT)
    type(Key.F4)
    keyUp(Key.ALT)
    wait(30)