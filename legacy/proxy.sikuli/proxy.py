empty = find(Pattern("1441705147863.png").exact())
#empty = find("1441098952737.png")
group = find(Pattern("1441098986961.png").exact())
layout = find(Pattern("1441099012920.png").exact())

flag = 0

while True:
    if flag == 0:
        dragDrop(group,empty)
        wait(3)
        flag = 1
    else:
        dragDrop(layout,empty)
        wait(3)
        flag = 0