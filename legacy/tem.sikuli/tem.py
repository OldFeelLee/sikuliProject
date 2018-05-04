import random
import string
import datetime

def RanTime():    #random 시간
    ran = "".join([random.choice(string.digits)])
    global s
    s=int(ran)
    wait(s)
    global t
    t = s*10
    if t==0:
        t=10
    else:
        if t>30:
            t=30


#RanTime()
#print (s)
#print (t)


try:
    click("1458613819775.png")
except FindFailed:
    today = datetime.datetime.now()
    s = str(today)
    popup(s)