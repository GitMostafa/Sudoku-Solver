# Helpful text paragraphs for user
def welcome_message():
    print("\n|---------------------------------|")
    print("|                                 |")
    print("|   Welcome To My Sudoku Solver!  |")
    print("|                                 |")
    print("|---------------------------------|\n\n")

def available_options():
    print("Available Choices:")
    print("1. Input your own sudoko board for program to solve")
    print("2. Use an in-built sudoko board and check its solution\n")

def input_sudoku_board():
    print("Please input each number 1 by 1, as if you're filling the grid row by row")
    print("So you should enter the top left number first, then the one right to it and so on until the row is finished")
    print("This process is repeated for the number of rows in our grid, which is 9")
    print("So in total, you will have to input 81 numbers, where you should input 0 for an empty (not filled) square")
    print("Please be careful not to enter anything else other than a number that's between 0 and 9\n\n")


# Prints sudoku board in a formatted way
def print_board(board):
    for row in range(len(board)):
        if (row % 3 == 0) and (row != 0):
            print("-----------------------------")

        for col in range(len(board[row])):
            if col % 3 == 0:
                print(" | ", end = "")

            print(board[row][col], end = " ")

        print("|")

# Finds empty slot in sudoku board (denoted by 0)
def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return (row, col)      
    return None      

# Checks to see if specific number is allowed to be put in specific position
def is_valid(board, position, number):
    (row, col) = position
    # check row
    for colIndex in range(len(board[row])):
        if board[row][colIndex] == number:
            return False

    # check col
    for rowIndex in range(len(board)):
        if board[rowIndex][col] == number:
            return False
    
    # check box (where boxes are denoted by 0 to 3 in both orientations)   
    horizontalBox = row // 3
    verticalBox = col // 3

    for r in range(horizontalBox * 3, horizontalBox * 3 + 3):
        for c in range(verticalBox * 3, verticalBox * 3 + 3):
            if board[r][c] == number:
                return False
                
    return True

# Solves input board utilizing backtracking
def solve(board):
    insertionInfo = dict()
    isNumberInserted = False
    iterationNum = 0
    startNum = 1
    emptyPos = find_empty(board)

    while(emptyPos):
        (row, col) = emptyPos

        for num in range(startNum, 10):
            if is_valid(board, emptyPos, num):
                board[row][col] = num
                isNumberInserted = True
                break
        
        if (isNumberInserted):
            insertionInfo[iterationNum] = [num, row, col]
            iterationNum += 1
            startNum = 1
            isNumberInserted = False

        else:
            iterationNum -= 1
            if (iterationNum < 0):
                print("\n\nError! This board is not valid (can't be solved)!!")
                return False
            # Here backtracking becomes clear where if we couldn't insert a number in current position, we go to previous position and try a different sol
            startNum = insertionInfo[iterationNum][0] + 1
            r = insertionInfo[iterationNum][1]
            c = insertionInfo[iterationNum][2]
            insertionInfo.pop(iterationNum)
            board[r][c] = 0

        emptyPos = find_empty(board)

    return True


welcome_message()
available_options()

while True:
    userInput = input("Enter your choice (Input either 1 or 2)\n")
    try:
        choiceNum = int(userInput)
        if (choiceNum < 1) or (choiceNum > 2):
            continue
        break
    except ValueError:
        print("\nThis is not a valid choice!\n")
print("______________\n")

if choiceNum == 1:
    input_sudoku_board()
    inputBoard = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    for row in range(9):
        for col in range(9):
            while True:
                currRow = str(row + 1)
                currCol = str(col + 1)
                inputNumber = input("Enter number that's in row " + currRow + " and column " + currCol + "\n")
                try:
                    currIndexNum = int(inputNumber)
                    if (currIndexNum < 0) or (currIndexNum > 9):
                        continue
                    
                    # This part is to make sure that user inputs a board that doesn't violate sudoku laws (like having repeated numbers in same row)
                    if currIndexNum != 0:
                        if not is_valid(inputBoard, (row, col), currIndexNum):
                            print("\nError! Entering this number violates sudoku laws, please recheck the board and input a different number!\n")
                            continue
                    inputBoard[row][col] = currIndexNum
                    break
                except ValueError:
                    print("\nThis is not a valid number (Please enter a number between 0 and 9)!\n")
    print("\n______________\n")
    print("This is your inputted board:\n")
    print_board(inputBoard)

    if not find_empty(inputBoard):
       print("\nError, The input board has no empty squares!\n")

    else:
        input("\nTo solve this board press enter\n")
        if solve(inputBoard):
            print("The Solved Board:\n")
            print_board(inputBoard)


else:
    testBoard = [
        [5, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 7, 1, 0, 3, 5, 8, 0],
        [0, 2, 0, 0, 0, 0, 0, 9, 0],
        [0, 7, 0, 8, 0, 2, 0, 1, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 5, 0, 3, 0, 1, 0, 2, 0],
        [0, 1, 0, 0, 0, 0, 0, 6, 0],
        [0, 3, 4, 7, 0, 8, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 7]
    ]
    print("The Board Before Solving:\n")
    print_board(testBoard)
    input("\nTo solve this board press enter\n")
    print("\nThe Solved Board:\n")
    solve(testBoard)
    print_board(testBoard)

print("\n\n Thanks for using my Sudoku Solver!\n")