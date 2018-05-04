import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)




Time()
f=open("c:/a/install.txt",'a')
f.write(s+"    test!\n")
f.close()  
run("C:\sikuli\gr1mailtest.bat")