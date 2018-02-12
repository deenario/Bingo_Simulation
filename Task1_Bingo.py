import random


# Method that creates Player and assign 5 random numbers to each player.
def createPlayers(_rows, _column):
    player = 1
    # For loop that runs 100 times to create 100 rows for 100 players
    for x in range(_rows):
        Matrix[x][0] = player
        MatrixBool[x][0] = player
        # Another for loop that assigns random numbers to these 100 players
        for y in range(1, _column):
            Matrix[x][y] = random.randint(1, 80)
            MatrixBool[x][y] = False
        player += 1


# Method to check a random number with players.
def checkNumber(_rows, _column, _randomPick):
    for x in range(_rows):
        for y in range(1, _column):
            tempMatrix = Matrix[x][y]
            # checks if the player has the random number
            if tempMatrix == _randomPick:
                MatrixBool[x][y] = True
                # Method that checks if the player all 5 numbers are found
                checkBingo(x, _column)


# Method to check if Bingo state is reached
def checkBingo(_x, _column):
    global BINGO
    bingo = 0
    for y in range(1, _column + 1):
        # If all 5 numbers of a player are found it will hit bingo state.
        if bingo < 5:
            if y < 6:
                tempBool = MatrixBool[_x][y]
                if tempBool:
                    bingo += 1
        else:
            BINGO = 1
            print("Player ", MatrixBool[_x][0], " Won")
            print("BINGO")
    bingo = 0


# Variables deceleration and initialization.
rows = 100
column = 6
Matrix = [[0 for x in range(column)] for y in range(rows)]
MatrixBool = [[0 for x in range(column)] for y in range(rows)]
numberList = []
singleGameRunScore = []
totalGameRuns = 1000
singleGameRun = 0

# For loop to run 1000 games.
for x in range(totalGameRuns):
    print("Match ", x + 1)
    BINGO = 0
    # calls the create player method to create new players for every game.
    createPlayers(rows, column)
    while BINGO < 1:
        randomPick = random.randint(1, 80)
        # checks if the random number was already called before.
        if randomPick in numberList:
            randomPick = random.randint(1, 80)
        else:
            numberList.append(randomPick)
            checkNumber(rows, column, randomPick)
            singleGameRun += 1
    numberList.clear()
    singleGameRunScore.append(singleGameRun)
    singleGameRun = 0
    print()

# Prints the final results.
print("The List of how many Runs each game took to Get Bingo ")
print(singleGameRunScore)
average = sum(singleGameRunScore) / len(singleGameRunScore)
print("The average Number of Random numbers needed to Get BINGO in 1000 Games is ", average)
input("Program Finished Running")