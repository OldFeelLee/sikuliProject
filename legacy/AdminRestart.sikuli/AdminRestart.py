while True :
    admin = find("1438850456827.png")
    rightClick(admin) 
    wait(1)
    click(Pattern("1438850477054.png").targetOffset(-29,-51))
       
    wait(1)
    onAppear("1438850525092.png",click("1438850536993.png"))
    wait(30)
    rightClick(Pattern("1438850676036.png").similar(0.92).targetOffset(-15,16))
    wait(2)
    click("1438851185831.png")
    wait(30)