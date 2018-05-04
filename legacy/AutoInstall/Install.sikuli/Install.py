# -*- coding: utf-8 -*-
import datetime
from sikuli import errorConst

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def InputPath():
#    global idis
    global setuppath
    setuppath=input(unicode("설치파일 경로 입력하세요.","utf-8"))  


def success():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    Install Complete!\n")
    f.close()
    
def failed():
    f=open("c:/a/install.txt",'a')
    f.write(s+"    Install Fail!\n")
    f.write(s+"    All Test Skip\n")
    f.close()



Time()

oem=open("c:/a/install.txt").read(1)
f=open("c:/a/install.txt",'a')
f.write(s+"    Start!\n")
f.close()


while True:
    InputPath()
    if not App.open(setuppath):
        popup(unicode("설치경로를 확인해주세요 ","utf-8"), unicode("Error","utf-8"))
    
    else:

        break
#exit(errorConst.error_1)    
try:    
    cnt=0

    while not exists("1483670596154.png"):
        type(Key.ENTER)
        wait(1)
    while not exists(Pattern("1483671043427.png").exact(),1):
        click(Pattern("1483670752328.png").similar(0.96))
        
    while not exists(Pattern("1483671346800.png").similar(0.91)):
        type("n")
        if exists("1483672154543.png"):
            if oem =="I":
                App.focus("IDIS Solution Suite")
            else:
                App.focus("iNEX")
    
    if exists("1483671483949.png",600):
        click("1483671506517.png")
        
    Time()
    success()
    exit(errorConst.no_error)
#    run("C:\sikuli\gr1mailtest.bat")    
except FindFailed:
    Time()
    failed()
    exit(errorConst.error_1)
#    run("C:\sikuli\gr1mailtest.bat")