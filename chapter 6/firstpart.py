
print('''Dear Alice,
      
      Eve's cat has been arrested for catnapping, cat buglary, and extortion,
      
      Sincerly,
      Bob''')

print("Dear Alice\n\nEve's cat has been arrested for catnapping, cat burglary,and extortion\n\nSincerly,\nBob")

"""This is a test python program.
Written by Al Sweigart al@inventwithpython.com

this program was designed for python 3, not Python 2.
"""

def spam():
    """This is a multiline comment to help explain what the spam() function does."""
    print('Hello')

print('How are you?')
feeling = input()
if feeling.lower() =='great':
    print('feel great too.')
else:
    print('Ihope the rest of your day is good')

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

    