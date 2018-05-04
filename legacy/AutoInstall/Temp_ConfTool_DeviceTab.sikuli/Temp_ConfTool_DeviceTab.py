# -*- coding: utf-8 -*-
#! python
from sikuli.Sikuli import *
import STM_LoadBalance
#import ConfTool
'''
for b in range(0,4,1):
    click("direction_%s.png" %(b))
    wait(1)
    print b

    #Pattern("direction_0.png").exact()Pattern("direction_1.png").exact()Pattern("direction_2.png").exact()Pattern("direction_3.png").exact()


def Log(filename,mode,contents,flag):
    global flagCheck
#    global fr
    flagCheck=0
    f=open(filename,mode)
    if flagCheck==int(flag):
        f.write(contents+" pass\n")
        f.close()
    else:
        f.write(contents+" fail\n")
        f.close()

    fr=open(filename).read().split("\n")


def ConfigRead(filename):
    global fp
    fp=open(filename).read().split("\n")

fp = open("c:/a/temp.txt")
content = fp.read().split("\n")


if content[2]=='DeviceAdd=0':
    popup("ok")

else:
    popup("1")

print content[2]


Config("aaa.txt",'w',"2t","0")
Config("aaa.txt",'a',"DeviceAdd","0")
#ConfigRead("aaa.txt")
print fr
print flagCheck


import datetime
import errorConst
import ConfigConst

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def Log(filename,mode,flag):
    global flagCheck
    flagCheck=0

    f=open(filename+".txt",mode)
    Time()
    if flagCheck==int(flag):
        f.write(s+"    "+status+" pass\n")
        f.close()
    else:
        f.write(s+"    "+status+" fail\n")
        f.close()
status="111"
Log("170221","a",errorConst.no_error)

'''
STM_LoadBalance.loadbalanceTest_deviceAssign()



