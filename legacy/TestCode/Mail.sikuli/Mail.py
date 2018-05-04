import datetime


def Time():
    global s
    global t
    global time 
    time = datetime.datetime.now()
    t = str(time)
    global today
    today = datetime.datetime.now()
    s = str(today)
    
def Hours():
    global hours 
    hours = datetime.timedelta(hours=12)



def Minute():
    global min
    min = datetime.timedelta(minutes=1)

#run("d:\sikuli\gr1mailtest.bat")
#run ("D:\Test_Util\gr1Mailer\gr1mailtest.bat")
#run("cmd")
def Time2():
    Time()
    Hours()
#Minute()
#d=today+hours
    global e
    e=today+hours
def su():
    a=1
    b=2
    c=a+b
'''
while True:
    Time()
    click("1481607714697.png")
    if e<today:
        run("d:\sikuli\gr1mailtest.bat")
        print e
        print today
        break
'''
#if d>today:
    #run("d:\sikuli\gr1mailtest.bat")
Time2()
