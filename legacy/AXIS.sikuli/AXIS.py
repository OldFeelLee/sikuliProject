
def doTest() :    
    global errorReason
    try:
        click("1437728549609.png")
        
 

        return True
    except FindFailed :
        errorReason = "no target resolution or framerate"
        return False

        errorReason = "Unknown"
while True :
    if doTest() == False :
        alert(errorReason)
        wait(1)