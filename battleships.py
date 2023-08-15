from random import randint


COMPUTER_BOARD = [[""] * 8 for x in range(8)]
PLAYER_BOARD = [[" "] * 8 for x in range(8)]

letter_be_number = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}


def print_field(field):
    print("     A B C D E F G H")
    print("     ---------------")
    row_number = 1
    for row in field:
        print("%d|%s" % (row_number, "|".join(row)))
        row_number += 1


def create_ships():
    pass


def ship_location():
    pass


def count_hits():
    pass


create_ships()
turns = 10
