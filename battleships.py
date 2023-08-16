from random import randint
import msvcrt
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


letter_be_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}


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
        print_field(field)
        ship_row, ship_column = ship_location()
        while field[ship_row][ship_column] == "X":
            print("That location is already taken, choose another")
            ship_row, ship_column = ship_location()
        field[ship_row][ship_column] = "X"

# Input function to guess where the computer ships are
def ship_location():
    column = input("Please choose a ship column A-H: ").strip().upper()
    while column not in "ABCDEFGH" or column == "":
        print("Please choose a valid column")
        column = input("Choose the column of the ship: ").strip().upper()
    row = input("Please chose a ship row 1-8: ").strip().upper()
    while row not in "12345678" or row == "":
        print("Please choose a valid row")
        row = input("Choose the row of the ship: ").strip().upper()
    return int(row) - 1, letter_be_number[column]


# checks if all ships are hit
def count_hits(field):
    count = 0
    for row in field:
        for column in row:
            if column == "X":
                count += 1
    return count


def enter_or_esc():
    print("Press Enter to continue or ESC to quit...")
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\x1b':  # ESC key
                exit()  # ends the Game
            elif key == b'\r':  # Enter key
                break  # go on with the game


# Main function to start the game
if __name__ == "__main__":
    create_ships(COMPUTER_BOARD)
    turns = 6  # you have 6 Turns to guess
    while turns > 0:  # as long as the turns are grater 0 the while loop runs
        clear_terminal()  # clears the terminal after each round
        print("BATTLESHIP\n")
        print_field(PLAYER_BOARD)
        row, column = ship_location()
        if PLAYER_BOARD[row][column] == "-" or PLAYER_BOARD[row][column] == "X":  # if you guess twice the same it
            print("\nYou already had that guess\n")  # prints an error
        elif COMPUTER_BOARD[row][column] == "X":  # if you hit a ship
            print("\nYou hit a Battleship\n")  # it prints a hit Message
            PLAYER_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("\nYou missed\n")  # if you miss a guess it prints the miss message
            PLAYER_BOARD[row][column] = "-"
            turns -= 1
        if count_hits(PLAYER_BOARD) == 5:
            print(
                "\nYou got all the Battleships\n"
            )  # Winning message if all battleships are hit
            break
        print(
            "\nYou have " + str(turns) + " turns remaining\n"
        )  # prints every round the remaining turns
        if turns == 0:  # if all turns are over
            print("Game over\n")  #   game over message
        enter_or_esc()  # after each round you have to press the Enter to go on or ESC to end the game
