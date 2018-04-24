from sikuli import *
import datetime
import string
import errorConst
import currentTime
import fileLog
import existsFunc

def ConfToolOpen():
    fileLog.status = "ConfToolOpen"
    App.open("C:\IDIS Solution Suite\Client\G2ProblemReporter.exe")
    wait(5)
    existsFunc.whileNotExsits_type("1524447598736.png","1524447609584.png",Key.ENTER)
    wait(2)
    existsFunc.whileNotExists("1524447630007.png","1524447634504.png")
    fileLog.status = None