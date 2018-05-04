import datetime
import string



def Time():    #get current time
    global s

    today = datetime.datetime.now()
    s = str(today)
    wait(2)

def click_click(image1,image2):
    click(image2)
#    click_image1 = click(image1)
    print('===')
#    click_image1    
    wait(2)
#    click_image2= click(image2)
#    click_image2
    click(image1)
    
def keyHold(key1):
    keyDown(key1)
    wait(5)
    keyUp(key1)
    wait(2)

#click_click("1519016822353.png","1519016826767.png")
