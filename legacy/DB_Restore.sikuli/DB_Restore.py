def restore():
    click("1452678573156.png")
    wait(2)
    click(Pattern("1452678590878.png").targetOffset(54,50))
    wait(2)
    click(Pattern("1452678658215.png").targetOffset(166,-168))
    wait(2)
    click("1452764343165.png")
    wait(1)
    click("1452678714288.png")
    wait(1)
    click("1452678736626.png")


while True:
    while True:
        if exists(Pattern("1452678778391.png").similar(0.88).targetOffset(36,120)):
            if exists(Pattern("1452679677465.png").exact()):
                click(Pattern("1452678778391.png").similar(0.88).targetOffset(36,120))
                break
            else:
                wait(1)
        else:
            wait(1)
    while True:
        if exists(Pattern("1452764376168.png").exact()):         
            restore()
            break
        else:
            wait(1)
        
        