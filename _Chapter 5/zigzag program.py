import time, sys

indent = 0 # how many spaces to indent
indentincreasing = True #Whenever the indentation is increasing or not.

try:
    while True: #The main loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) #Pause for 1/10 of a second

        if indentincreasing:
            #Increase the number of spaces.
            indent = indent + 1
            if indent == 20:
                #Change direction
                indentincreasing = False
        
        else:
            # Decreasing the number of spaced.
            indent = indent - 1
            if indent == 0:
                indentincreasing = True
except KeyboardInterrupt:
    sys.exit()