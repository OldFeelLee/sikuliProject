oem=open("c:/sikuli/TestResult.txt").read(1)
if oem == "I":
    click(Pattern("1486534341669.png").similar(0.94).targetOffset(0,6))
else:
    click(Pattern("1486538586471.png").similar(0.90))

click("1486539678467.png")
click("1486539690669.png")
