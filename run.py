# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from admin import Admin
from ship import Ship
from board import Board
from validation import Validation

game = Admin(0, 0, 0, 0, 0, 0)

ship_size = 3

while True:
    name_input = Validation(input("Enter your name:\n"))
    if name_input.validate_name():
        print(f"Thank you {name_input.data}, let's get ready to play!\n")
        break


print("Please Choose Difficulty")
while True:
    difficulty_input = Validation(input(
        "Press E for Easy, M for Medium and H for Hard:\n").upper())
    if difficulty_input.validate_diff():
        game.difficulty(difficulty_input.data)
        break

print("Here are the rules:\n")
print(f"Each player has {game.ship_amount} ship/ships on their board")
print("They will be placed horizontally or vertically\n")
print("Your job is to guess the position of these ships")
print("Each player will take turns guessing coordinates")
print("This guess will either be a 'hit' or a 'miss'")
print("Hit all the positions taken up by a ship and you sink it")
print("Sink all of the ships and you win!\n")

print("Do you want to begin?")
while True:
    start_input = Validation(input("Y for Yes, N for No:").upper())
    if start_input.validate_start():
        break

ship_max = (game.ship_amount + ship_size)-1
player_score, comp_score = 0, 0

player_ships = Ship(ship_size, game.board_size, ship_max, game.ship_amount)
computer_ships = Ship(ship_size, game.board_size, ship_max, game.ship_amount)

game.board_1 = Board(game.board_size, "hidden")
game.board_2 = Board(game.board_size, "position")
game.board_3 = Board(game.board_size, "guess")

player_ships.position_ship(1, game.board_1)
computer_ships.position_ship(2, game.board_2)

player_places, computer_places = game.count_board_places()

game.check_board_ok(player_places, computer_places,
                    player_ships, computer_ships)

print("\n**Your Guesses**\n")
game.board_3.print_board()
print("\n****************\n")

print("\n**Your Board**\n")
game.board_2.print_board()
print("\n**************\n")

print(f"Target score is {game.point_target}")
print("Good Luck!!\n")

game.guess(player_score, comp_score)
