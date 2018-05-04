import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

try:
    App.open("C:\IDIS Solution Suite\Client\G2Client.exe")
    while not exists("1484038689399.png"):
        wait(1)
    App.focus("IDIS Solution Suite Client")
    type(Pattern("1484026887173.png").similar(0.92),"12345678"+ Key.ENTER)
    while not exists("1484027016886.png"):
        wait(1)
    click(Pattern("1484027016886.png").targetOffset(150,55))
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    Client Login Complete!\n")
    f.close() 

except FindFailed:
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    Client Login fail!\n")
    f.close()    
 