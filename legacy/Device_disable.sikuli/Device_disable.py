flag = 1
while True:
    doubleClick("1437991813315.png")
    wait(2)
    if flag == 1:
        click(Pattern("1437991831708.png").targetOffset(-37,0))
        wait(1)
        click("1437991915571.png")
        wait(4)
        flag = 0
    else:
        click(Pattern("1437991976622.png").targetOffset(-38,0))
        wait(1)
        click("1437991915571.png")
        wait(4)
        flag = 1
        