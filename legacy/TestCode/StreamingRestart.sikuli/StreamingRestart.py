from sikuli import Mail


def Restart():    
    click(Pattern("1482136474829.png").similar(0.59))
    wait(1)
    type("streaming")
    wait(1)
    click("1482136537849.png")
    wait(1)
    click("1482136565146.png")
    wait(20)
    rightClick(Pattern("1482136633736.png").targetOffset(-97,1))
    wait(1)
    click("1482136656962.png")
    while not exists(Pattern("1482139858787.png").similar(0.93)):
        wait(1)

def Play():
    cnt=0
    while True:
        cnt=cnt+1   
        Restart()
        f= open("c:/a/Streaming2.txt",'a')
        Mail.Time()
        f.write(s+"    '%s'    OK!\n" % cnt)
        f.close()
        if e<today:
            run("d:\sikuli\gr1mailtest.bat")
    
            break

Mail.Time2()
Play()



