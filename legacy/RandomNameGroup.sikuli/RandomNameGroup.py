import random 
import string
global name

  
def GroupName():
    name = "".join( [random.choice(string.digits)] ) 
    type("1450694591373.png",name)
    wait(1)
    click(Pattern("1450694614100.png").targetOffset(-43,4))
    wait(1)

while True:
 

    click(Pattern("1450694251839.png").exact().targetOffset(-149,-16))
    while True:
        if exists("1450694534763.png"):
            GroupName() 
            break
        else:
            wait(1)

    while True :
        if exists("1450694732931.png"):
            click(Pattern("1450694732931.png").targetOffset(143,60))

            wait(1)
            GroupName()
        else :
            break


