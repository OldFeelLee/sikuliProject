flag=1
while True:
    click(Pattern("1469433598115.png").targetOffset(-34,37))
    while True: 
        if exists("1469433629573.png"):
            break
        else:
            wait(1)
    click(Pattern("1469433629573.png").targetOffset(-267,-39))
    wait(1) 
    click(Pattern("1469433714919.png").similar(0.94).targetOffset(-31,39))
    if flag == 1:
        type(Key.DOWN+Key.ENTER)
        wait(1)
        flag=0
    else:
        type(Key.UP+Key.ENTER)
        wait(1)
        flag=1
    click(Pattern("1469433827825.png").targetOffset(-72,5))
    wait(1)
    click(Pattern("1469434000693.png").targetOffset(26,43))
    while exists("1469434033969.png"):
        wait(1)
    type("1469434033969.png",Key.ENTER)
    while True:
        if exists(Pattern("1469434153466.png").exact()):
            break
        else:
            wait(1)