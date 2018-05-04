import datetime
import random
import string


def RanTime():    #random 시간
    ran = "".join([random.choice(string.digits)])
    s=int(ran)
    wait(s)

def Time():    #get current time
    global s
    today = datetime.datetime.now()
    s = str(today)

def Log(filename,mode,flag):     #result log
    global flagCheck
    flagCheck=0
    f=open(filename+".txt",mode)
    Time()
    if cnt == 0:
        f.write(s+"    "+" start\n")   
    else:
        if flagCheck==int(flag):
            f.write(s+"    "+cnt+" pass\n")
            f.close()
        else:
            f.write(s+"    "+cnt+" fail\n")
            f.close()


def actionRepeat():
    global cnt
    cnt = 0
    Log("TestResult",'w',errorConst.no_error)       
    while True:
        
        doubleClick(Pattern("1512379400075.png").similar(0.93))
        wait(1)
        type(Key.ESC)
        wait(1)
        Log("TestResult",'a',errorConst.no_error)        
        cnt = cnt +1
        


try : 

    actionRepeat()


except FindFailed:
    Log("TestResult",'a',errorConst.error_1)     