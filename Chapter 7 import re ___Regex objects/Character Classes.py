""" PG 173 Character classes
\d == Any numeric character from 0-9
\D == Any character that is not a digit from 0-9
\w == any letter, Numeric digit, or underscore character (((matching word characters))) 
\W == any character that is not a letter Numberic digit or underscored character
\s Any space, tab, or newline character. [Think of this as matching "space" characters]
\S any character that is not a space tab or new line
"""

#example of \d+\s\w+
>>> xmasRegex = re.compile(r'\d+\s\w+')
>>> xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens,
2 doves, 1 partridge')
['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']
>>>
#example of needing to be more specific like finding the vowels in a snetence.
>>> vowelRegex = re.compile(r'[aeiouAIEOU]')
>>> vowelRegex.findall('RoboCop eats baby food. Baby Food.')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'a', 'o', 'o']
>>>

### the Carrot ^ character with the use of Barckets [] will find all other characters that dont match the ones specified
>>> vowelRegex = re.compile(r'[^aeiouAIEOU]')
>>> >>> vowelRegex.findall('RoboCop eats baby food. Baby Food.')
>>> vowelRegex.findall('RoboCop eats baby food. Baby Food.')
['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'b', 'y', ' ', 'F', 'd', '.']
>>>

### using the Carrot ^ character without the Brackets will only allow the search to be found if the begining of the string starts with the regex patter H
>>> beginsWithHello = re.compile(r'^Hello')
>>> beginsWithHello.search('Hello, world!')
<re.Match object; span=(0, 5), match='Hello'>
>>> beginsWithHello.search('He said Hello.') == None
True
>>>

## using the dollar sign $ at the end ensures string has to end with the regex patter 2
>>> endsWithNumber = re.compile(r'\d$')
>>> endsWithNumber.search('Your Number is 42')
<re.Match object; span=(16, 17), match='2'>
>>> endsWithNumber.search('Your number is forty tow') == None
True
>>>

### Using the Carrot ^ at the Begining and the $ at the end to ensure the search matches the regex perfectly. in the below example only digits are allowed by using the \d
>>> wholeStringIsNum = re.compile(r'^\d+$')
>>> wholeStringisNum.search('123456789')
Traceback (most recent call last):
>>> wholeStringIsNum.search('12345xyz6789') == None
True
>>> wholeStringIsNum.search('12 3456789') == None
True
>>>