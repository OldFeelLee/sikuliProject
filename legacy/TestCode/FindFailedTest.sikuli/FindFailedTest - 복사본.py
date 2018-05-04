# --- nice and easy
if exists("1481778392073.png"): # no exception, returns None when not found
        pass # it is there
else:
        pass # we miss it
'''
# --- using exception handling
# every not found in the try block will switch to the except block
try:
        find("1481778392073.png")
        pass # it is there
except FindFailed:
        pass # we miss it
'''
# --- using setFindFailedResponse
setFindFailedResponse(PROMPT) # no exception raised, not found returns None
if find("1481778392073.png"):
#        setFindFailedResponse(ABORT) # reset to default
        pass # it is there
        a=1
        print a
else:
#        setFindFailedResponse(ABORT) # reset to default
        pass # we miss it
        a=2
        print a
        run("d:\sikuli\gr1mailtest.bat")
'''
# --- using setThrowException
setThrowException(False) # no exception raised, not found returns None
if find("1481778392073.png"):
        setThrowException(True) # reset to default
        pass # it is there
else:
        setThrowException(True) # reset to default
        pass # we miss it


'''