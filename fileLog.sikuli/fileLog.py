import datetime
import string
import errorConst
import currentTime
import os

def Log(filename,mode,flag):     #result log
    global cnt
    global status
    os.chdir("C:\sikuliLog")
    cntstr =str(cnt)
    statusStr = str(status) 
    f=open(filename+".txt",mode)
    currentTime.Time()
    if cnt==0:
        f.write(currentTime.s+"    "+" start\n")
        f.close()
        cnt = cnt + 1
    else:
        if flag==errorConst.no_error: 
            f.write(currentTime.s+"    "+"    "+cntstr+"    "+statusStr+" pass\n")
            f.close()
            cnt = cnt + 1
        else:
            f.write(currentTime.s+"    "+"    "+cntstr+"    "+statusStr+" fail\n")
            f.close()


def Log_flagCheck(filename,mode,flag):     #result log
    global cnt
    global status
    global tempFlag
    os.chdir("C:\sikuliLog")
    cntstr =str(cnt)
    statusStr = str(status) 
    f=open(filename+".txt",mode)
    currentTime.Time()
    if cnt==0:
        f.write(currentTime.s+"    "+" start\n")
        f.close()
        cnt = cnt + 1
        tempFlag = errorConst.Disable
    else:
        if flag==errorConst.no_error: 
                
            if tempFlag == errorConst.Disable:
                f.write(currentTime.s+"    "+"    "+cntstr+"    "+statusStr+" pass\n")
                f.close()                
                cnt = cnt +1
                tempFlag = errorConst.Enable
            else:
                f.write(currentTime.s+"    "+"    "+cntstr+"    "+statusStr+" pass\n")
                f.close() 
                tempFlag = errorConst.Disable 
        else:
            f.write(currentTime.s+"    "+"    "+cntstr+"    "+statusStr+" fail\n")
            f.close()