catnames = []
while True:
    print ('enter a name of a cat ' + str(len(catnames) + 1) + 
           '(or enter nothing to stop.):')
    name = input()
    if name == '':
        break

    catnames = catnames + [name] ##list concatenation
    print('The cat names are:')
for name in range(len(catnames)):
        print('your ' + str(name) + ' catname is ' + catnames[name])

for index, name in enumerate(catnames):
     print('your ' + str(index) + ' catname is ' + (name))\
     

catnames.append('jack')
print(catnames)
catnames.append('buddy')
catnames.remove('jack')
print(catnames)

catnames.sort()
print(catnames)
catnames.sort(reverse=True)
#orr 
catnames.reverse()      #same thing as reverse=True

name = 'zophia the cat'
for i in name:
    print('*** ' + i + ' ***')

new_name = name[0:7] + 'the' + name[10:]
print(new_name)

id(new_name)

#you can use dognames = copy.copy(catnames) to copy the list to a nef reference

#If the list has a list you will need to use copy.deepcopy(catnames)