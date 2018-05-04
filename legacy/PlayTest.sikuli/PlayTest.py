
def doTest() :    
    global errorReason
    try:
        playTab = find(Pattern("1434533736399.png").exact())
        playTab2 = find("1434447787800.png")
        
        obj = exists("1434437263056.png",5)
        if obj != None :
            dragDrop(obj, playTab)
        wait(2)
        playTab.doubleClick()
        wait(5)
        playTab.doubleClick()
        wait(5)
        playTab.rightClick()
        wait("1434448832344.png")
        hover("1434448832344.png")
        click("1434448848764.png")
        wait(5)
        playTab2.click()
        return True
    except FindFailed :
        errorReason = "no target resolution or framerate"
        return False

        errorReason = "Unknown"
while True :
    if doTest() == False :
        alert(errorReason)
        wait(1)
        
                
    