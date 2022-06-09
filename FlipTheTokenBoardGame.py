import random
import time

class Admin:
    def set_players(self):
        players = int(input("Enter the number of players: \n"))
        return players

    def set_timelimit(self):
        timelimit = int(input("Set the time limit: \n"))
        return timelimit

    def set_max_tries(self):
        max_tries = int(input("Set the maximum amount of tries: \n"))
        return max_tries

    def set_number_of_tokens(self):
        rows = int(input("Set the desired number of rows: \n"))
        columns = int(input("Set the desired number of columns: \n"))
        no_tokens = rows * columns
        return no_tokens, rows, columns

def countdown(t = Admin.set_timelimit()):
   pass

class Board:
    Total_tokens = Admin.set_number_of_tokens()[0]
    Time = Admin.set_timelimit()
    Attempts = Admin.set_max_tries()

    def flip(self):
        timeleft = self.Time
        current_attempt = 0
        while timeleft == 0 and current_attempt >= self.Attempts:
            timeleft = timeleft - time.time()
            if Tokens.sides is False:
                x = input("Enter the x-axis coordinate of the winning coin: ")
                y = input("Enter the y-axis coordinate of the winning coin: ")
                choice = str((x, y))
                if Tokens.token_coordinates == choice:
                    Tokens.sides = True
                if choice == WiningToken.generate_win_token():
                    print("You win!")
                    break
            else:
                print("Invalid choice, token is already flipped!")

            current_attempt += 1

class Tokens(Board):
    sides = False
    token_coordinates = ""
    generated_tokens = 0
    def gen_tokens:
        while generated_tokens <= Admin.set_number_of_tokens()[0]:
            def coordinates(self):
                rows = int(Admin.set_number_of_tokens()[1])
                columns = int(Admin.set_number_of_tokens()[2])
                return rows, columns

            token_coordinates = str(coordinates())
            generated_tokens += 1
            return token_coordinates

class WiningToken(Tokens):
    def generate_win_token(self):
        row = random.randint(0, Tokens.rows)
        column = random.randint(0, Tokens.columns)
        wining_token = str((row, column))
        return wining_token


class Player:
