from sikuli import *
import datetime
import string
import errorConst
import currentTime
import fileLog
import existsFunc

def Open():
    fileLog.status = "ConfToolOpen"
    App.open("C:\IDIS Solution Suite\Client\G2ConfTool.exe")
    wait(5)
    type(Key.ENTER)
    existsFunc.whileNotExsits_type("1524448236851.png","1524447598736.png",Key.ENTER)
    wait(2)
    existsFunc.whileNotExists("1524447634504.png","1524448259676.png")
    fileLog.status = None