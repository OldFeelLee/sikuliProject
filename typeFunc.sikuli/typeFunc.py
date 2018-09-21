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

def type_hover(str1,img1):
    type(str1)
    wait(3)
    hover(img1)
    wait(3)


def type_wait(str1, waitTime):
    type(str1)
    wait(waitTime)


def type_existsClick(str1, waitTime, img1):
    type(str1)
    wait(waitTime)
    if exists(img1):
        return True
    else:
        return False
        
def type_exists(str1, img1):
    type(str1)
    wait(2)
    if exists(img1):
        type(Key.LEFT)
        wait(2)
        type(Key.ENTER)
        wait(2)


        
def type_type_exists(str1, str2, img1):
    type(str1)
    wait(2)
    type(str2)
    wait(2)
    if exists(img1):
        type(Key.LEFT)
        wait(2)
        type(Key.ENTER)
        wait(2) 
        return True
    else:
        return False