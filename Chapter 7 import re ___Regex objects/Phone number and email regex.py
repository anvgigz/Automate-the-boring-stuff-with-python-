#!pYTHON 3 
#phone and email.py - finds phone numbers and email addresses on the cluoboard

import re, pyperclip

phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?                  #Area code
                        (\s|-|\.)?                          #seperator
                        (\d{3})                             #First 3 digits
                        (\s|-|\.)                           #seperator
                        (\d{4})                             # Last 4 Digits
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?      # Extension
                        )''', re.VERBOSE)

emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+       #Username
                        @                       # @ Symbol
                        [a-zA-Z0-9.-]+          # Domain Name
                        (\.[a-zA-Z]{2,4})       # dot-something
                        )''', re.VERBOSE)

# Read text from the clipboard
text = pyperclip.paste()

# Find all matches in the clipboard text
matches = phoneRegex.findall(text)

phoneNumbers = [match[0] for match in matches]

emailMatches = emailRegex.findall(text)
emailAddresses = [match[0] for match in emailMatches]

results = phoneNumbers + emailAddresses

# Copy results to the clipboard
if results:
    pyperclip.copy('\n'.join(results))
    print('Phone numbers and email addresses copied to clipboard:')
    print('\n'.join(results))
else:
    print('No phone numbers or email addresses found.')

#TODO: Create email regex.

# TODO find matches in clipboard text.

# copy results to the clipboard




# Read text from the clipboard
#clipboard_text = pyperclip.paste()
#print('Text from clipboard:', clipboard_text)