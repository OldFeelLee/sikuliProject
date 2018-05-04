from sikuli import ConfToolConst


def ConfToolSelect():
    items = ("SystemSetup", "DBImport_Export","DeviceAdd","UserAuthority","ManyDeviceAdd_Delete", "All" )
    selected = select("FuncSelect","ConfTool", options = items)
    if selected == items[ConfToolConst.SystemSetup]:
        popup("t")
#        runScript("C:\sikuli\script\AutoInstall\")
    elif selected == items[ConfToolConst.DBImport_Export]:
        runScript("C:\sikuli\script\AutoInstall\DBExport")
        runScript("C:\sikuli\script\AutoInstall\DBImport")
    elif selected == items[ConfToolConst.DeviceAdd]:
#        runScript("C:\sikuli\script\AutoInstall\")    
        popup("t")    
    elif selected == items[ConfToolConst.UserAuthority]:
#        runScript("C:\sikuli\script\AutoInstall\")     
        popup("t")    
    elif selected == items[ConfToolConst.ManyDeviceAdd_Delete]:
        runScript("C:\sikuli\script\AutoInstall\ConfTool_ManyDeviceAdd_Delete")     
                     
    else:
        popup("AllScriptRun")


ConfToolSelect()