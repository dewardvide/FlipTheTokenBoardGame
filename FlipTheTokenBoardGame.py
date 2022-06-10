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
class Board:
    Total_tokens = Admin.set_number_of_tokens(Admin)[0]
    Time = Admin.set_timelimit(Admin)
    Attempts = Admin.set_max_tries(Admin)

    def flip(self):
        timeleft = self.Time
        current_attempt = 0
        while timeleft == 0 and current_attempt >= self.Attempts:
            timeleft = timeleft - time.time()
            if Tokens.sides is False:
                x = input("Enter the x-axis coordinate of the winning coin: ")
                y = input("Enter the y-axis coordinate of the winning coin: ")
                choice = str((x, y))
                if choice == Tokens.generate_tokens(Tokens)[2]:
                    Tokens.sides = True
                if choice == WiningToken.generate_win_token(WiningToken):
                    print("You win!")
                    break
            else:
                print("Invalid choice, token is already flipped!")

            current_attempt += 1

class Tokens(Board):
    def generate_tokens(self):
        list_of_tokens = []
        sides = False
        token_coordinates = ""
        generated_tokens = 0
        x = 0
        y = 0
        while generated_tokens < Board.Total_tokens:
            while x < Admin.set_number_of_tokens(Admin)[1]:
                x += 1
                continue
            while y < Admin.set_number_of_tokens(Admin)[2]:
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
    def play(self):
        while True:
            option = input("Menu\n==========\nSelect and option: \n1.Set up\n2.Play\n3.Quit")
            if option == 1:
                Admin.set_number_of_tokens(Admin)
                Admin.set_timelimit(Admin)
                Admin.set_max_tries(Admin)
                Admin.set_players(Admin)
            elif option == 2:
                Tokens.generate_tokens(Tokens)
                Board.flip(Board)
            elif option == 3:
                quit()
            else:
                print("Invalid values!")
