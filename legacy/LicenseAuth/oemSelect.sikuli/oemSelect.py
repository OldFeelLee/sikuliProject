
def OEMWrite(filename,oem):
    f=open(filename+".txt",'w')
    f.write(oem+"\n")
    f.close()
   

def OEMSelect():
    items = ("idis","type1")
    selected = select(unicode("OEM 선택","utf-8"),"OEM", options = items)
    if selected == items[0]:
        OEMWrite("TestResult","IDIS")

    else :
        OEMWrite("TestResult","TYPE1")


OEMSelect()