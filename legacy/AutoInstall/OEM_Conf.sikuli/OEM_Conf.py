#oem 별 client focusing 및 ConfTool 실행

def focus_app(appName):
    global g2conftool
    g2conftool = App(appName)
    g2conftool.focus()

def openApp_logIn(path,image):
    check=str(g2conftool)
    if check[1]=='-':
        App.open(path)
        while not exists(image):
            wait(1)
        type(image,"12345678"+Key.ENTER)   



oem=open("c:/sikuli/TestResult.txt").read(1)
if oem == "I":
    focus_app("G2ConfTool.exe")
    openApp_logIn("C:\IDIS Solution Suite\Client\G2ConfTool.exe",Pattern("1486530419073.png").similar(0.92))

else:
    focus_app("G2ConfTool.exe")
    openApp_logIn("C:\iNEX\Client\G2ConfTool.exe",Pattern("1486530419073.png").similar(0.92))
