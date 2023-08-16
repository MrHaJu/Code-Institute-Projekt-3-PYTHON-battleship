from random import randint


# Invisible Board holding ship locations
COMPUTER_BOARD = [[" "] * 8 for x in range(8)]
# Player Borads displays hits and misses
PLAYER_BOARD = [[" "] * 8 for x in range(8)]

def print_field(field):
    print("     A B C D E F G H")
    print("     ---------------")
    row_number = 1
    for row in field:
        print("%d|%s" % (row_number, "|".join(row)))
        row_number += 1

letter_be_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}

# 5 Ships created by Computer
def create_ships(field):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while field[ship_row][ship_column] == "X":
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




