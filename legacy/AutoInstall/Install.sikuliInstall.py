import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

def InputPath():
    global idis
    global setuppath
    setuppath=input(unicode("설치파일 경로 입력하세요.","utf-8"))
    
    items = ("idis","type1")
    selected = select(unicode("OEM 선택","utf-8"),"OEM", options = items)
    if selected == items[0]:
        idis = 1
    else :
        idis = 2
Time()
f=open("c:/a/install.txt",'w')
f.write(s+"    Start!\n")
f.close()         
while True:
    InputPath()
    if not App.open(setuppath):
        popup(unicode("설치경로를 확인해주세요 ","utf-8"), unicode("Error","utf-8"))
    
    else:
        break
try:    
    while not exists("1483670596154.png"):
        type(Key.ENTER)
        wait(1)
    while not exists(Pattern("1483671043427.png").exact()):
        click(Pattern("1483670752328.png").similar(0.96))
    
    idis = 1
    
    while not exists(Pattern("1483671346800.png").similar(0.91)):
        type("n")
        if exists("1483672154543.png"):
            if idis == 1:
                App.focus("IDIS Solution Suite")
            else:
                App.focus("iNEX")
    
    while not exists("1483671483949.png"):
        wait(1)
    click("1483671506517.png")
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    Install Complete!\n")
    f.close()     
#    run("C:\sikuli\gr1mailtest.bat")    
except FindFailed:
    Time()
    f=open("c:/a/install.txt",'a')
    f.write(s+"    Install Fail!\n")
    f.close()  
#    run("C:\sikuli\gr1mailtest.bat")