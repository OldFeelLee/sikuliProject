#b = unicode("한글", "utf-8")
#a=input(value)
#popup(unicode("가나다","utf-8"))
"""
App.open("C:\IDIS Solution Suite\Client\G2ConfTool.exe")
App.open("notepad")
wait(1)
type("10.0.127.111")
"""
multiline = """녹화된 영상이 재생되오니, 하기 내용을 확인해주세요.
1. 녹화 스케쥴 설정대로 녹화되었는지 확인
2. 이벤트 발생 구간을 기점으로 Stream 변경 확인 및 영상 이상 유무 확인
3. 재생 중 영상깨짐 유/무 확인
"""
#popup(unicode(multiline,"utf-8"),"Play Test")

#popup(unicode("녹화된 영상이 재생되오니, 하기 내용을 확인해주세요.\n 1. 영상 깨짐 유/무\n 2. 이벤트 발생 구간을 기점으로 Stream 변경 확인 및 영상 이상 유무 확인", "utf-8"),"Play Test")

"""
CA=input(unicode("카메라 ip를 입력하세요.","utf-8"))
CP=input(unicode("카메라 pw를 입력하세요.","utf-8"))

type(Pattern("1462240099062.png").targetOffset(-17,18),CA)
type(Pattern("1462240099062.png").targetOffset(-17,18),CP)
"""

"""
value = unicode("Enter a Sayı", "utf-8")
a=input(value)
#popup(a)
type(Pattern("1462240099062.png").targetOffset(-17,18),a)
"""





items = ("idis","3rdParty")
selected = select(unicode("Please select an item from the list","utf-8"),"protocol", options = items)
if selected == items[0]:
    popup(unicode("idis를 선택함","utf-8"))
else:
    popup(unicode("3rd 선택","utf-8"))
    exit(1)






