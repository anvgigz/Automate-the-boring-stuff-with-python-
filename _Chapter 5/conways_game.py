###Conways gaame of life

import random, time, copy

WIDTH = 240
HEIGHT = 20

##Creatr a list of list for the cells::
nextCells = []

for x in range(WIDTH):
    column = [] #create a new comumn.
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')  #aDD A LIVING CELL
        else:
            column.append(' ') ##Add a dead cell.
    nextCells.append(column) ###nextCells is a list of column lists.

while True: ## Main program Loop
    print('/n/n/n/n/n') ##Seperate each step with newlines.
    currentCells = copy.deepcopy(nextCells)

    ##Print currentcells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') ##Print the # or space.
        print() ##Print a newline at the end of the row.

    ##Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            ##Get Neighboring coordinates::
            ## `% WIDTH` ensures left coord is always within 0 and WIDTH -1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            #Count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-left Neighbor is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 ## Top neighbor is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 ##Top-right neighbor is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 ##Left neighbor is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 #Right neighbor is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # bottom-left neighbor is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # bottom neighbor is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive

                #Set cell based on Conway's game of life rules..
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                ##Living cells with 2 or 3 neighbors stay alive::
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                ##Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                ##Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(.02) ##Add 1 1-second pause to reduce flickering