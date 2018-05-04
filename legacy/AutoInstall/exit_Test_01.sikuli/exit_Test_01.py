# -*- coding: utf-8 -*-

from sikuli import Install

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def failed():
    Time()
    f=open("c:/a/Exit.txt",'w')
    f.write(s+"    fail!\n")
    f.close()


print Install.idis
