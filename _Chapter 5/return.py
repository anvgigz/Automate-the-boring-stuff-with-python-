import random

def getanswer(answernumber):
    if answernumber == 1:
        return "It is certain"
    elif answernumber == 2:
        return 'It is decidedly so'
    elif answernumber == 3:
        return "muh muh maybe"
    elif answernumber == 4:
        return 'tOttaly dudes'
    elif answernumber == 5:
        return 'ya ok'
    elif answernumber == 6:
        return 'that might5 work'
    elif answernumber == 7:
        return 'this will never work'
    elif answernumber == 8:
        return 'thats a great idea'
    elif answernumber ==  9:
        return 'fantastic spot on to what i was thinking'
    
r = random.randint(1,9)
certainty = getanswer(r)
print(certainty)