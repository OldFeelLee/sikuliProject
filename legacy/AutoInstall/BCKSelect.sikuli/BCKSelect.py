from sikuli import BCKConst

def BCKSelect():
    items = ("BCK_Setup", "BCK_ClipCopy", "All" )
    selected = select("FuncSelect","BCK", options = items)
    if selected == items[BCKConst.BCK_Setup]:
        runScript("C:\sikuli\script\AutoInstall\BCK_Setup")
    elif selected == items[BCKConst.BCK_ClipCopy]:
        runScript("C:\sikuli\script\AutoInstall\BCK_ClipCopy")    

    else:
        popup("AllScriptRun")


        
BCKSelect()