import datetime
import string



def Time():    #get current time
    global s

    today = datetime.datetime.now()
    s = str(today)

def DateWrite(filename):
    Time()
    f=open(filename+".txt",'w')
    f.write(s+"\n")
    f.close()


def Log(filename,mode,flag):     #result log
    global flagCheck
    global cnt

    flagCheck=0
    f=open(filename+".txt",mode)
    Time()
    cntstr = str(cnt)
    if cnt == 0 :
        f.write(s+"    "+" start\n")
        f.close()

    else:
        if flagCheck==int(flag):
            f.write(s+"    "+cntstr+" pass\n")
            f.close()

        else:
            f.write(s+"    "+cntstr+" fail\n")
            f.close()


def actionRepeat():

    global cnt 
    cnt = 0
    Log("ActionTest",'w',errorConst.no_error)       
    while True:
        cnt = cnt +1
        doubleClick(Pattern("1512379400075.png").similar(0.93))
        wait("1512466430148.png",20)
        type(Key.ESC)
        wait(1)
        Log("ActionTest",'a',errorConst.no_error)        




'''
try : 
    Time()

    #date_temp = list(s)
    
    date_temp=list(s)[8:10]
    tempInt = [int(x) for x in date_temp]
    print(tempInt)
    if tempInt[0] <=1 and tempInt[1] <=7:
        popup("ok")
    else:
        popup("xx")
    
    App.open("C:\IDIS Solution Suite\Client\G2ConfTool.exe")
       
except FindFailed:
    exit(None)

'''