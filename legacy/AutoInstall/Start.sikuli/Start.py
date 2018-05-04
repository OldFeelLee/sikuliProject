from sikuli import errorConst

Ecode = runScript("C:\sikuli\script\AutoInstall\FuncSelect") 
if Ecode==5:
    runScript("C:\sikuli\script\AutoInstall\Play_2") 

else:
    runScript("C:\sikuli\script\AutoInstall\FuncInput")