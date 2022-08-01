import sys
import time
import pygame
from pygame.locals import *

import main
from quiz_game import quiz_brain

# sys.path.append('C:/Users/reezq/Desktop/Python Project/Pygame Games')
from quiz_game import screen_setup
from quiz_game import Sounds
from quiz_game import data



class Home:
    def __init__(self):

        self.click = None
        self.obj = None
        self.wrong_sound = None
        self.right_sound = None
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.quiz = screen_setup.Screen_Setup()

        # sets Scree widndow name as Quiz Game
        pygame.display.set_caption('Quiz Game ')

        # Created buttons from object of button class
        self.try_again = screen_setup.Button(" Try Again  ")
        self.home_button = screen_setup.Button("  Home  ")
        self.start_button = screen_setup.Button("     Start     ")
        self.true_button = screen_setup.Button("  True  ")
        self.false_button = screen_setup.Button("  False  ")
        self.back_button = screen_setup.Button(" <--- Back  ")
        self.category1_button = screen_setup.Button("        GK        ")
        self.category2_button = screen_setup.Button("     Animal    ")
        self.category3_button = screen_setup.Button("   Science    ")
        self.category4_button = screen_setup.Button("   Cartoons  ")

        # self.obj = data.Return_Question_Bank('Animal')
        self.quest = data.Offline_Dataset("Gk")
        self.quiz_brain = quiz_brain.Quiz_Brain(self.quest.get_quest())

        self.startPygame()

    def startPygame(self):
        pygame.init()
        self.quiz.font()
        self.quiz.set_background_color(self.quiz, self.black)
        self.right_sound = pygame.mixer.Sound('quiz_game/Sounds/success_sound.wav')
        self.click = pygame.mixer.Sound('quiz_game/Sounds/Clicking_button.wav')
        self.wrong_sound = pygame.mixer.Sound('quiz_game/Sounds/wrong_sound.mp3')

        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                elif event.type == MOUSEBUTTONDOWN:

                    print("pos x :", event.pos[0])
                    self.quiz.set_background_color(self.quiz, self.black)
                    # if self.home_button.isClicked(event):
                    #     print("clicked home")

                    if self.start_button.isClicked(event):
                        self.click.play()
                        time.sleep(0.5)
                        self.question_ui()
                        self.quiz.set_background_color(self.quiz, self.black)


                    elif self.category1_button.isClicked(event):
                        self.click.play()
                        time.sleep(0.5)
                        self.obj = data.Return_Question_Bank('Gk')
                        self.quiz_brain = quiz_brain.Quiz_Brain(self.obj.quest)
                        self.question_ui()
                        self.quiz.set_background_color(self.quiz, self.black)

                    elif self.category2_button.isClicked(event):
                        self.click.play()
                        time.sleep(0.5)
                        self.obj = data.Return_Question_Bank('Animal')
                        self.quiz_brain = quiz_brain.Quiz_Brain(self.obj.quest)
                        self.question_ui()
                        self.quiz.set_background_color(self.quiz, self.black)

                    elif self.category3_button.isClicked(event):
                        self.click.play()
                        time.sleep(0.5)
                        self.obj = data.Return_Question_Bank('Science')
                        self.quiz_brain = quiz_brain.Quiz_Brain(self.obj.quest)
                        self.question_ui()
                        self.quiz.set_background_color(self.quiz, self.black)

                    elif self.category4_button.isClicked(event):
                        self.click.play()
                        time.sleep(0.5)

                        self.quest = data.Offline_Dataset("Cartoon")

                        self.quiz_brain = quiz_brain.Quiz_Brain(self.quest.get_quest())
                        self.question_ui()
                        self.quiz.set_background_color(self.quiz, self.black)

                    elif self.back_button.isClicked(event):
                        self.click.play()
                        main.Welcome_Screen()
                        time.sleep(0.5)







                else:
                    self.welcome_Screen()

            pygame.display.update()

    def welcome_Screen(self):
        """
        home screen is defined and is printed when user is not doing anything
        :return:
        """
        self.quiz.print_Text(self.quiz, "Welcome", "xl", self.quiz.SCREENWIDTH // 4 - 15,
                             1 * self.quiz.SCREENHEIGHT // 8 + 10,
                             self.white)

        self.quiz.print_Text(self.quiz, "Quiz game by Reez Tuscano", "m", 8, 2 * self.quiz.SCREENHEIGHT // 8 + 15,
                             self.white)

        self.start_button.draw(self.quiz, 'l', self.quiz.SCREENWIDTH / 4, self.quiz.SCREENHEIGHT / 4 + 80,
                               self.black,
                               self.white)
        self.back_button.draw(self.quiz, 'l', 0, 0,
                               self.black,
                               self.white)

        self.quiz.print_Text(self.quiz, "-------Select Category-------", "m", 20,
                             2 * self.quiz.SCREENHEIGHT / 4 + 20,
                             self.white)

        # category buttons are defined
        self.category1_button.draw(self.quiz, 'l', self.quiz.SCREENWIDTH / 4, 2 * self.quiz.SCREENHEIGHT / 4 + 60 + 10,
                                   self.black,
                                   self.white)
        self.category2_button.draw(self.quiz, 'l', self.quiz.SCREENWIDTH / 4, 2 * self.quiz.SCREENHEIGHT / 4 + 110 - 5,
                                   self.black,
                                   self.white)
        self.category3_button.draw(self.quiz, 'l', self.quiz.SCREENWIDTH / 4, 2 * self.quiz.SCREENHEIGHT / 4 + 160 - 20,
                                   self.black,
                                   self.white)
        self.category4_button.draw(self.quiz, 'l', self.quiz.SCREENWIDTH / 4, 2 * self.quiz.SCREENHEIGHT / 4 + 210 - 35,
                                   self.black,
                                   self.white)

    def question_ui(self):
        """
        main game UI logic to display questions
        :return:
        """
        self.quiz.set_background_color(self.quiz, self.black)
        self.quiz_brain.score = 0
        self.quiz_brain.question_number = 0
        while self.quiz_brain.when_to_exit():
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                elif event.type == MOUSEBUTTONDOWN:
                    if self.true_button.isClicked(event):
                        print("clicked true")
                        self.quiz_brain.user_Choice('t')
                        if self.quiz_brain.right_or_wrong:
                            self.quiz.print_Text(self.quiz, "You are Correct", "m", 1 * self.quiz.SCREENWIDTH // 4,
                                                 7 * self.quiz.SCREENHEIGHT // 8,
                                                 self.white)
                            self.right_sound.play()
                            pygame.display.update()
                            time.sleep(3)



                        else:
                            self.quiz.print_Text(self.quiz, "You are Wrong", "m", 1 * self.quiz.SCREENWIDTH // 4,
                                                 7 * self.quiz.SCREENHEIGHT // 8,
                                                 self.white)
                            self.wrong_sound.play()
                            pygame.display.update()
                            time.sleep(1)



                    elif self.false_button.isClicked(event):
                        print("clicked false")
                        self.quiz_brain.user_Choice('f')
                        if self.quiz_brain.right_or_wrong:
                            self.quiz.print_Text(self.quiz, "You are Correct", "m", 1 * self.quiz.SCREENWIDTH // 4,
                                                 7 * self.quiz.SCREENHEIGHT // 8,
                                                 self.white)
                            self.right_sound.play()
                            pygame.display.update()
                            time.sleep(3)



                        else:
                            self.quiz.print_Text(self.quiz, "You are Wrong", "m", 1 * self.quiz.SCREENWIDTH // 4,
                                                 7 * self.quiz.SCREENHEIGHT // 8,
                                                 self.white)
                            self.wrong_sound.play()
                            pygame.display.update()
                            time.sleep(1)




                    elif self.back_button.isClicked(event):
                        self.click.play()
                        main.pygame_setup.Home()
                        time.sleep(0.5)

                    self.right_sound.stop()
                    self.wrong_sound.stop()


                else:
                    self.quiz.set_background_color(self.quiz, self.black)
                    wrapped_text_list = self.quiz_brain.wrap_text()
                    for i in range(0, len(wrapped_text_list)):
                        self.quiz.print_Text(self.quiz, wrapped_text_list[i], "m", 10,
                                             1 * self.quiz.SCREENHEIGHT // 8 + 10 + i * 30, self.white)

                    self.true_button.draw(self.quiz, 'L', self.quiz.SCREENWIDTH / 4 - 45,
                                          3 * self.quiz.SCREENHEIGHT / 4 - 25.,
                                          self.black,
                                          self.white)
                    self.false_button.draw(self.quiz, 'L', self.quiz.SCREENWIDTH / 4 + 85,
                                           3 * self.quiz.SCREENHEIGHT / 4 - 25,
                                           self.black,
                                           self.white)
                    self.back_button.draw(self.quiz, 'm', 190, 490,
                                          self.black,
                                          self.white)
                    string_score = "Score: " + str(self.quiz_brain.get_final_score()) + " / " + str(10)
                    self.quiz.print_Text(self.quiz, string_score, "m", self.quiz.SCREENWIDTH - 120,
                                         0,
                                         self.white)
                    self.quiz.print_Text(self.quiz, "Q", "L", 5,
                                         5,
                                         self.white)
                    self.quiz.print_Text(self.quiz, self.quiz_brain.get_question_number(), "m", 40,
                                         15,
                                         self.white)

            pygame.display.update()
        self.end_Ui()

    def end_Ui(self):
        """
        end screen of our game.
        :return:
        """
        self.quiz.set_background_color(self.quiz, self.black)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.try_again.isClicked(event):
                        return
                else:
                    self.try_again.draw(self.quiz, 'l', self.quiz.SCREENWIDTH / 4 - 10,
                                        2 * self.quiz.SCREENHEIGHT / 4 - 25,
                                        self.black,
                                        self.white)
                    string_score = str(self.quiz_brain.get_final_score()) + " / " + str(10)

                    self.quiz.print_Text(self.quiz, "You have scored ", "l", 25,
                                         1 * self.quiz.SCREENHEIGHT // 8,
                                         self.white)
                    self.quiz.print_Text(self.quiz, string_score, "L", self.quiz.SCREENWIDTH // 2 - 40,
                                         2 * self.quiz.SCREENHEIGHT // 8 + 10,
                                         self.white)

            pygame.display.update()
