def main():
    # The main function
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2)  # The function that starts the game is also in here.

def intro():
    # This function introduces the rules of the game Tic Tac Toe
    print("Hello! Welcome to Pam's Tic Tac Toe game!")
    print("\n")
    print("Rules: Player 1 and player 2, represented by X and O, take turns "
          "marking the spaces in a 3*3 grid. The player who succeeds in placing "
          "three of their marks in a horizontal, vertical, or diagonal row wins.")
    print("\n")
    input("Press enter to continue.")
    print("\n")

def create_grid():
    # This function creates a blank playboard
    print("Here is the playboard: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board

def sym():
    # This function decides the players' symbols
    symbol_1 = input("Player 1, do you want to be X or O? ").upper()
    while symbol_1 not in ["X", "O"]:
        symbol_1 = input("Invalid choice. Please choose X or O: ").upper()
    symbol_2 = "O" if symbol_1 == "X" else "X"
    print(f"Player 2, you are {symbol_2}.")
    input("Press enter to continue.")
    print("\n")
    return symbol_1, symbol_2

def startGamming(board, symbol_1, symbol_2, count):
    # This function starts the game.

    # Decides the turn
    player = symbol_1 if count % 2 == 0 else symbol_2
    print(f"Player {player}, it is your turn.")

    # Get valid row and column
    row, column = get_valid_move(board)

    # Locates player's symbol on the board
    board[row][column] = player
    return board

def get_valid_move(board):
    while True:
        try:
            row = int(input("Pick a row (0-2): "))
            column = int(input("Pick a column (0-2): "))
            if row not in [0, 1, 2] or column not in [0, 1, 2]:
                print("Out of bounds. Try again.")
            elif board[row][column] != " ":
                print("That spot is already taken. Try again.")
            else:
                return row, column
        except ValueError:
            print("Please enter a valid number.")

def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
    while count <= 9 and winner:
        board = startGamming(board, symbol_1, symbol_2, count)
        printPretty(board)
        if isWinner(board, symbol_1, symbol_2):
            print("Game over.")
            break
        if count == 9:
            print("The board is full. Game over.")
            print("There is a tie.")
        count += 1

def printPretty(board):
    # This function prints the board nicely
    print("---+---+---")
    for row in board:
        print(" | ".join(row))
        print("---+---+---")

def isWinner(board, symbol_1, symbol_2):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            print(f"Player {board[i][0]} wins!")
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            print(f"Player {board[0][i]} wins!")
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        print(f"Player {board[0][0]} wins!")
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        print(f"Player {board[0][2]} wins!")
        return True

    return False

# Call Main
main()
