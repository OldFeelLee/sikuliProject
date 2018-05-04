import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)


try:
    App.focus("iNEX Setup")
    App.focus("IDIS Solution Suite Setup")
    click(Pattern("1484012552582.png").similar(0.78))
    doubleClick("1484012573707.png")
    click("1484012599714.png")
    click("1484012615797.png")
    wait(1)
    type(Key.DOWN)
    type(Key.DOWN)
    click("1484012731288.png")
    click("1484012755437.png")
    click("1484012777957.png")
    while not exists("1484012815560.png"):
        wait(1)
    click("1484013274945.png")
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    Storage add complete!\n")
    f.close()
except FindFailed:
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    Storage add fail!\n")
    f.close()