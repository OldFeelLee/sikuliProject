import random
import datetime

def ranNumber(t1,t2):
    global ranTime
    ranTime = random.randrange(t1,t2)


def RanTime():    
    ran = "".join([random.choice(string.digits)])
    s=int(ran)
    wait(s)