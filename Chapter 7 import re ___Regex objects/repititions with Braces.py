import re

>>> haRegex = re.compile(r'(Ha){3}')
>>> mo1 = haRegex.search('HaHaHa')
>>> mo1.group()
'HaHaHa'
>>>
>>> mo2 = haRegex.search('Ha')
>>> mo2 ==None
True
>>>


### By default the longest string will be chossen
>>> greedyHaRegex = re.compile(r'(Ha){3,5}')
>>> mo1 = greedyHaRegex.search('HaHaHaHaHa
>>> mo1 = greedyHaRegex.search('HaHaHaHaHa')
>>> mo1.group()
'HaHaHaHaHa'
>>>

### including the question Mark ? will make the first shortes string be found rather than the longest.
>>> nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
>>> mo2 = nongreeduHaRegex.search('HaHaHaHaHa')
>>> mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
>>> mo2.group()
'HaHaHa'
>>>


## findall() will find the first match as well as all others.
"""first example without the findall() only the first number is found"""
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('Cell: 343-567-4322 Work: 444-222-444')
>>> mo.group()
'343-567-4322'
>>>
### findall() finds all the numbers listed
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') ##has no groups
>>> phoneNumRegex.findall('Cell: 444-555-3333 Work: 555-666-6666')
['444-555-3333', '555-666-6666']

>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  ###Has groups
>>> phoneNumRegex.findall('Cell: 222-333-5564 Work: 999-333-2245')
[('222', '333', '5564'), ('999', '333', '2245')]
>>>
