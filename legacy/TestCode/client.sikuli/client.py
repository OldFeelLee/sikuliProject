from guide import *

while not exists(Pattern("1481794539590.png").similar(0.97)):
    click(Pattern("1481794460344.png").targetOffset(0,11))
    '''
    if exists("1481795270892.png"):
        text("1481795270892.png", "Find")
        show(3)
    '''        
    while not exists("1481795270892.png"):
        if exists(Pattern("1481794494943.png").similar(0.91)):
                click(Pattern("1481794494943.png").similar(0.91))
        wait(1)
    wait(5)
    click("1481795270892.png")
    
            