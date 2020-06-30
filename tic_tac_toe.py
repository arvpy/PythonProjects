# Tic-Tac-Toe

print('''  Tic-Tac-Toe
  (1) (2) (3)
  (4) (5) (6)
  (7) (8) (9)
    ''')  # Displaying the positions
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]  # Displaying the empty board
count = 0  # Declaring global variable


def display_board():
    print(board[0] + "   " + board[1] + "   " + board[2])
    print(board[3] + "   " + board[4] + "   " + board[5])
    print(board[6] + "   " + board[7] + "   " + board[8])
    check_win()

def counter():  # To check count and set X and O accordingly
    global count
    count += 1
    return count


def value_repeat():  # To checks if the position is filled already
    print("Please choose another position")
    global count
    count -= 1
    handle_turn()


def handle_turn():  # Swaps between X and O
    x = counter()
    try:            # To check for invalid input
        pos = int(input("Choose the position"))
        if x % 2 != 0:
            if board[pos - 1] == '-':
                board[pos - 1] = 'X'
            else:
                value_repeat()
        else:
            if board[pos - 1] == '-':
                board[pos - 1] = 'O'
            else:
                value_repeat()
        display_board()
        handle_turn()
    except ValueError:
        print("Invalid input")
        value_repeat()


def check_win():  # Checks for winner by checking horizontal, vertical, and diagonal match


    if board[0] == board[1] == board[2] != '-':
        print("You win!!! Mr."+board[0])
        exit(0)
    elif board[3] == board[4] == board[5] != '-':
        print("You win!!! Mr."+board[3])
        exit(0)
    elif board[6] == board[7] == board[8] != '-':
        print("You win!!! Mr."+board[6])
        exit(0)

    # checking columns
    elif board[0] == board[3] == board[6] != '-':
        print("You win!!! Mr."+board[0])
        exit(0)
    elif board[1] == board[4] == board[7] != '-':
        print("You win!!! Mr."+board[1])
        exit(0)
    elif board[2] == board[5] == board[8] != '-':
        print("You win!!! Mr."+board[2])
        exit(0)
    # checking diagonals
    elif board[0] == board[4] == board[8] != '-':
        print("You win!!! Mr. "+board[0])
        exit(0)
    elif board[2] == board[4] == board[6] != '-':
        print("You win!!! Mr."+board[2])
        exit(0)
    elif board[0] != '-' and board[1] != '-' and board[2] != '-' and board[3] != '-' and board[4] != '-' and board[5] != '-' and board[6] != '-' and board[7] != '-' and board[8] != '-':
        print("Oops!!Its a Tie")
        exit(0)
    else:
        handle_turn()


handle_turn()
