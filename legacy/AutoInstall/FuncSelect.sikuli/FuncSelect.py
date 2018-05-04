def Config(filename,mode,contents):
    global fr  
    f=open(filename,mode)
    f.write(contents+"\n")
    f.close()      
    fr=open(filename).read().split("\n")
    


def FuncSelect():

    items = (unicode("전체","utf-8"),unicode("부분적","utf-8"))
    selected = select(unicode("기능선택","utf-8"),"Selcet", options = items)
    if selected == items[0]:

        runScript("C:\sikuli\script\AutoInstall\Play_2")
    else :
        
        runScript("C:\sikuli\script\AutoInstall\FuncList")


runScript("C:\sikuli\script\AutoInstall\OEMSelect")

FuncSelect()

run("C:\sikuli\gr1mailtest.bat") # Test 결과 메일