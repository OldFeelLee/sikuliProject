playbutton = find(Pattern("1439192614694.png").exact())
count = 0
while True:


    
#    click(Pattern("1439192421160.png").exact().targetOffset(-1,10))
    click(Pattern("1439348450569.png").similar(0.98).targetOffset(4,9))
    wait(1.5)
    for b in range(0,3,1):
        click(playbutton)
        wait(1.5)
    wait(4)
        
    click(Pattern("1439192947095.png").exact())
    wait(1)
    count = count+1
    if count == 50:
        click(Pattern("1439193623625.png").similar(0.97))
        wait(2)
        click("1439193653802.png")
        wait(1)
        count = 0
        while True: 
            if exists("1439193848481.png"):
                break
            else:
                wait(2)
             