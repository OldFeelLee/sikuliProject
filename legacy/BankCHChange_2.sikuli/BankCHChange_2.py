
def doTest() :    
    global errorReason
    try:
        rightClick(Pattern("1434933988801.png").exact())
        wait(1)
        click("1434934034521.png")
        wait(40)        
        click(Pattern("1434934184434.png").targetOffset(36,120))
        wait(3) 
        click("1434620993343.png")
        wait(2)
        click(Pattern("1434602091691.png").exact())
        wait(2)
        click("1434602134910.png")
        wait(10)
        doubleClick(Pattern("1434602229019.png").exact())
        wait(2)
        click(Pattern("1434602318724.png").exact())
        wait(1)
        click(Pattern("1434602957190.png").exact())
        wait(1)
        click("1434602402679.png")
        wait(1)
        click("1434602427102.png")
        wait(1)
        click(Pattern("1434602453569.png").exact())
        wait(1)
        ok = find("1434602493251.png")
        ok.click()
        wait(1)
        ok.click()
        wait(5)
        click(Pattern("1434934341909.png").targetOffset(147,-8))
        wait(10)
        return True
    except FindFailed :
        errorReason = "no target resolution or framerate"
        return False

        errorReason = "Unknown"
while True :
    if doTest() == False :
        alert(errorReason)
        wait(1)
        
                
    