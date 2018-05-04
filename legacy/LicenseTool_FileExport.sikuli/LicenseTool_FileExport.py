while True:
    click(Pattern("1447405624365.png").similar(0.95))
    wait(1)
    type(Pattern("1447406106400.png").similar(0.96).targetOffset(55,0),"1")
    wait(1)
    click("1447405657168.png")
    wait(1)
    click("1447405673901.png")
    while True:
        if exists("1447405688294.png"):
            click("1447405720147.png")
            break
        else:
            wait(1)
        