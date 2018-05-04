cnt = 0
import random
import string

def RanTime():
    ran = "".join([random.choice(string.digits)])
    s=int(ran)
    wait(s)


while True:
    type("1452577834782.png","ServiceManager.exe start"+Key.ENTER)
    RanTime()
    while True:
        if cnt <100:
            if exists("1452577937295.png"):
                type("1452577834782.png","ServiceManager.exe stop"+Key.ENTER)
                cnt = 0
                break
            else:
                wait(1)
                cnt = cnt+1
        else:
            break
    if cnt == 100:
        break