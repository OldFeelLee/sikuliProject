
def doTest() :    
    global errorReason
    try:
        for a in range(0,5,1): 
      #      cmd = find("1437541586044.png")
       #     cmd.click()
            type(Pattern("1437541586044.png").similar(0.93),"g2client.exe --run-multiple" + Key.ENTER) 
            wait(200)
        for b in range(0,5,1):
            click(Pattern("1437542937681.png").exact().targetOffset(18,-17))
            wait(2)
            click(Pattern("1437542982419.png").similar(0.83))
            wait(20)      
# for a in range(0,10,3):

  
        return True
    except FindFailed :
        errorReason = "no target resolution or framerate"
        return False

        errorReason = "Unknown"
while True :
    if doTest() == False :
        alert(errorReason)
        wait(1)