from sikuli import RECConst

def RECSelect():
    items = ("StorageAdd", "REC_Schedule", "Play", "EventREC_Search", "ClipCopy", "All" )
    selected = select("FuncSelect","REC", options = items)
    if selected == items[RECConst.StorageAdd]:
        runScript("C:\sikuli\script\AutoInstall\StorageAdd")
    elif selected == items[RECConst.REC_Schedule]:
        runScript("C:\sikuli\script\AutoInstall\REC_Schedule")    
    elif selected == items[RECConst.Play]:
#        runScript()    
        popup("nothing")    
    elif selected == items[RECConst.EventREC_Search]:
#        runScript()
        popup("nothing")    
    elif selected == items[RECConst.ClipCopy]:
        runScript("C:\sikuli\script\AutoInstall\REC_ClipCopy")
        
    else:
        popup("AllScriptRun")


        
RECSelect()