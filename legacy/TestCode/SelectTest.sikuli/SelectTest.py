from sikuli import errorConst


def OEMSelect():
    global idisstr    
    items = (unicode("전체","utf-8"),unicode("기능","utf-8"))
    selected = select(unicode("기능선택","utf-8"),"Selcet", options = items) # 
    if selected == items[0]:
#        idis = 1
        exit(errorConst.Full)
    else :
#        idis = 2
        exit(errorConst.Part)
OEMSelect()