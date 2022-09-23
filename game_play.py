import ShipGame
from colorama import Fore


class GameError(Exception):
    pass


def place_ship(game, length, player_num):
    coordinate = input(Fore.WHITE + "Please enter the top-left most coordinate of your ship of length "
                       + str(length) + ": ").upper()
    direction = input("Please enter whether the ship spans C (a column, vertical) or R (a row, horizontal): ") \
        .upper()
    if game.place_ship(player_num, length, coordinate, direction) is False:
        print(Fore.RED + "Error, please try again.")
        return place_ship(game, length, player_num)
    else:
        return


def take_turn(game, player_num):
    coordinate = input(Fore.WHITE + "Please enter the coordinate you would like to fire on: ").upper()
    if game.fire_torpedo(player_num, coordinate) is False:
        print(Fore.RED + "Error, please try again.")
        return take_turn(game, player_num)
    else:
        return


def game_play():
    """implements user friendly game play for testing"""
    game = ShipGame.ShipGame()
    player_1 = input("Please enter your name: ")
    player_2 = input("Please enter your opponent's name: ")
    for num in range(1, 3):
        if num == 1:
            player_num = "first"
            print(player_1 + ", it is now your turn to place your ships.")
        else:
            player_num = "second"
            print(player_2 + ", it is now your turn to place your ships.")
        ships_lengths = [2, 3, 3, 4, 5]
        for length in ships_lengths:
            place_ship(game, length, player_num)
        print("A bunch of lines now follow to ensure the other player cannot see your input.")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
    while game.get_current_state() == "UNFINISHED":
        for num in range(1, 3):
            if num == 1:
                player_num = "first"
                print(player_1 + ", it is your turn to fire on your opponent.")
            else:
                if game.get_current_state() != "UNFINISHED":
                    break
                player_num = "second"
                print(player_2 + ", it is your turn to fire on your opponent.")
            take_turn(game, player_num)
    if game.get_current_state() == "FIRST_WON":
        print(player_1 + " wins! Congratulations!")
    elif game.get_current_state() == "SECOND_WON":
        print(player_2 + " wins! Congratulations!")


game_play()
