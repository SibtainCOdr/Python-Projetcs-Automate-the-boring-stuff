import random, time, copy
from turtle import width
WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells:
nextcells = []
for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # Adds living cell
        else:
            column.append(' ') # Adds a dead cell
    nextcells.append(column) #next cells is a list of columns list

while True: # Main program loop
    print('\n\n\n\n\n') #separate rach step with new lines
    currentcells = copy.deepcopy(nextcells)
    # Print currentcells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentcells[x][y], end='') # print the # or space
        print() # Print a mewline at the end of the row 
    
    # Calculate the next step's cells based on current step's cell:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring co ordinates:
            # % WIDTH ensure leftcoord is always between 0 and WIDTH - 1
            leftcord = (x - 1) % WIDTH
            rightcord = (x + 1) % WIDTH
            abovecord = (y - 1) % HEIGHT
            belowcord = (y + 1) % HEIGHT

            # Count the number of living neighbors:
            numneighbors = 0
            if currentcells[leftcord][abovecord] == '#':
                numneighbors += 1 # top left neighbor is alive
            if currentcells[x][abovecord] == '#':
                numneighbors += 1 #Top neighbor is alive
            if currentcells[rightcord][abovecord] == '#':
                numneighbors += 1 # top right neighbor is alive
            if currentcells[leftcord][y] == '#':
                numneighbors += 1 #left neighbor is alive
            if currentcells[rightcord][y] == '#':
                numneighbors += 1 # RIght neighhbor is alive
            if currentcells[leftcord][belowcord] == '#':
                numneighbors += 1 # Bottom-left neighbor is alive
            if currentcells[x][belowcord] == '#':
                numneighbors += 1 # bottom neighbor is alive
            if currentcells[rightcord][belowcord] == '#':
                numneighbors += 1 # bottom right neighbor is alive

            # Set the cell based on conways game of life rules:
            if currentcells[x][y] == '#' and (numneighbors == 2 or numneighbors == 3):
                # living cells with 2 or 3 neighbors stay alive:
                nextcells[x][y] = '#'
            elif currentcells[x][y] == '' and numneighbors == 3:
                # Dead cell wih 3 neighbors become alive:
                nextcells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextcells[x][y] = ' '
    time.sleep(1)
