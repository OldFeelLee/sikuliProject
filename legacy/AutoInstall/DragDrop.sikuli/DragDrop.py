click(Pattern("1486533725403.png").targetOffset(1,-2))

if exists(Pattern("1484027139115-1.png").similar(0.89)):
    dragDrop(Pattern("1484027139115.png").similar(0.88),"1486533839889.png")

else:    
    doubleClick("1484027117697.png")
    dragDrop(Pattern("1484027139115.png").similar(0.88),"1486533839889.png")


