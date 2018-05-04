empty = find("1452242951814-4.png")
playbutton = find(Pattern("1440749921529.png").similar(0.85))
flag = 0

while True:

    if flag == 0:
        while True :
            if exists(Pattern("1439343972471.png").exact().targetOffset(7,12)):
                if exists("1452242951814.png"):
                    dragDrop(Pattern("1439343972471.png").exact().targetOffset(7,12),"1452242951814-1.png")
                    while True:
                        if exists(Pattern("1440750889470.png").similar(0.97)):
                            click(playbutton)
                            break
                        else:
                            wait(1)
                else:
                    rightClick(empty)
                    wait(1)
                    hover("1452244705021.png")
                    wait(1)
                    click("1452244722917.png")             

            else :
                flag =1
                break
    if flag == 1:
        while True :
            if exists(Pattern("1439345934972.png").exact().targetOffset(-1,-13)):
                if exists("1452242951814-2.png"):
                    dragDrop(Pattern("1439345934972.png").exact().targetOffset(-1,-13),"1452242951814-3.png")
                    while True:
                        if exists(Pattern("1440750889470.png").similar(0.97)):
                            click(playbutton)
                            break
                        else:
                            wait(1)                    
                else:
                    rightClick(empty)
                    wait(1)
                    hover("1452244556561.png")
                    wait(1)
                    click("1452244566617.png")             

            else :
                flag =0
                break
            


