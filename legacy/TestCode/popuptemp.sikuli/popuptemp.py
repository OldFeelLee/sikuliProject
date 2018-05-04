import random
import string

ran = "".join([random.choice(string.digits)])
s = int(ran)

if s ==0:
    print(ran)
    popup("0")
else:
    if s == 1:
        print(ran)
        popup("1")
    else:
        if s == 2:
            print(ran)
            popup("2")
        else:
            if s == 3:
                print(ran)
                popup("3")
            else:
                print (ran)
                popup("!!!")