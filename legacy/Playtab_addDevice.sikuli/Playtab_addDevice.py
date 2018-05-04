
def doTest() :    
    global errorReason
   

    
    try:
        device = find("1437640795961.png")
        pane = find("1437640500582.png")
          
        
        exists("1437640500582.png",5)
        if pane == None:             
            onChange(rightClick())
            wait(2)
            hover("1437644670884.png")
            wait(1)
            click("1437644687265.png")
            wait(1)
 #          rightClick(paneClone)
        else :
            dragDrop(device,pane) 
            
     
       
      
        return True
    except FindFailed :
        errorReason = "no target "
        return False
    
while True :
    if doTest() == False :
        alert(errorReason)
        wait(1)