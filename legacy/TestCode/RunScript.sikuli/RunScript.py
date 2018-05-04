#from sikuli import StreamingRestart
#from sikuli import Mail

#from guide import *
#Mail.Time2()
#StreamingRestart.Play()
'''
try:
    a=1
    b="2"
    c=App.focus("iNEX System/Debug LogViewer")
#        popup(b)
    print c
except :
    print a
'''



c=App.focus("iNEX System/Debug LogViewer")
a=str(c)
#a=c[1]
#m=a[1]
if a[1] =='-':
    popup("1111")
else:
    popup("!!!!!")

