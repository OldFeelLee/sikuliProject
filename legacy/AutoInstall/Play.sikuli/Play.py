
run("java -jar sikulix.jar -r C:\sikuli\script\AutoInstall\Install.skl") # 설치
run("java -jar sikulix.jar -r C:\sikuli\script\AutoInstall\ConfTool.skl") # 장치 등록
run("java -jar sikulix.jar -r C:\sikuli\script\AutoInstall\StorageAdd.skl") #Storage 설정
run("java -jar sikulix.jar -r C:\sikuli\script\AutoInstall\REC_Schedule.skl") #REC schedule 설정
run("java -jar sikulix.jar -r C:\sikuli\script\AutoInstall\MON_Schedule.skl") #EventAck schedule 설정 
run("java -jar sikulix.jar -r C:\sikuli\script\AutoInstall\Client.skl") # Client login
run("java -jar sikulix.jar -r C:\sikuli\script\AutoInstall\Client_Live.skl") #Client_Live 확인
run("java -jar sikulix.jar -r C:\sikuli\script\AutoInstall\ClipCopy.skl") #ClipCopy
run("java -jar sikulix.jar -r C:\sikuli\script\AutoInstall\BackupSetup.skl") #Backup 설정

run("java -jar sikulix.jar -r C:\sikuli\script\AutoInstall\ProblemReporter.skl") # ProblemReporter


run("C:\sikuli\gr1mailtest.bat")

