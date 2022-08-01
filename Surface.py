import pygame


class Surface:

    def __init__(self):
        # Fps or framesper second loads our screen 32 times per secod to make it look like a video

        self.background_color = None
        self.SCREEN = None
        self.FPS = 32

        # it sets width and height of our scree window as per neet
        self.SCREENWIDTH = 289
        self.SCREENHEIGHT = 511

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.set_screen_dimension(height=self.SCREENHEIGHT, width=self.SCREENWIDTH)
        self.set_background_color(color=self.BLACK)
        pygame.display.set_caption("Game Pack")
        pygame.display.update()
        # self.font()

    def set_background_color(self, color=None):
        '''
        Use this function to set up background color of our screen.
        :param quiz: Object of the Screen_setup class to make changes to our screen.
        :param color: Sets color of the background. send color in tuple form(0,0,0) for black
        :return: None
        '''
        self.background_color = self.SCREEN.fill(color)
        pygame.display.update()

    def set_screen_dimension(self, height=None, width=None):
        # self.SCREENHEIGHT = height
        # self.SCREENWIDTH = width
        self.SCREEN = pygame.display.set_mode((width, height))
        pygame.display.update()

    def get_screen_dimention(self):
        return self.SCREENWIDTH, self.SCREENHEIGHT


class Game_Files:
    def __init__(self):
        self.GAME_SPRITE = {}
        self.GAME_SOUND = {}
        self.load_files()

    def load_files(self):
        self.GAME_SPRITE['snake_game'] = {}
        image = pygame.transform.scale(pygame.image.load('./Game_Sprites/snake_head.png'), (30, 30))
        self.GAME_SPRITE['snake_game']['snake_head'] = image
        self.GAME_SPRITE['welcome_screen'] = {}
        image = pygame.transform.scale(pygame.image.load('./Game_Sprites/game_background.jpg'), (211, 510))
        self.GAME_SPRITE['welcome_screen']['background'] = pygame.image.load('./Game_Sprites/game_background.jpg')
        self.GAME_SPRITE['guess_celebrity'] ={}

        image =pygame.transform.scale(pygame.image.load('./Game_Sprites/Question_Ui.png'),(290,511))
        self.GAME_SPRITE['guess_celebrity']['question_ui'] =image

        image = pygame.transform.scale(pygame.image.load('./Game_Sprites/You_are_correct.png'), (290, 511))
        self.GAME_SPRITE['guess_celebrity']['correct'] = image

        image = pygame.transform.scale(pygame.image.load('./Game_Sprites/You_are_wrong.png'), (290, 511))
        self.GAME_SPRITE['guess_celebrity']['wrong'] = image

        image = pygame.transform.scale(pygame.image.load('./Game_Sprites/end_screen.png'), (290, 511))
        self.GAME_SPRITE['guess_celebrity']['end'] = image

        self.GAME_SPRITE['cat_crossing'] = {}
        image = pygame.transform.scale(pygame.image.load('./Game_Sprites/road.png'),(290,511))
        self.GAME_SPRITE['cat_crossing']['road']=image


        pygame.mixer.init()
        self.GAME_SOUND['guess_celebrity']={}
        self.GAME_SOUND['guess_celebrity']['correct']=pygame.mixer.Sound('Game_Sound/correct.wav')
        self.GAME_SOUND['guess_celebrity']['wrong'] = pygame.mixer.Sound('./Game_Sound/wrong.wav')
        self.GAME_SOUND['guess_celebrity']['tick'] = pygame.mixer.Sound('./Game_Sound/tick_tick.wav')

class Print_Text():
    def __init__(self, surface):

        self.font_heading = None
        self.font_para = None
        self.font_sub = None
        self.font_heading_xl = None
        self.SURFACE = surface
        self.set_font()

    def set_font(self, font='freesansbold.ttf'):
        """
        call this function after pygame initialisation
        sets fonts to be used in game for font regularity
        :return:
        """
        # print("running")
        self.font_heading_xl = pygame.font.Font(font, 35)
        self.font_heading = pygame.font.Font(font, 30)
        self.font_sub = pygame.font.Font(font, 25)
        self.font_para = pygame.font.Font(font, 20)
        self.font_xs = pygame.font.Font(font,15)

    def print_Text(self, text, font_type='m', position_x=0, position_y=0, text_color=(255, 255, 255),
                   background_color=False, set_bg_color=(255, 255, 255)):
        """
        This method is used to print text on our screen follow to prompt and give argument to this function

        :param text: text you want to print
        :param font_type: select font size you want to print
        :param position_x: where do you want to print the text on the screen on X-axis (horizontal)
        :param position_y: where do you want to print the text on the screen on Y-axis (horizontal)
        :param text_color: give color of the text in tuple form eg (0,0,0) for black
        :param background_color: give color of the background of text in tuple form eg (255,255,255) for white
        :return: nothing
        """

        if font_type == "L" or font_type == "l":
            font = self.font_heading
        elif font_type == "m" or font_type == "m":
            font = self.font_sub
        elif font_type == 'xl' or font_type == "XL":
            font = self.font_heading_xl
        elif font_type == 'xs' or font_type == "XS":
            font = self.font_xs
        else:
            font = self.font_para

        if background_color:
            text_to = font.render(text, True, text_color, set_bg_color)
        else:
            background_color=None
            text_to = font.render(text, True, text_color, background_color)

        self.SURFACE.SCREEN.blit(text_to, (position_x, position_y))

        return text_to.get_width(), text_to.get_height()


class Button(Print_Text):
    def __init__(self, surface):
        """
        this is the button class constructor

        """
        super().__init__(surface)
        self.position_x = None
        self.position_y = None
        self.size_of_button = None

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

    def create(self, text, font_size='m', position_x=0, position_y=0, text_color=(0, 0, 0), background_color=False,
               set_bg_color=(255, 255, 255)):
        """
        This function is used to draw button on the screen follow the prompt and give arguments to it
                :param quiz: created object of Screen_setup
                :param font_size: select font size you want to print. eg- "L" for large.
                :param position_x: where do you want to print the text on the screen on X-axis (horizontal).
                :param position_y: where do you want to print the text on the screen on Y-axis (horizontal).
                :param text_color: give color of the text in tuple form. eg- (0,0,0) for black
                :param background_color: give color of the background of text in tuple form. eg-(255,255,255) for white.
                :return: nothing
                """

        self.position_x = position_x
        self.position_y = position_y

        self.size_of_button = self.print_Text(text, font_size, position_x, position_y, text_color=text_color,
                                              background_color=background_color, set_bg_color=set_bg_color)

    def isClicked(self):
        '''
        checks if user clicked on the button or not
        :param event: event variable of the pygame.event.get() to kow user movment
        :return: True or None
        '''
        mouse_position = pygame.mouse.get_pos()

        if self.position_x < mouse_position[0] < self.position_x + self.size_of_button[0]:
            if self.position_y < mouse_position[1] < self.position_y + self.size_of_button[1]:
                print("clicked")
                return True
