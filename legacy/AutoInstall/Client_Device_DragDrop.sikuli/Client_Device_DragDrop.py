
def if_exists_dragDrop(image1,image2,image3):
    click(Pattern("1486533725403.png").targetOffset(1,-2))            
    if exists(image1):
        dragDrop(image1,image2)
    else:
        doubleClick(image3)
        dragDrop(image1,image2)

oem=open("c:/sikuli/TestResult.txt").read(1)
if oem == "I":
    click(Pattern("1486533725403.png").targetOffset(1,-2))
    if_exists_dragDrop(Pattern("1484027139115-1.png").similar(0.89), "1486533839889.png","1484027117697.png")  
    
else:
    click(Pattern("1486533725403.png").targetOffset(1,-2))
    
    if_exists_dragDrop(Pattern("1484027139115.png").similar(0.88),"1486538171323.png","1484027117697.png")
    
    
