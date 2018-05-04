#App.open("C:/IDIS Solution Suite/Server/AdministrationService.exe")
import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)



       
while True:
    f= open("c:/a/RECTest_160503.txt",'a')

    type("1460014672303.png","RecordingService.exe start\n"+Key.ENTER)
    Time()
    f.write(s+"    REC Start!\n")
    f.close()
    wait(60)
    while True:
        
        if exists(Pattern("1460020188018.png").similar(0.92)):
            f= open("c:/a/RECTest_160503.txt",'a')
            Time()
            f.write(s+"    ImportDB...\n")
            f.close()
            wait(1)
        else:
            wait(30)
            break                        
        
    
    f= open("c:/a/RECTest_160503.txt",'a')
    Time()
    f.write(s+"    Import Complete!\n")
    f.close()


    while True:
        f= open("c:/a/RECTest_160503.txt",'a')        
        if exists(Pattern("1458899480223.png").similar(0.86)):

            Time()
            data = s + "    icon 1ea \n"
            f.write(data)
            
            if exists(Pattern("1458899550747.png").similar(0.91)):

                Time()
                data = s+ "    icon 2ea \n" 
                f.write(data)
                
                if exists(Pattern("1458899567283.png").similar(0.76)):
                    Time()
                    data = s + "    icon 3ea \n"
                    f.write(data)
                    
                    if exists("1461316111601.png"):
                        Time()
                        data = s + "    icon 4ea complete! \n"
                        f.write(data)
                        f.close()
                        break
                    else:
                        wait(1)
                        Time()
                        data = s + "    Final fail \n"
                        f.write(data)

                else:
                    wait(1)
                    Time()
                    data = s + "    4fail \n"
                    f.write(data)

            else:
                wait(1)
                Time()
                data = s + "    3fail \n"
                f.write(data)
          
        else:
            wait(1)
            Time()
            data = s + "    2fail \n"
            f.write(data)
    click(Pattern("1460624722021.png").similar(0.92))
    keyDown(Key.CTRL)
    type("c")
    keyUp(Key.CTRL)
     