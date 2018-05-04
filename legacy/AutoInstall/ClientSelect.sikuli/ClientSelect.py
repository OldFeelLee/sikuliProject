import ClientConst


def ClientSelect():
    items = ("RECIcon", "All" )
    selected = select("FuncSelect","Client", options = items)
    if selected == items[ClientConst.Client_RECIcon]:
        runScript("C:\sikuli\script\AutoInstall\Client_RECIcon")

    else:
        popup("AllScriptRun")


ClientSelect()