import random
import time

class Admin:
    def __init__(self):
        self.players = 1
        self.time_limit = 60
        self.max_tries = 5
        self.rows = 5
        self.columns = 5
        self.no_tokens = 25

    def set_players(self, players):
        self.players = players
        return self.players

    def set_time_limit(self, time_limit):
        self.time_limit = time_limit
        return self.time_limit

    def set_max_tries(self, max_tries):
        self.max_tries = max_tries
        return self.max_tries

    def set_number_of_tokens(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.no_tokens = self.rows * self.columns
        return self.no_tokens, self.rows, self.columns

class Board:
    def __init__(self, board_admin):
        self.total_tokens = board_admin.no_tokens
        self.time = board_admin.time_limit
        self.attempts = board_admin.max_tries

    def flip(self, x, y):
        time_left = self.time
        current_attempt = 0
        while time_left > 0 and current_attempt >= self.attempts:
            time_left = time.time() - time_left
            if choice in Tokens.list_of_tokens and Tokens.sides is False:
                Tokens.sides = True
                if choice == WiningToken.wining_token:
                    return "You win!"
                else:
                    print("Please try again.\n")
                    print(time_left)
            else:
                print("Invalid choice, token is already flipped!")

            current_attempt += 1

        if current_attempt == self.attempts:
            print("You have no chances left!")
            
class Tokens(Board):
    def generate_tokens(self, board_admin):
        list_of_tokens = []
        sides = False
        token_coordinates = ""
        generated_tokens = 0
        x = 0
        y = 0
        while generated_tokens < board_admin.no_tokens:
            while x < board_admin.no_tokens:
                x += 1
                continue
            while y < board_admin.no_tokens:
                y += 1
                continue
            token_coordinates = str((x, y))
            list_of_tokens.append(token_coordinates)
            generated_tokens += 1
        return sides, list_of_tokens, token_coordinates

class WiningToken(Tokens):
    def generate_win_token(self):
        row = random.randint(0, Tokens.rows)
        column = random.randint(0, Tokens.columns)
        wining_token = str((row, column))
        return wining_token

class Player:
    def play(self, board_admin, input_board):
        while True:
            option = int(input("Menu\n==========\nSelect and option: \n1.Set up\n2.Play\n3.Quit\n"))
            if option == 1:
                board_admin.set_number_of_tokens(int(input("Set the desired number of rows: \n")), int(input("Set the desired number of columns: \n")))
                board_admin.set_time_limit(int(input("Set the time limit: \n")))
                board_admin.set_max_tries(int(input("Set the maximum amount of tries: \n")))
                board_admin.set_players(int(input("Enter the number of players: \n")))
            elif option == 2:
                Tokens.generate_tokens(Tokens, board_admin)
                input_board.flip(input("Enter the x-axis coordinate of the winning coin: "), input("Enter the y-axis coordinate of the winning coin: "))
            elif option == 3:
                quit()
            else:
                print("Invalid values!")

admin1 = Admin()
board1 = Board(admin1)
Player.play(Player, admin1, board1)
