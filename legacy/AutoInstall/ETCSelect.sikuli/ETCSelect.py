import ETCConst


def ETCSelect():
    items = ("LicenseAuth", "ProblemReporter" )
    selected = select("FuncSelect","ETC", options = items)
    if selected == items[ETCConst.LicenseAuth]:
        runScript("C:\sikuli\script\AutoInstall\LicenseAuth")
    elif selected == items[ETCConst.ProblemReporter]:
        runScript("C:\sikuli\script\AutoInstall\ProblemReporter")
    else:
        popup("AllScriptRun")


ETCSelect()