import sys
'''
def exit(code=0):
    if code ==5 :
        App.open("notepad")
'''

#run("java -jar sikulix.jar -r C:\sikuli\script\AutoInstall\exit_Test.skl",15) 

ret = runScript("C:\sikuli\script\AutoInstall\exit_Test")

if ret == 5 :
    runScript("C:\sikuli\script\AutoInstall\exit_Test_01"
