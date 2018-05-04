from sikuli import MONConst

def MONSelect():
    items = ("MON_Schedule", "ActionAck", "All" )
    selected = select("FuncSelect","REC", options = items)
    if selected == items[MONConst.MON_Schedule]:
        runScript("C:\sikuli\script\AutoInstall\MON_Schedule")
    elif selected == items[MONConst.ActionAck]:
        runScript("C:\sikuli\script\AutoInstall\Client_EventManager")    
        
    else:
        runScript("C:\sikuli\script\AutoInstall\MON_Schedule")
        runScript("C:\sikuli\script\AutoInstall\Client_EventManager")    
        
MONSelect()
