import string
import datetime


def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)


cnt=0
while True:
    cnt= cnt+1
    strcnt = str(cnt)
    click(Pattern("1468910698450.png").exact().targetOffset(52,4))
    wait(2)
    click(Pattern("1468910735888.png").targetOffset(73,0))
    wait(2)
    type(Key.ESC)
    wait(1)
    f= open("d:/a/new_261_leak_0729.txt",'a')
    Time()
    f.write(s+"    "+strcnt+"    Success!\n")
    f.close()
    """
    if cnt==1000:
        break
    """