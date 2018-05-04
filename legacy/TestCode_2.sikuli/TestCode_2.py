import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)

cnt = 1
empty = str("===========================================\n")
StartButton = find (Pattern("1458783675490.png").similar(0.96).targetOffset(-9,4)) #시작
#popup("start")
StopButton=find(Pattern("1458783675490.png").similar(0.96).targetOffset(-13,25))
#popup("stop")
while True:
    f = open("C:/a/c.txt",'a')
    f.write(empty)

    while True:
        if cnt==1: # 모든서비스 정지 상태
            if exists("1458783762689.png"):
                click(Pattern("1458815937294.png").similar(0.98).targetOffset(-34,-23))
                click(StartButton) #시작
                cnt = 0
                wait(30)
                break
            else:
                wait(1)
        
        else:      #모든 서비스 동작상태
            status = str("        
            if exists(Pattern("1458899636163.png").similar(0.86)):
                click(Pattern("1458815937294.png").similar(0.98).targetOffset(-34,-23))
                click(StopButton) #종료
                cnt = 1
                wait(30)
                break

            else:
                wait(1)
    
    while True:
        count = 1
#        f = open("C:/a/c.txt",'a')
        if exists(Pattern("1458899480223.png").similar(0.86)):
            today = datetime.datetime.now()
            s = str(today)

            data = s + "    icon 1ea \n"

            f.write(data)
            
            if exists(Pattern("1458899550747.png").similar(0.87)):
#                f = open("C:/a/b.txt",'a')
                today = datetime.datetime.now()
                s = str(today)
                data = s+ "    icon 2ea \n" 
                f.write(data)
#                f.close()
                if exists(Pattern("1458899567283.png").similar(0.98)):
#                    f = open("C:/a/b.txt",'a')
                    today = datetime.datetime.now()
                    s = str(today)
                    data = s + "    icon 3ea \n"
                    f.write(data)
#                    f.close()
                    if exists(Pattern("1458899606944.png").exact()):
#                        f = open("C:/a/b.txt",'a')
                        today = datetime.datetime.now()
                        s = str(today)
                        data = s + "    icon 4ea complete! \n"

                        f.write(data)
 
                        f.close()
                        count = count +1
                        break
                    else:
                        wait(1)
#                        f = open("C:/a/b.txt",'a')
                        today = datetime.datetime.now()
                        s = str(today)
                        data = s + "    Final fail \n"
                        f.write(data)
                        f.close()
                else:
                    wait(1)
#                    f = open("C:/a/b.txt",'a')
                    today = datetime.datetime.now()
                    s = str(today)
                    data = s + "    4fail \n"
                    f.write(data)
#                    f.close()
            else:
                wait(1)
#                f = open("C:/a/b.txt",'a')
                today = datetime.datetime.now()
                s = str(today)
                data = s + "    3fail \n"
                f.write(data)
#                f.close()             
        else:
            wait(1)
#            f = open("C:/a/b.txt",'a')
            today = datetime.datetime.now()
            s = str(today)
            data = s + "    2fail \n"

            f.write(data)
#            f.close()        