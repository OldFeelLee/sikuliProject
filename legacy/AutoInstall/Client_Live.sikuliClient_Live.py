import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)


try:
    App.focus("IDIS Solution Suite Client")
    click(Pattern("1484031077942.png").similar(0.94))
    click(Pattern("1484031221469.png").exact().targetOffset(-23,0))


    if exists(Pattern("1484027139115.png").similar(0.89)):
        device = find(Pattern("1484027139115.png").similar(0.89))
        pane = find(Pattern("1484031272691.png").similar(0.88))
        dragDrop(device,pane)
        if not exists(Pattern("1484031388904.png").similar(0.88)):
            if exists("1484032115779.png"):
                wait(5)
                Time()
                f=open("c:/a/install.txt",'a')
                f.write(s+"    Streaming_Device NotConnected!\n")
                f.close()
            else:
                Time()
                f=open("c:/a/install.txt",'a')
                f.write(s+"    Live Complete!\n")
                f.close()                   
                
            rightClick(pane)
            click("1484031561458.png")
            click("1484031583576.png")


    else:
        doubleClick("1484027117697.png")
        device = find(Pattern("1484027139115.png").similar(0.89))
        pane = find(Pattern("1484031272691.png").similar(0.88))
        dragDrop(device,pane)
        if not exists(Pattern("1484031388904.png").similar(0.88)):
            if exists("1484032115779.png"):
                wait(5)
                Time()
                f=open("c:/a/install.txt",'a')
                f.write(s+"    Streaming_Device NotConnected!\n")
                f.close() 

            else:
                Time()
                f=open("c:/a/install.txt",'a')
                f.write(s+"    Live Complete!\n")
                f.close()     
 
                
            rightClick(pane)
            click("1484031561458.png")
            click("1484031583576.png")      

except FindFailed:
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    Live failed!\n")
    f.close() 
