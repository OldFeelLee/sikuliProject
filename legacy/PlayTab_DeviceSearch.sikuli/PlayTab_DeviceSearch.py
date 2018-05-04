empty = find("1452242951814.png")

while True:
    if exists("1452242951814.png"):
        if exists(Pattern("1439343972471.png").exact().targetOffset(7,12)):
            dragDrop(Pattern("1439343972471.png").exact().targetOffset(7,12),"1452242951814.png")
        else:
            dragDrop(Pattern("1439344247546.png").exact().targetOffset(7,-13),"1452242951814.png")
    else :
        rightClick(empty)
        wait(1)
        hover("1452242989203.png")
        wait(1)
        click("1452243002311.png")

