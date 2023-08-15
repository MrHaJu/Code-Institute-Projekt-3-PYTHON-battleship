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


def ship_location():
    pass


def count_hits():
    pass


create_ships()
turns = 10
