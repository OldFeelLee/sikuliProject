from sikuli import STMConst

def STMSelect():
    items = ("Live", "PTZ", "Loadbalance","All" )
    selected = select("FuncSelect","STM", options = items)
    if selected == items[STMConst.Live]:
        runScript("C:\sikuli\script\AutoInstall\Client_Live")
    elif selected == items[STMConst.PTZ]:
        runScript("C:\sikuli\script\AutoInstall\STM_PTZ")    
    elif selected == items[STMConst.Loadbalance]:
        runScript("C:\sikuli\script\AutoInstall\STM_LoadBalance")    
        
    else:
        popup("AllScriptRun")


        
STMSelect()