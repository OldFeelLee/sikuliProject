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

def exists_click_click(showimg,clickimg1,clickimg2):
    if exists(showimg):
        click(clickimg1)
        wait(2)
        click(clickimg2)
        wait(2)
        