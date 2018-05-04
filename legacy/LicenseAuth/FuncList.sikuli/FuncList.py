
def FuncSelect():

    items = ("Online","Offline")
    selected = select(unicode("인증방식선택","utf-8"),"Selcet", options = items)
    if selected == items[0]:
        runScript("C:\sikuli\script\LicenseAuth\Serial")
        runScript("C:\sikuli\script\LicenseAuth\LicenseAuth")
        
    else :
        runScript("C:\sikuli\script\LicenseAuth\Serial")                
        runScript("C:\sikuli\script\LicenseAuth\LicenseAuth_Off")


FuncSelect()