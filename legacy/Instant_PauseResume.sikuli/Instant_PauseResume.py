import random
import string
#status = find("1450921812983.png")
status = find("1450949222473.png")
type(status,"i")
cnt = 0

def ranTime():
    ran = "".join( [random.choice(string.digits)] ) 
    s = int(ran)
    wait(s)
    type(status,Key.SPACE)

while True :
    ranTime()
    ranTime()
    cnt = cnt + 1
    if (cnt==1000):
        type(status,"i")
        wait(1)
        type(status,"i")