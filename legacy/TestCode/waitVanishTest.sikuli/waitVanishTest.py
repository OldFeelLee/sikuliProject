def waitVanish_click(image):
    wait(image, FOREVER)
    try:
        while exists(image, 10):
            type(image,Key.ENTER)
            
            wait(1)
    except:
        wait(1) #noop.


waitVanish_click(Pattern("1486617477531.png").exact())