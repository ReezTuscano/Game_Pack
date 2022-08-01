import pygame


class Screen_Setup:
    """
    this is a class containing all the Knowledge required to set up and run pygame.
    just instantiate Screen setup and all the things would be take care of to set up pygame.
    """

    def __init__(self):
        self.font_heading_xl = None
        self.background_color = None
        self.font_para = None
        self.font_sub = None
        self.font_heading = None

        # Fps or framesper second loads our screen 32 times per secod to make it look like a video
        self.FPS = 32

        # it sets width and height of our scree window as per neet
        self.SCREENWIDTH = 289
        self.SCREENHEIGHT = 511

        # screen is the surface over which we draw our game
        self.SCREEN = pygame.display.set_mode((self.SCREENWIDTH, self.SCREENHEIGHT))

        # game sprite and sound contains all the required pictures and game t display on the screen its ot compulsary
        # but its optional.
        self.GAME_SPRITE = {}
        self.GAME_SOUND = {}

    def set_background_color(self, quiz, color):
        '''
        Use this function to set up background color of our screen.
        :param quiz: Object of the Screen_setup class to make changes to our screen.
        :param color: Sets color of the background. send color in tuple form(0,0,0) for black
        :return: None
        '''
        self.background_color = quiz.SCREEN.fill(color)

    def font(self):
        """
        call this function after pygame initialisation
        sets fonts to be used in game for font regularity
        :return:
        """
        # print("running")
        self.font_heading_xl = pygame.font.Font('freesansbold.ttf', 40)
        self.font_heading = pygame.font.Font('freesansbold.ttf', 30)
        self.font_sub = pygame.font.Font('freesansbold.ttf', 20)
        self.font_para = pygame.font.Font('freesansbold.ttf', 14)

    def print_Text(self, quiz, text, font_type, position_x, position_y, text_color, background_color=False):
        """
        This method is used to print text on our screen follow to prompt and give argument to this function
        :param quiz: created object of Screen_setup
        :param text: text you want to print
        :param font_type: select font size you want to print
        :param position_x: where do you want to print the text on the screen on X-axis (horizontal)
        :param position_y: where do you want to print the text on the screen on Y-axis (horizontal)
        :param text_color: give color of the text in tuple form eg (0,0,0) for black
        :param background_color: give color of the background of text in tuple form eg (255,255,255) for white
        :return: nothing
        """

        if font_type == "L" or font_type == "l":
            font = quiz.font_heading
        elif font_type == "m" or font_type == "m":
            font = quiz.font_sub
        elif font_type == 'xl' or font_type == "XL":
            font = quiz.font_heading_xl
        else:
            font = quiz.font_para

        if background_color:
            text_to = font.render(text, True, text_color, background_color)
        else:
            text_to = font.render(text, True, text_color, background_color)

        quiz.SCREEN.blit(text_to, (position_x, position_y))

        return text_to.get_width(), text_to.get_height()


class Button:
    def __init__(self, text):
        """
        this is the button class constructor
        :param text: where it take text to print on the button
        """
        self.position_x = None
        self.position_y = None
        self.size_of_button = None
        self.text = text


    def draw(self, quiz, font_size, position_x, position_y, text_color, background_color=False):
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
        if self.text != "":
            self.size_of_button = quiz.print_Text(quiz, self.text, font_size, position_x, position_y, text_color,
                                                  background_color)

    def isClicked(self, event):
        '''
        checks if user clicked on the button or not
        :param event: event variable of the pygame.event.get() to kow user movment
        :return: True or None
        '''
        if self.position_x < event.pos[0] < self.position_x + self.size_of_button[0]:
            if self.position_y < event.pos[1] < self.position_y + self.size_of_button[1]:
                return True
