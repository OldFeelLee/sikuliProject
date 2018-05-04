#from sikuli import *
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



Time()
#print s








'''
global s
if exists("1481621400458.png"):
    s=1
else:
    s=100


'''  