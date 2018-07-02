from sikuli import *
import fileLog


def click_click(img1,img2):
    fileLog.status = "click1"    
    click(img1)
    wait(2)
    fileLog.status = "click2"
    click(img2)
    wait(2)

def click_wait_click(img1,img2,waitTime):
    click(img1)
    wait(waitTime)
    click(img2)
    wait(waitTime)

def click_wait_doubleClick(img1,img2,waitTime):
    click(img1)
    wait(waitTime)
    doubleClick(img2)
    wait(waitTime)

def click_type(img1,str):
    click(img1)
    wait(3)
    type(str)
    wait(3)


def click_type_hover_(img1,str,hoverImg):
    click(img1)
    wait(3)
    type(str)
    wait(3)
    hover(hoverImg)
    wait(3)


def click_type_hover(img1,str,hoverImg):
    click(img1)
    wait(3)
    type(str)
    wait(3)
    hover(hoverImg)
    wait(3)


def click_click_click(img1,img2,img3):
    click(img1)
    wait(2)
    click(img2)
    wait(2)
    click(img3)
    wait(2)

def click_click_type(img1, img2, str1):
    click(img1)
    wait(2)
    click(img2)
    wait(2)
    type(str1)
    wait(2)