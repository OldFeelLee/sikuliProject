
while True:
    click(Pattern("1456911223266.png").targetOffset(219,-2))
    wait(60)
    if exists(Pattern("1456910933654.png").similar(0.96)):
        rightClick(Pattern("1456910728916.png").similar(0.92))
        wait(1)
        click(Pattern("Admin.png").similar(0.94))
        wait(20)
    else:
        break