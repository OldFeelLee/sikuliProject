import datetime
import sys
from sikuli import errorConst

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def success():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    ClientLogIn complete!\n")
    f.close()  

def failed():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    "+status+" fail!\n")
    f.write(s+"    Live + ClipCopy Test Skip\n")
    f.close()  
    

try:
    global status
    status = "Client LogIn"
    oem=open("c:/a/install.txt").read(1)
    if oem == "I":
        App.open("C:\IDIS Solution Suite\Client\G2Client.exe")
    else:
        App.open("C:\iNEX\Client\G2Client.exe")
    if exists("1484038689399.png",600):        
#        App.focus("IDIS Solution Suite Client")
        type(Pattern("1484026887173.png").similar(0.92),"12345678"+ Key.ENTER)
    if exists("1484027016886.png",FOREVER):        
        click(Pattern("1484027016886.png").targetOffset(150,55))
    Time()
    success()
    exit(errorConst.no_error)

except FindFailed:
    Time()
    failed()  
    exit(errorConst.error_1)