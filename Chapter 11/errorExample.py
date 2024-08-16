def spam():
    bacon()

def bacon():
    raise Exception('this is the error message.')

spam()

try:
     raise Exception('This is the error message.')
except:
     errorFile = open('errorInfo.txt','w')
     errorFile.write(traceback.format_exc())
     errorFile.close()
     print('The traceback info was written to erronInfo.txt.')

     111
The traceback info was written to erronInfo.txt.
>>>

