import pyinputplus


""" page 189
inputStr()

inputNum()

inputChoice()

inputMenu()

inputDatetime()

inputYesNo()

inputBool()

inputEmail()

inputFilepath()

inputPassword()
"""
>>> import pyinputplus as pyip

>>> response = pyip.inputNum()
c
'c' is not a number.
4
>>>
## enter a NUM
>>> response = pyip.inputInt(prompt='Enter a number: ')
Enter a number: ff
'ff' is not an integer.
Enter a number: ee
'ee' is not an integer.
Enter a number: 6.6
'6.6' is not an integer.
Enter a number: 3
>>>

#needs to be <= 4
>>> response = pyip.inputNum('Enter num:', min=4)
Enter num:f
'f' is not a number.
Enter num:2
Number must be at minimum 4.
Enter num:4
>>>

# needs to be > 4
>>> response = pyip.inputNum('Enter num: ', greaterThan=4)
Enter num: 4
Number must be greater than 4.
Enter num: f
'f' is not a number.
Enter num: 5
>>>

# you can skip the questoin
>>> response = pyip.inputNum(blank=True)
r
'r' is not a number.
u
'u' is not a number.

>>> response = pyip.inputNum(blank=True)
8
>>>

# 2 tries allowed
>>> response = pyip.inputNum(limit=2)
d
'd' is not a number.
b
'b' is not a number.
Traceback (most recent call last):


# 10 second timeout
>>> response = pyip.inputNum(timeout=10)
a
'a' is not a number.
Traceback (most recent call last):



### Choosing to allow certain characters with the numbers.
>>> response = pyip.inputNum(allowRegexes=[r'(I|X|V|L|C|D|M)+',r'zero'])
ff
'ff' is not a number.
X
>>> response = pyip.inputNum(allowRegexes=[r'(I|X|V|L|C|D|M)+',r'zero'])
XLLLXLXLX
>>> response = pyip.inputNum(allowRegexes=[r'(I|X|V|L|C|D|M)+',r'zero'])
3
>>> response = pyip.inputNum(allowRegexes=[r'(I|X|V|L|C|D|M)+',r'zero'])
zero
>>>

## blocking certain characters>>> response = pyip.inputNum(blockRegexes=[r'[48204]$'])
f
'f' is not a number.
4
This response is invalid.
1
>>>

## allowing and blocking Regexes
>>> response = pyip.inputStr(allowRegexes=[r'caterpillar','category'],blockRegexes=[r'cat'])
d
>>> response = pyip.inputStr(allowRegexes=[r'caterpillar','category'],blockRegexes=[r'cat'])
caterpillar
>>> response = pyip.inputStr(allowRegexes=[r'caterpillar','category'],blockRegexes=[r'cat'])
cat
This response is invalid.


def addUpToTen(numbers):
     numbersList = list(numbers)
     for i, digit in enumerate(numbersList):
             numbersList[i] = int(digit)
     if sum(numbersList) != 10:
             raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
     return int(numbers) #Return an int form of numbers.
>>> response = pyip.inputCustom(addUpToTen) #No Parentheses after adduptoten here
999
The digits must add up to 10, not 27.
91
>>>