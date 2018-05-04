from sikuli import ServiceConst

def FuncList():
    items = ("REC", "STM", "MON", "BCK", "VW","Client","ConfTool", "ETC" )
    selected = select("ServiceSelect","Selcet", options = items)
    if selected == items[ServiceConst.REC]:
        runScript("C:\sikuli\script\AutoInstall\RECSelect")
    elif selected == items[ServiceConst.STM]:
        runScript("C:\sikuli\script\AutoInstall\STMSelect")
    elif selected == items[ServiceConst.MON]:
        runScript("C:\sikuli\script\AutoInstall\MONSelect")    
   
    elif selected == items[ServiceConst.BCK]:
#        runScript()
        popup("nothing")    
    elif selected == items[ServiceConst.VW]:
#        runScript()
        popup("nothing")
    elif selected == items[ServiceConst.Client]:
        runScript("C:\sikuli\script\AutoInstall\ClientSelect")
    elif selected == items[ServiceConst.ConfTool]:
#        runScript()
        runScript("C:\sikuli\script\AutoInstall\ConfToolSelect")
    elif selected == items[ServiceConst.ETC]:
        runScript("C:\sikuli\script\AutoInstall\ETCSelect")
FuncList()