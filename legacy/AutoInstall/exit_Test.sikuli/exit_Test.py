import sys
import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)
    
'''
def exit(code=0):
    if code ==15 :
        App.open("notepad")
    elif code == 1:
        App.open("calc")
'''


try:
    click("1484104430682.png")

except:
    sys.exit(5)
    Time()
    f=open("c:/a/Exit.txt",'w')
    f.write(s+"    except!\n")
    f.close()


