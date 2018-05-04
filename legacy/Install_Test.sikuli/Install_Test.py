while True:
    doubleClick(Pattern("1438232040368.png").exact())
    wait(2)
    click(Pattern("1438231337553.png").targetOffset(24,10))
    button = find("1438231462550.png")
    onAppear("1438231445032.png",click(button))
    
    onAppear("1438231501996.png",click(button))
    onAppear("1438231610744.png",click(button))
    onVanish(Pattern("1438231955612.png").exact(),click(Pattern("1438231795632.png").similar(0.80).targetOffset(-76,2)))
    wait(1)
    click(button)
    wait(1)
    click(button)
    