while True:
    if exists(Pattern("1443693572298.png").exact()):
        click(Pattern("1443693572298.png").exact())
        wait(1)
        click(Pattern("1443693624254.png").exact())
    else:
        wait(5)
        