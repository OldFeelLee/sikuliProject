while True:
    click(Pattern("1449652409041.png").similar(0.94).targetOffset(107,-8))
    wait(2)
    keyDown(Key.SHIFT+Key.CTRL+Key.ALT)
    wait(3)
    click("1449649878404.png")
    wait(2)
    keyUp(Key.SHIFT+Key.CTRL+Key.ALT)
    click(Pattern("1449651370216.png").similar(0.86).targetOffset(63,-2))
    wait(1)
    click("1449651446928.png")
    wait(1)
    click(Pattern("1449651470101.png").targetOffset(18,-2))
    wait(1)
    keyDown(Key.CTRL+"a")
    wait(1)
    keyUp(Key.CTRL+"a")
    wait(1)
    type("20")
    wait(1)
    click("1449651630401.png")
    while True:
        if exists(Pattern("1481699974182.png").exact()):
            click("1449651659394.png")
            break
        else:
            wait(1)

    while True:
        if exists("1481699828877.png"):
#        if exists("1449652000950.png"):
            wait(1)
        else:
            click("1481700111227.png")
            wait(1)
            keyDown(Key.CTRL+"a")
            wait(1)
            keyUp(Key.CTRL+"a")
            wait(1)
            click(Pattern("1449652204904.png").exact().targetOffset(87,-18))
            wait(1)
            click("1449652247572.png")
            break
    while True:
        if exists("1481700001299.png"):
            wait(1)
        else:
            break