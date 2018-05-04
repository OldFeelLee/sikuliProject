import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def success():
    f=open("c:/a/client.txt",'a')
    f.write(s+"    ServiceDB Import complete!\n")
    f.close()  

def failed():
    f=open("c:/a/client.txt",'a')
    f.write(s+"    "+" fail!\n")
    f.close() 


def click_until_show(clickimage, showimage):
    while not exists(showimage, 1):
        click(clickimage)
        wait(1)

def play():
    while True:
        click_until_show("1486631807563.png", "1486631839773.png")
        
        hover("1486631726030.png")
        click("1486631730312.png")
        click("1486631735599.png")
        if exists(Pattern("1486631859280.png").targetOffset(33,122),FOREVER):
            click(Pattern("1486631859280.png").targetOffset(33,122))

try:
    Time()
    f=open("c:/a/client.txt",'w')
    f.write(s+"    start!\n")
    f.close()  
    play()

except FindFailed:
    Time()
    failed()
