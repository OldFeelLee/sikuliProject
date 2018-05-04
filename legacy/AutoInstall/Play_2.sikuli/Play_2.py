# -*- coding: utf-8 -*-
#! python
from sikuli import errorConst



Ecode = runScript("C:\sikuli\script\AutoInstall\Install") # 설치
#runScript("C:\sikuli\script\AutoInstall\exit_Test_01")
if Ecode == errorConst.no_error:
    runScript("C:\sikuli\script\AutoInstall\LicenseAuth")
    Ecode_00 = runScript("C:\sikuli\script\AutoInstall\ConfTool") # 장치 등록    
    if Ecode_00 == errorConst.no_error:    
        runScript("C:\sikuli\script\AutoInstall\StorageAdd") #Storage 설정
        runScript("C:\sikuli\script\AutoInstall\TextInSetup") #TextIn 설정
        runScript("C:\sikuli\script\AutoInstall\REC_Schedule") #REC schedule 설정
        runScript("C:\sikuli\script\AutoInstall\MON_Schedule") #EventAck schedule 설정 
        runScript("C:\sikuli\script\AutoInstall\BackupSetup") #Backup 설정    
        runScript("C:\sikuli\script\AutoInstall\PosSimRun") #PosSim 실행 및 설정        
    Ecode_01 = runScript("C:\sikuli\script\AutoInstall\Client") # Client login
    if Ecode_01 == errorConst.no_error :
        if Ecode_00 == errorConst.no_error:
            runScript("C:\sikuli\script\AutoInstall\Client_Live") #Client_Live 확인
            runScript("C:\sikuli\script\AutoInstall\Client_EventManager") #Client_EventActionAck 확인
            runScript("C:\sikuli\script\AutoInstall\STM_PTZ") #Client_PTZ 확인

            runScript("C:\sikuli\script\AutoInstall\REC_ClipCopy") #REC_ClipCopy
            runScript("C:\sikuli\script\AutoInstall\BackupSearch") # BackupClipCopy    
    runScript("C:\sikuli\script\AutoInstall\ProblemReporter") # ProblemReporter
 
    Ecode_02 = runScript("C:\sikuli\script\AutoInstall\DBExport") # DB Export
    if Ecode_02 == errorConst.no_error:
        runScript("C:\sikuli\script\AutoInstall\DBImport") # DB Import
    
#run("C:\sikuli\gr1mailtest.bat") # Test 결과 메일
#run("C:\sikuli\ExportDel.bat") # DB Expot file 삭제
