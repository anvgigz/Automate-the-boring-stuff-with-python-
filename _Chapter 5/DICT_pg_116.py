import pprint


picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups') ## this is doe to prevent errors in code 'cups', 0)

print('I a bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs')      #amazing

spam = {'name': 'Pooka', 'age': 5}

if 'color' not in spam:
    spam['color'] = 'black'
print(spam)

spam = {'name': 'Pooka', 'age': 5} # changed back

spam.setdefault('color', 'black')

print(spam)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

print(pprint.pformat(count))