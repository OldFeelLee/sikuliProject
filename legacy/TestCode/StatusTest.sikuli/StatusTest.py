import datetime

def Time():
    global s
    today = datetime.datetime.now()
    s = str(today)



def failed():
    Time()
    f=open("d:/a/install.txt",'a')
    f.write(s+"    "+status+"    fail!\n")
    f.close() 


def temp():
    global status
    status = "test"
    print status    
    failed()
    status = "test1"
    print status    
    failed()
    status = "test2"
    print status 
    failed()


def temp2():
    global status 
#    status = "test3"
    status = "설치파일 경로 입력하세요."
    print status    
    failed()



temp()
temp2()
   