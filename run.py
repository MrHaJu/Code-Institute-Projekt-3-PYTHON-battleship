from random import randint
import keyboard
import os


# Invisible Board holding ship locations
COMPUTER_BOARD = [[" "] * 8 for x in range(8)]
# Player Borads holding player ship locations
PLAYER_BOARD = [[" "] * 8 for x in range(8)]
# holding hit or misses by Player
PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
# holding hit or misses by Computer
COMPUTER_GUESS_BOARD = [[" "] * 8 for i in range(8)]


# function to clear the terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def print_field(field):
    print("  A B C D E F G H")
    print("  ---------------")
    row_number = 1
    for row in field:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


letter_be_number = {"A": 0,
                    "B": 1,
                    "C": 2,
                    "D": 3,
                    "E": 4,
                    "F": 5,
                    "G": 6,
                    "H": 7}


# 5 Ships created by Computer
def computer_create_ships(field):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while field[ship_row][ship_column] == "X":
            ship_row, ship_column = ship_location()
        field[ship_row][ship_column] = "X"


# 5 ships to create by Player
def player_create_ships(field):
    for ship in range(5):
        clear_terminal()
        print("\nBATTLESHIP\n")
        print("\nYou have to choose 5 ship Locations for your playfield\n")
        print("After that, the game starts automatically\n")
        print_field(field)
        ship_row, ship_column = ship_location()
        while field[ship_row][ship_column] == "X":
            print("That location is already taken, choose another")
            ship_row, ship_column = ship_location()
        field[ship_row][ship_column] = "X"


# Input function to guess where the computer ships are
def ship_location():
    while True:
        try:
            column = input("Please choose a ship column A-H: ").strip().upper()
            if column not in "ABCDEFGH" or column == "":
                raise KeyError
            if column in "ABCDEFGH":
                column = letter_be_number[column]
                break
        except KeyError:
            print("Please choose a valid column")
    while True:
        try:
            row = input("Please chose a ship row 1-8: ").strip().upper()
            if row not in "12345678" or row == "":
                raise ValueError
            if row in "12345678":
                row = int(row) - 1
                break
        except ValueError:
            print("Please choose a valid row")
    return row, column


# checks if all ships are hit
def count_hits(field):
    count = 0
    for row in field:
        for column in row:
            if column == "X":
                count += 1
    return count


def enter_or_esc():
    print("Press Enter to continue or space to quit...")
    while True:
        if keyboard.is_pressed("space"):  # Check if the space key is pressed
            exit()  # Ends the game
        elif keyboard.is_pressed("enter"):  # Check if the Enter key is pressed
            break  # Continue with the game


# Main function to start the game
if __name__ == "__main__":
    computer_create_ships(COMPUTER_BOARD)
    player_create_ships(PLAYER_BOARD)
    turns = 10  # you have 6 Turns to guess
    while turns > 0:  # as long as the turns are greater than 0, the loop runs
        clear_terminal()  # clears the terminal after each round
        print("BATTLESHIP\n")
        print("Each round begins with your turn. ")
        print("when you have made your move, the computer makes a move.\n")
        print("Everyone has 10 turns. The first to sink all ships wins. ")
        print("When all turns have been used up and ships are still standing,")
        print("the player with the most hits wins.\n")
        print("Computer moves")
        print_field(COMPUTER_GUESS_BOARD)
        print("\nPlayer")
        print_field(PLAYER_BOARD)
        print("\nMake your move\n")
        print_field(PLAYER_GUESS_BOARD)
        row, column = ship_location()
        if (
            PLAYER_GUESS_BOARD[row][column] == "-"
            or PLAYER_GUESS_BOARD[row][column] == "X"
        ):
            print("\nYou already had that guess\n")
        elif COMPUTER_BOARD[row][column] == "X":
            print("\nYou hit a Battleship\n")
            PLAYER_GUESS_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("\nYou missed\n")
            PLAYER_GUESS_BOARD[row][column] = "-"
            turns -= 1
        if count_hits(PLAYER_GUESS_BOARD) == 5:
            print("\nYou got all the Battleships\n")
            break
        print("\nYou have " + str(turns) + " turns remaining\n")
        if turns == 0:
            print("Game over\n")
            break
        # after each round press the Enter to go on or ESC to end the game
        enter_or_esc()

        # Computer's turn
        row, column = randint(0, 7), randint(0, 7)
        while (
            COMPUTER_GUESS_BOARD[row][column] == "-"
            or COMPUTER_GUESS_BOARD[row][column] == "X"
        ):
            row, column = randint(0, 7), randint(0, 7)
        if PLAYER_BOARD[row][column] == "X":
            COMPUTER_GUESS_BOARD[row][column] = "X"
        else:
            COMPUTER_GUESS_BOARD[row][column] = "-"

        clear_terminal()  # clears the terminal after each round
        print("BATTLESHIP\n")
        print("Player\n")
        print_field(PLAYER_GUESS_BOARD)
        print("\nComputer\n")
        print_field(COMPUTER_GUESS_BOARD)

        if count_hits(COMPUTER_GUESS_BOARD) == 5:
            print("\nSorry, the computer won.")
            break

    player_hits = count_hits(PLAYER_GUESS_BOARD)
    computer_hits = count_hits(COMPUTER_GUESS_BOARD)

    clear_terminal()
    print("BATTLESHIP - GAME OVER\n")
    print("Player")
    print_field(PLAYER_GUESS_BOARD)
    print("\nComputer")
    print_field(COMPUTER_GUESS_BOARD)

    if player_hits > computer_hits:
        print("\nCongratulations! You win with", player_hits, "hits!")
    elif computer_hits > player_hits:
        print("\nSorry, the computer wins with", computer_hits, "hits!")
    else:
        print("\nIt's a tie! Both have", player_hits, "hits.")

    input("\nPress Enter to exit...")  # Wait for user input before exiting
