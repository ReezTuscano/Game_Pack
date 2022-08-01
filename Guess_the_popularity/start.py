import random
import sys

import pygame.display

from Guess_the_popularity import game_data
from Surface import Game_Files, Surface

game_files = Game_Files()
game_files.load_files()


class Guess_the_Popularity():

    def __init__(self):

        self.team_A = None
        self.team_B = None
        self.user_choice = None
        self.user_already_asked = []

    def get_instagram_celebrities(self):
        random_integer = self.get_random_number()

        return game_data.data[random_integer]

    def get_random_number(self):

        self.flag = 0
        while self.flag==0:
            random_integer = random.randint(0, len(game_data.data) - 1)
            if self.user_already_asked.count(random_integer) == 0:
                self.flag=1
                self.user_already_asked.append(random_integer)
                print(random_integer)

                return random_integer
            print("recursive call")

    def compare_celebrities(self):

        if self.team_A['follower_count'] > self.team_B['follower_count']:
            if self.user_choice == 'A':
                print('user wins')
                pygame.display.update()
                return 'WIN'
            else:
                print("user lost")
                pygame.display.update()
                return 'LOST'

        elif self.team_A['follower_count'] == self.team_B['follower_count']:
            print("that's a tie")
            return 'TIE'

        else:
            if self.user_choice == 'B':
                print('user wins')
                pygame.display.update()
                return 'WIN'
            else:
                print("user lost")
                pygame.display.update()

                return 'LOST'

    def set_user_input(self, user_choice):
        self.user_choice = user_choice
        return self.compare_celebrities()

    def get_team_A(self):
        self.team_A = self.get_instagram_celebrities()

        return f"Team A: {self.team_A['name']}, {self.team_A['description']}  from {self.team_A['country']}. "

    def get_team_B(self):
        self.team_B = self.get_instagram_celebrities()

        return f"Team B: {self.team_B['name']}, {self.team_B['description']}  from {self.team_B['country']}. "

# if __name__ == "__main__":
#     while True:
#         guess = Guess_the_Popularity()
#         print(guess.get_team_A())
#         print("\n")
#         print(guess.get_team_B())
#
#         print(guess.set_user_input(input("Team A or B")))
