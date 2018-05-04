
def doTest() :  

    global errorReason

    try:
       
 
        click(Pattern("1437727533856.png").exact())
        wait(2)
        type(Pattern("1437705801315.png").exact().targetOffset(-3,13),"ax")
        wait(2)
        if flag == 1:
           click(Pattern("1437705854123.png").exact().targetOffset(-53,0))
           flag = 0
           wait(2)
           click("1437730277374.png")
           wait(2)
        else:
           click(Pattern("1437705968665.png").exact().targetOffset(-52,-1))
           flag = 1
           wait(2)
           click("1437730277374.png")
           wait(2)
        return True
    except FindFailed :
        errorReason = "no target resolution or framerate"
        return False

        errorReason = "Unknown"
 while True :
    if doTest() == False :
        alert(errorReason)
        wait(1)