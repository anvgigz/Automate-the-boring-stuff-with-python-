"""Wild Card Character DOT (.*)"""

# you want to search for 'first name' then include anything after it ending with the 'last name'
"""The Dot character means any single character except new line
The Start Character * means "zero or more of the preceding character"
"""

>>> nameRegex = re.compile(r'First Name:(.*) Last Name: (.*)')
>>> mo = nameRegex.search('First Name: Al Last Name: Sweigart')
>>> mo.group(1)
' Al'
>>> mo.group(2)
'Sweigart'
>>>

##adding question mark at the end makes the search non greedy and only grab the first occurance of the word grouping
>>> nongreedyRegex = re.compile(r'<.*?>')
>>> mo = nongreedyRegex.search('<To serve mane> for dinner.>')
>>> mo.group()
'<To serve mane>'

# without it the last arror key is grabbed, thus grabbing the whole string.
>>> greedyRegex = re.compile(r'<.*>')
>>> mo = greedyRegex.search('<To serve man> for diner.>')
>>> mo.group()
'<To serve man> for diner.>'

>>> noNewlineRegex = re.compile(r'.*')
>>> noNewlineRegex.search('Search the public trust.\nProtect the innocent.\nUphold the law.').group()
'Search the public trust.'
>>>

>>> newlineRegex = re.compile('.*',re.DOTATAL)
>>> newlineRegex.search('Search the public trust.\nProtect the innocent.\nUphold the law.').group()
'Search the public trust.\nProtect the innocent.\nUphold the law.'
>>>

#passign the second arguement re.I (orre.IGNORECASE) will grab robocop no matter the cassing
>>> robocop = re.compile(r'robocop',re.I)
>>> robocop.search('RoboCop si part maen, part nachine, all cop.').group()
'RoboCop'

#substituting words.
>>> namesRegex = re.compile(r'Agent \w+')
>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret dociments to Agent Bob.')
'CENSORED gave the secret dociments to CENSORED.'
>>>

>>> agentNamesRegex = re.compile(r'Agent (\w)\w*')
>>> agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double Agent.')
'A**** told C**** that E**** knew B**** was a double Agent.'
>>>