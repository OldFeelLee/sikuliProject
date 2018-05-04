#Client loading 및 tab 초기화


def hover_click_click(image1,image2,image3):
    hover(image1)
    click(image2)
    click(image3)

while not exists("1484296119568.png"):
    click("1484296137392.png")
    type(Key.ENTER)
    wait(1)    


oem=open("c:/a/install.txt").read(1)
if oem == "I":
    hover_click_click("1486540793488.png","1486539519285.png","1486539537552.png")

else:
    hover_click_click("1486539510228.png","1486539519285.png","1486539537552.png")
