while True:
    wait(1)
    click("1456307787295.png")
    while True:
        if exists(Pattern("1456307413548.png").similar(0.76)):
            wait(1)
        else:
            break
    
    dragDrop(Pattern("1456307506848.png").similar(0.80),"1456307551105.png")
    wait(5)
    click("1456307686788.png")
    wait(1)
    click("1456307710609.png")
    wait(1)
    click(Pattern("1456307732010.png").targetOffset(9,6))
