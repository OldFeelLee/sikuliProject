import datetime

pane = find("1462864774894.png")
device = find(Pattern("1462864085559.png").similar(0.91))

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

while True:
    dragDrop(device,pane)
    wait(10)
    click(Pattern("1462864238481.png").targetOffset(-17,0))
    wait(5)
    click("1462873465825.png")
    wait(10)
    f= open("c:/a/Redundant.txt",'a')
    if exists(Pattern("1462865061703.png").exact()):
        Time()
        f.write(s+"    complete!\n")

    else:
        Time()
        f.write(s+"    fail!\n")
    f.close()        
    type(Key.ALT+"s")
    wait(1)
    type("r")
    type("a")
    wait(10)
            
        