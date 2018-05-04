import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

while True:
    App.open("D:\INIT\Pro_1604041716\Pro INIT.exe")
   
    while True:
         if exists(Pattern("D:/Sikuli/script/INIT_test.sikuli/1459762808742.png").similar(0.89)):
             click(Pattern("D:/Sikuli/script/INIT_test.sikuli/1459762840696.png").similar(0.87))
             break
        else:
            wait(1)
   
    Time()
    f= open("c/a/d.txt,'a')
    f.write(s+"    complete!")
    f.close()
    keyDown(Key.ALT)
    type(Key.F4)
    keyUp(Key.ALT)
