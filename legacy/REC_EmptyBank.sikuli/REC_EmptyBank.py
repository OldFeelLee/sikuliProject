empty = find ("1439946778668.png")
axis = find(Pattern("1439881313814.png").exact())
PlayButton = find(Pattern("1439880450997.png").similar(0.96))
while True:
    dragDrop(axis,empty)
    while True:
        if exists(Pattern("1440068323398.png").similar(0.94)):

            break
        else:
            wait(2)
 

    click(PlayButton)

    