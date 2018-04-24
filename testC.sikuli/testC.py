import datetime
import string
import errorConst
import currentTime
import fileLog
import clickFunc
import existsFunc    
import os
import glob


os.chdir("E:\clip")
files = glob.glob("*.exe")
for a in files:   
    os.remove(a)
