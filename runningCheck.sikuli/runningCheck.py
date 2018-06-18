from sikuli import *
import subprocess


def running(processName):

    n=0# number of instances of the program running 
    prog=[line.split() for line in subprocess.check_output("tasklist").splitlines()]
    [prog.pop(e) for e in [0,1,2]] #useless 
    for task in prog:
        if task[0]==processName:
            n=n+1
    if n>0:
        return True
    else:
        return False       
