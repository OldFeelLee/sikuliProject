#def capture():
import datetime

while True:
    keyDown(Key.ALT+Key.PRINTSCREEN)
    wait(1)
    keyUp(Key.ALT+Key.PRINTSCREEN)
    wait(1)
    keyDown(Key.WIN+"r")
    wait(1)
    keyUp(Key.WIN+"r")
    wait(1)
    type("mspaint"+Key.ENTER)
    today = datetime.datetime.now()
    s = str(today)

    while True:
        if exists("1450781301356.png"):
            wait(1)
            keyDown(Key.CTRL+"v")
            wait(1)
            keyUp(Key.CTRL+"v")
            wait(1)
            keyDown(Key.ALT+"d"+"a")
            wait(1)
            keyUp(Key.ALT+"d"+"a")
            type(s)
            wait(1)
            type(Key.ENTER)
            break
        else :
            wait(1)