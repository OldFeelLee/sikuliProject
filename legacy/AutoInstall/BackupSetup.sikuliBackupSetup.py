import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

try:
    App.focus("IDIS Solution Suite Setup")
    click("1484028992465.png")
    wait(1)
    doubleClick("1484029034988.png")
    while not exists("1484029097236.png"):
        wait(1)
    click("1484029119976.png")
    click("1484029150212.png")
    click(Pattern("1484029173037.png").targetOffset(-38,-2))
    click(Pattern("1484029203546.png").exact().targetOffset(-57,1))
    click(Pattern("1484029240476.png").targetOffset(-41,-1))
    while not exists(Pattern("1484029277359.png").targetOffset(25,30)):
        wait(1)
    click(Pattern("1484029277359.png").targetOffset(25,30))
    click(Pattern("1484029349565.png").targetOffset(167,73))
    click(Pattern("1484029382020.png").targetOffset(-53,-13))
    doubleClick("1484029416250.png")
    click(Pattern("1484029438876.png").targetOffset(-35,1))
    click(Pattern("1484029463734.png").targetOffset(171,31))
    click(Pattern("1484029491300.png").similar(0.96).targetOffset(-33,-35))
    click(Pattern("1484029529925.png").targetOffset(-47,2))
    click(Pattern("1484029574945.png").targetOffset(167,30))
    click("1484029597521.png")
    wait(1)
    type(Key.DOWN)
    type(Key.DOWN)
    click("1484012731288.png")
    click("1484029731994.png")
    click("1484030159947.png")
    while not exists("1484030722944.png"):
        wait(1)
    click("1484030610390.png")
    
    click("1484030265938.png")

    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    BackupSetup complete!\n")
    f.close() 
    

except FindFailed:
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    BackupSetup fail!\n")
    f.close()     


    