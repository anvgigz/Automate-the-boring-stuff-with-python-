def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

def chicken_nuggets():
    global bombalomb            #global variable --transferable to different local scopes (((def)))
    bombalomb = 'superbomb'
    nuggets()
    print(bombalomb)

def nuggets():

    print(bombalomb)
    
chicken_nuggets()

def spam(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print('invalid arguement')
    

def numbers():
    print(spam(9))
    print(spam(39))
    print(spam(98))
    print(spam(0))

print(numbers())


