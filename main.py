import sys

import pygame
import pygame.locals


from Surface import Surface, Print_Text, Button, Game_Files
from quiz_game import pygame_setup
from Guess_the_popularity import start,pygame_setup_guess,game_data
from Cat_crossing_game import cat_crossing_main

pygame.init()

class Start_Screen:
    def __init__(self):

        self.SURFACE = Surface()
        self.game_files = Game_Files()
        self.screen_dimension = self.SURFACE.get_screen_dimention()


class Welcome_Screen(Start_Screen):
    def __init__(self):

        super().__init__()

        self.button = None
        self.SURFACE.SCREEN.blit(self.game_files.GAME_SPRITE['welcome_screen']['background'], (0, 0))

        self.text = Print_Text(self.SURFACE)
        self.cat_crossing_button_p1= Button(self.SURFACE)
        self.cat_crossing_button_p2 = Button(self.SURFACE)
        self.quiz_button = Button(self.SURFACE)
        self.guess_insta_button_p1 = Button(self.SURFACE)
        self.guess_insta_button_p2 = Button(self.SURFACE)
        self.event_listenter()

    def on_surface(self):


        # self.quiz_button.create("B1", text_color=self.SURFACE.WHITE, background_color=False)
        self.text.print_Text("Game pack by", font_type='l', text_color=(0,255,0), position_x=self.screen_dimension[0] / 4 - self.screen_dimension[0] / 9, position_y=self.screen_dimension[1] / 13, background_color=None)
        self.text.print_Text("Reez Tuscano", position_x=self.screen_dimension[0] / 4 - self.screen_dimension[0] / 18, position_y=1 * self.screen_dimension[1] / 13 + self.screen_dimension[1] / 9, background_color=None)
        self.text.print_Text("-------Choose Game--------", background_color=True, set_bg_color=(102,178,255), position_x=0, position_y=1 * self.screen_dimension[1] / 13 + 1.8 * self.screen_dimension[1] / 6, )
        self.quiz_button.create("  Quiz Game  ", position_x=self.screen_dimension[0] / 4 - self.screen_dimension[0] / 18, position_y=1 * self.screen_dimension[1] / 13 + 2.5 * self.screen_dimension[1] / 6, background_color=True, text_color=(255, 255, 255), set_bg_color=(100, 100, 255))

        self.guess_insta_button_p1.create("  Guess popular  ", position_x=self.screen_dimension[0] / 4 - self.screen_dimension[0] / 18, position_y=1 * self.screen_dimension[1] / 13 + 3 * self.screen_dimension[1] / 6, background_color=True, text_color=(255, 255, 255), set_bg_color=(100, 100, 255))
        self.guess_insta_button_p2.create("   celebrity  ",
                                       position_x=self.screen_dimension[0] / 4 - self.screen_dimension[0] / 18,
                                       position_y=1 * self.screen_dimension[1] / 13 + 3.28 * self.screen_dimension[1] / 6,
                                       background_color=True, text_color=(255, 255, 255), set_bg_color=(100, 100, 255))

        self.cat_crossing_button_p1.create("  Cat Crossing  ", position_x=self.screen_dimension[0] / 4 - self.screen_dimension[0] / 18, position_y=1 * self.screen_dimension[1] / 13 + 3.7 * self.screen_dimension[1] / 6, background_color=True, text_color=(255, 255, 255), set_bg_color=(100, 100, 255))
        self.cat_crossing_button_p2.create("  the Road   ", position_x=self.screen_dimension[0] / 4 - self.screen_dimension[0] / 18, position_y=1 * self.screen_dimension[1] / 13 + 4 * self.screen_dimension[1] / 6, background_color=True, text_color=(255, 255, 255), set_bg_color=(100, 100, 255))



        pygame.display.update()





    def event_listenter(self):
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()


                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.quiz_button.isClicked():
                        pygame_setup.Home()
                        pygame.display.update()

                    elif self.guess_insta_button_p1.isClicked() or self.guess_insta_button_p2.isClicked():
                        pygame_setup_guess.Pygame_setup_Guess_popularity(self.SURFACE)

                    elif self.cat_crossing_button_p1.isClicked() or self.cat_crossing_button_p2.isClicked():
                        print("wrking")
                        # cat_crossing_main.Cat_crossing_main(self.SURFACE)


                else:
                    self.on_surface()







if __name__ == "__main__":
    Welcome_Screen()
