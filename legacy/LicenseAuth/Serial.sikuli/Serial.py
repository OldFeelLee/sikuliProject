# -*- coding: utf-8 -*-

def SerialWrite(filename,oem):
    f=open(filename+".txt",'w')
    f.write(oem+"\n")
    f.close()


setSerial=input(unicode("Serial Key를 입력하세요.","utf-8")) 

SerialWrite("serial",setSerial)


