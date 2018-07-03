from sikuli import *

def whileNotExists(showImage,clickImage):
    while not exists(showImage):
        click(clickImage)
        wait(2)

        
def whileNotExsits_type(showImage,clickImage,str):
    while not exists(showImage):
        type(str)
        wait(2)
        click(clickImage)
        wait(2)
        

def whileNotExists_wait(showImage):
    while not exists(showImage):
        wait(2)

def exists_click(showimg):
    if exists(showimg,30):
        click(showimg)
        wait(2)

def exists_type(showimg,str1):
    if exists(showimg,300):
        type(str1)


def exists_click_click(showimg,clickimg1,clickimg2):
    if exists(showimg):
        click(clickimg1)
        wait(2)
        click(clickimg2)
        wait(2)

def exists_click_type(showimg,clickimg1,str1):
    if exists(showimg,60):
        click(clickimg1)
        wait(2)
        type(str1)
        wait(2)
        return True        