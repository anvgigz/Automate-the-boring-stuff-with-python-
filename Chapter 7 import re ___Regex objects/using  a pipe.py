>>> import re


>>> heroRegex = re.compile (r'Batman|tina Fey')
>>> mo1 = heroRegex.search('Batman and tina Fey')
>>> mo1.group()
'Batman'
>>>
>>> mo2 = heroRegex.search('tina Fey and Batman')
>>> mo2.group()
'tina Fey'
>>>

>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group()
'Batmobile'
>>> mo.group(1)
'mobile'
>>>


### question mark? is used to alow the compiler to do either option on a search
>>> batRegex = re.compile(r'Bat(wo)?man')
>>> mo1 = batRegex.search('The aventures of Batman')
>>> mo1.group()
'Batman'
>>> mo2.group(1)

>>> mo2 = batRegex.search('The Adventures of Batwoman')
>>> mo2.group()
'Batwoman'
>>>


### question mark? is used to alow the compiler to do either option on a search
>>> phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d')
>>> mo1 = phoneRegex.search('My number is 432-245-3232')
>>> mo1.group()
'432-245-323'
>>> mo2 = phoneRegex.search('My number is 444-3234')
>>> mo2.group()
'444-323'
>>>


## mispelled Regex as regec >>>> with the * star key the wo could be grabbed multiple times
>>> batRegec = re.compile(r'Bat(wo)*man')
>>> mo1 = batRegex.search('The Adventures of Batman')
>>> mo1.group()
'Batman'
>>>
>>> mo2 = batRegec.search('The Adventures of Batwowowowowowoman')
>>> mo2.group()
'Batwowowowowowoman'
>>>
>>> mo3 = batRegec.search('The Adventures of Batwoman')
>>> mo3.group()
'Batwoman'
>>>

###The + key means to match one or more but can not exclude the search of (wo) otherwise it will not find it.
>>> batRegex = re.compile(r'Bat(wo)+man')
>>> mo1 = batRegex.search('Adventures of Batwoman')
>>> mo1.group()
'Batwoman'
>>>
>>> mo2 = batRegex.search('The Adventures of Batwowowowowowoman')
>>> mo2.group()
'Batwowowowowowoman'
>>>
>>> mo3 = batRegex.search('Adventures of Batman')
>>> mo3.group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
>>> mo3 == None
True
>>>
