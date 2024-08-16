>>> import re
>>>
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
>>> mo = phoneNumRegex.search('My number is 435-234-5678.')
>>> print('Phone number found: ' + mo.grou())
>>> print('Phone number found: ' + mo.group())
Phone number found: 435-234-567
>>>



#Parentheses added to phone number to break it up
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d)')
>>> mo = phoneNumRegex.search('My number is 435-234-5678.')
>>> mo.group(1)
'435'
>>> mo.group(2)
'234'
>>> mo.group(3)
'567'
>>> mo.group(0)
'435-234-567'
>>>