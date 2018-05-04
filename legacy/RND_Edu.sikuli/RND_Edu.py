
def choice():
#    if num == 1:
    click(Pattern("1481004529281.png").similar(0.52).targetOffset(194,-58))
    wait(10)
    while True:
        if find(Pattern("1481005292522.png").exact()):
            
            click(Pattern("1481005292522.png").exact())
            wait(1)
        else:
            click("1481004731162.png")
            wait(1)

def StudyPage():
    while True:     
        if exists(Pattern("1481002030794.png").similar(0.89)):
            click(Pattern("1481002030794.png").similar(0.89))
            break
        else:
            type(Key.DOWN)
            wait(1)
            if exists(Pattern("1481005952807.png").exact()):
                break


def edu():
#    StudyPage()
    cnt = 0
    button = find(Pattern("1480999766694.png").similar(0.69))
    while True:
        if exists(Pattern("1481000349836.png").exact()):  
            wait(2)
            click(button)
            cnt = 0
            
        else:
            wait(1)
            cnt = cnt +1              
            strcnt = str(cnt)
            '''
            f= open("c:/a/test.txt",'a')
            f.write(strcnt+"\n")
            f.close()
            '''
            
            if exists(Pattern("1481001243339.png").similar(0.88)):
                wait(1)
                click(Pattern("1481001243339.png").similar(0.88))
                wait(5)
                click(button)
            elif exists(Pattern("1481001718335.png").similar(0.73)):
                wait(1)
                click(Pattern("1481001900097.png").similar(0.90))
                wait(2)
                StudyPage()
            elif exists("1481007301080.png"):
                wait(3)
                click(Pattern("1481007301080.png").targetOffset(-99,3))
                wait(3)
                click("1481007482397.png")
            elif exists("1481074868733.png"):
                click(Pattern("1481074868733.png").targetOffset(200,119))
                wait(40)
                click(Pattern("1481074946984.png").targetOffset(16,70))
            elif exists("1481079197510.png"):
                wait(1)
                click("1481079197510.png")
                wait(3)
                click("1481079308808.png")
                
            elif cnt==10:
                click(button)
                cnt=0
                
                


#choice()

edu()