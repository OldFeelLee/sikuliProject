from sikuli import *


def type_type_type(str1,str2,str3):
    type(str1)
    wait(5)
    type(str2)
    wait(5)
    type(str3)
    wait(5)

def type_type(str1,str2):
    type(str1)
    wait(5)
    type(str2)
    wait(5)

def type_type_click(str1,str2,img1):
    type(str1)
    wait(5)
    type(str2)
    wait(5)
    click(img1)
    wait(5)

def keyDownUp(holdKey,clickKey):
    keyDown(holdKey)
    wait(2)
    type(clickKey)
    wait(2)
    keyUp(holdKey)
    wait(2)