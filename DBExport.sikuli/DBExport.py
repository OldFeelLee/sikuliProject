import string
import errorConst
import currentTime
import fileLog
import clickFunc
import existsFunc
import ConfTool
import forFunc
import randomFunc
import runningCheck

def DBExport():

    fileLog.status = "DBExport Setting"
    clickFunc.click_click_type(Pattern("1486459824465.png").similar(0.69),Pattern("1486459847185.png").similar(0.88),Key.ENTER)
    if existsFunc.exists_click_type("1486516622854.png","1486516654143.png","ExportTest.iexp"+Key.ENTER) == True:
        existsFunc.exists_click(Pattern("1517384078551.png").targetOffset(45,32))
         
        fileLog.status = "DBExporting"
    existsFunc.exists_type(Pattern("1486516821324.png").similar(0.77),Key.ENTER)
    fileLog.Log("DBExport_07.02-07.09",'a',errorConst.no_error)
    wait(5)
try:
    fileLog.cnt = 0
    fileLog.status = None

    fileLog.Log("DBExport_07.02-07.09",'a',errorConst.no_error)

    while True : 
        if runningCheck.running("G2ConfTool") == False:
            ConfTool.Open()
        DBExport()
 
except FindFailed:
    fileLog.Log("DBExport_07.02-07.09",'a',errorConst.error_1) 


