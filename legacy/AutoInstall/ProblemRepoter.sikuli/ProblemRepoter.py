import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)


try:
    App.open("C:\IDIS Solution Suite\Client\G2ProblemReporter.exe")
    while not exists("1484036163256.png"):
        wait(1)
    click(Pattern("1484036163256.png").targetOffset(36,11))
    click(Pattern("1484036399623.png").targetOffset(-54,-1))
    while not exists("1484036446389.png"):
        wait(1)
    click("1484036217803.png")
    while not exists("1484036247515.png"):
        wait(1)
    click("1484036284781.png")
    App.focus("Problem Reporter")
    click("1484036338285.png")
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    Problem Reporter complete!\n")
    f.close() 

except FindFailed:
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    Problem Reporter fail!\n")
    f.close() 
