import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')

logging.debug('Start the program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1,n + 1):
        total *= i
        logging.debug('i, is ' + str(i) + ', total is ' + str(total))
        logging.debug('End of fatorial(%s%%)' % (n))
        return total
    
print(factorial(5))
logging.debug('End of program')

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Some debuggging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged')
logging.error('An erro has occurred.')
logging.critical('The program is unable to recover.')

## To disable logging use
logging.disable(logging.CRITICAL)
#this will only disable Critical logging ): # you would need to go lower
logging.disable(logging.DEBUG)


###logging to a file

logging.basicConfig(filename='myProgramLog.txt' , level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

import random
heads = 0
for i in range(1,1001):
    if random .randint(0,1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfwat done')
    print('Heads came up' + str(heads) + ' times.')