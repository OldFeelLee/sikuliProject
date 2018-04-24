import datetime
import string
import errorConst


def Time():    #get current time
    global s
    today = datetime.datetime.now()
    s = str(today)