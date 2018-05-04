import datetime
from StringIO import StringIO
from sikuli import *


def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

items = ("idis","type1")
selected = select(unicode("OEM º±≈√","utf-8"),"OEM", options = items)
if selected == items[0]:
    idis = 1
    idisstr = "IDIS"
else :
    idis = 2
    idisstr = "TYPE1"

Time()
f=open("c:/a/install.txt",'w')
f.write(idisstr+"\n")
f.write(s+"    Start!\n")
f.close()
#ff = StringIO("c:/a/install.txt")
content = open("c:/a/install.txt").read(1)  
f.close()
if content =="I":
    print content
else:
    print s

