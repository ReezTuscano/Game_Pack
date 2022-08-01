import pygame
class Load_Files:
    def __init__(self, quiz):

        quiz.GAME_SPRITE['numbers'] = (
            pygame.image.load('../Sprites/0.png').convert_alpha(),
            pygame.image.load('../Sprites/1.png').convert_alpha(),
            pygame.image.load('../Sprites/2.png').convert_alpha(),
            pygame.image.load('../Sprites/3.png').convert_alpha(),
            pygame.image.load('../Sprites/4.png').convert_alpha(),
            pygame.image.load('../Sprites/5.png').convert_alpha(),
            pygame.image.load('../Sprites/6.png').convert_alpha(),
            pygame.image.load('../Sprites/7.png').convert_alpha(),
            pygame.image.load('../Sprites/8.png').convert_alpha(),
            pygame.image.load('../Sprites/9.png').convert_alpha(),

        )

        quiz.GAME_SPRITE['home'] = pygame.image.load("../Sprites/quiz_game_home.jpg")




