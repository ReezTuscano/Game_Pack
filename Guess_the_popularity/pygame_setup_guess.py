import sys
import textwrap
import time

import pygame.display

import main
from Guess_the_popularity import start
# from main import Welcome_Screen
from Surface import Print_Text
from Surface import Game_Files, Button

game_files = Game_Files()
game_files.load_files()


class Pygame_setup_Guess_popularity():
    def __init__(self, surface):

        self.score = 0
        self.SURFACE = surface
        self.guess = start.Guess_the_Popularity()
        self.text = Print_Text(self.SURFACE)
        pygame.mixer.init()
        game_files.GAME_SOUND['guess_celebrity']['tick'].play()
        self.print_question()

    def print_question(self):
        self.SURFACE.set_background_color((0, 0, 0))

        self.SURFACE.SCREEN.blit(game_files.GAME_SPRITE['guess_celebrity']['question_ui'], (0, 0))

        for j in range(0, 2):
            if j == 0:
                text1 = self.guess.get_team_A()
            else:
                text1 = self.guess.get_team_B()
            print(text1)
            wrapped_text = textwrap.wrap(text1, 22)

            for i in range(0, len(wrapped_text)):
                self.text.print_Text(wrapped_text[i], font_type='s', position_x=10,
                                     position_y=30 + i * 25 + j * 300,
                                     background_color=False, set_bg_color=(255, 255, 255))
                # if j == 1:
                #
                #     self.text.print_Text(wrapped_text[i], font_type='s', position_x=10,
                #                          position_y=30+  i * 25 + j * 280,
                #                          background_color=False, set_bg_color=(255, 255, 255))
                # else:
                #     self.text.print_Text(wrapped_text[i], font_type='s', position_x=10,
                #                          position_y=25 + i * 25 + j * 280,
                #                          background_color=False, set_bg_color=(255, 255, 255))
        pygame.display.update()
        self.event_listener()

    def isClicked(self):
        '''
        checks if user clicked on the button or not
        :param event: event variable of the pygame.event.get() to kow user movment
        :return: True or None
        '''
        mouse_position = pygame.mouse.get_pos()

        if 0 < mouse_position[0] < self.SURFACE.SCREENWIDTH:
            if 0 < mouse_position[1] < self.SURFACE.SCREENHEIGHT / 2 - 10:
                print("clicked A")
                return 'clickedA'
            elif self.SURFACE.SCREENHEIGHT / 2 - 10 < mouse_position[1] < self.SURFACE.SCREENHEIGHT:
                print("clicked B")
                return 'clickedB'

    def event_listener(self):
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()


                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.isClicked() =='clickedA':
                        print("A")
                        if 'WIN' == self.guess.set_user_input('A'):
                            self.correct()
                        else:
                            self.wrong()
                    elif self.isClicked() =='clickedB':
                        print("B")
                        if 'WIN' == self.guess.set_user_input('B'):
                            self.correct()
                        else:
                            self.wrong()

    def correct(self):
        self.SURFACE.SCREEN.blit(game_files.GAME_SPRITE['guess_celebrity']['correct'], (0, 0))
        pygame.display.update()
        self.score +=1

        correct = game_files.GAME_SOUND['guess_celebrity']['correct']
        correct.play()
        time.sleep(1)
        self.print_question()

    def wrong(self):
        self.SURFACE.SCREEN.blit(game_files.GAME_SPRITE['guess_celebrity']['wrong'], (0, 0))
        pygame.display.update()

        game_files.GAME_SOUND['guess_celebrity']['tick'].stop()
        wrong = game_files.GAME_SOUND['guess_celebrity']['wrong']
        wrong.play()
        time.sleep(1)
        self.end_screen()

    def end_screen(self):
        self.SURFACE.set_background_color((0,0,0))
        self.SURFACE.SCREEN.blit(game_files.GAME_SPRITE['guess_celebrity']['end'], (0, 0))
        self.text.print_Text("You", position_x=10, position_y=210, font_type='L')
        self.text.print_Text("Lose!!", position_x=10, position_y=250, font_type='L')
        self.text.print_Text("Score", position_x=204, position_y=210, font_type='L')
        self.text.print_Text(str(self.score), position_x=220, position_y=250, font_type='L')

        home_button = Button(self.SURFACE)
        home_button.create("Home", position_x=115, position_y=75)

        retry_button = Button(self.SURFACE)
        retry_button.create("Retry", position_x=115, position_y=400)
        pygame.display.update()
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()


                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                    if 60< mouse_position[0] < 250:
                        if 10< mouse_position[1] <140:
                            print("clicked Home")


                            main.Welcome_Screen()


                        elif  350< mouse_position[1] <480 :
                            print("clicked Retry")
                            Pygame_setup_Guess_popularity(self.SURFACE)





