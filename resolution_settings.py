from __future__ import division  # For Python 2.7
import pygame
from pygame.locals import *

# POSITIONS CONSTANTS
SCREEN_CHECK_OFFSET_X = 125
SCREEN_CHECK_OFFSET_Y = 3
SCREEN_OFFSET_TEXT = 25
CHECK_BOX_OFFSET = 100
TEXT_Y_MODIFIER = 50
CHECK_BOX_SIZE = 30
FULL_SCREEN_Y = 415
WINDOWED_Y = 370
B_ACCEPT_Y = 20
RED_X_X = 40
RED_X_Y = 40
TEXT_Y = 80

# SCREEN AND FONT MODIFIERS
FULL_SCREEN_OPTION = 6
RESOLUTION_OPTIONS = 4
WINDOWED_OPTION = 5
ANTI_ANILIASING = 1
SCREEN_X = 500
SCREEN_Y = 600
CLICKED = 1

# COLORS CONSTANTS
GREY = (100, 100, 100)
TEXT_COLOR = (20, 20, 20)


class SettingsMenu:
    def __init__(self):
        pygame.init()
        self.__resolutions16_10 = ['1280x800', '1440x900', ' 1680x1050', ' 1920x1200', ' 2560x1600']
        self.__resolutions16_9 = ['852x480', '1280x720', '1365x768', '1600x900', ' 1920x1080']
        self.__resolutions4_3 = ['1024x768', '1152x864', '1280x960', ' 1400x1050', ' 1600x1200']
        self.__resolutions3_2 = ['720x480', '1152x768', '1280x564', '1440x960', ' 2880x1920']

    def load_menu_objects(self):
        # Variables
        b_options = []
        x_choice = None
        screen_setting = 1 
        res_text_list = []
        res_pos_list = []
        check_box_list = []
        pygame.display.Info()
        users_settings = []
        running = True
        click_window_option = False
        font = pygame.font.Font('resources/fonts/3Dventure.ttf', 30)
        font_accept = pygame.font.Font('resources/fonts/3Dventure.ttf', 80)
        user_resolution = pygame.display.Info().current_w / pygame.display.Info().current_h
        screen_x = pygame.display.Info().current_w
        screen_y = pygame.display.Info().current_h

        # Load background
        screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        background = pygame.Surface(screen.get_size()).convert()
        background.fill(GREY)

        # Images and fonts
        icon = pygame.image.load('resources/images/game_icon.png').convert_alpha()
        check_box = pygame.image.load("resources/images/check_box.png").convert_alpha()
        check_box = pygame.transform.scale(check_box, (CHECK_BOX_SIZE, CHECK_BOX_SIZE))
        red_x = pygame.image.load("resources/images/red_x.png").convert_alpha()
        full_text = font.render("Full Screen", ANTI_ANILIASING, TEXT_COLOR)
        window_text = font.render("Windowed", ANTI_ANILIASING, TEXT_COLOR)
        settings_font = font.render("Game Settings", ANTI_ANILIASING, TEXT_COLOR)
        accept_font = font_accept.render("Play", ANTI_ANILIASING, TEXT_COLOR)

        # Get resolution options
        if user_resolution == int(16 / 10):
            for i in range(len(self.__resolutions16_10)):
                res_text = font.render(self.__resolutions16_10[i], ANTI_ANILIASING, TEXT_COLOR)
                res_text_list.append(res_text)
                res_pos = res_text.get_rect()
                res_pos.centerx = background.get_rect().centerx
                res_pos.centery += (TEXT_Y + (i * TEXT_Y_MODIFIER))
                res_pos_list.append(res_pos)

                check_box_list.append(check_box)
                b_accept_pos = check_box.get_rect()
                b_accept_pos.centerx = res_pos.centerx - CHECK_BOX_OFFSET
                b_accept_pos.centery = res_pos.centery
                b_options.append(b_accept_pos)

        elif user_resolution == 16 / 9:
            for i in range(len(self.__resolutions16_9)):
                res_text = font.render(self.__resolutions16_9[i], ANTI_ANILIASING, TEXT_COLOR)
                res_text_list.append(res_text)
                res_pos = res_text.get_rect()
                res_pos.centerx = background.get_rect().centerx
                res_pos.centery += (TEXT_Y + (i * TEXT_Y_MODIFIER))
                res_pos_list.append(res_pos)

                check_box_list.append(check_box)
                b_accept_pos = check_box.get_rect()
                b_accept_pos.centerx = res_pos.centerx - CHECK_BOX_OFFSET
                b_accept_pos.centery = res_pos.centery
                b_options.append(b_accept_pos)

        elif user_resolution == 4 / 3:
            for i in range(len(self.__resolutions4_3)):
                res_text = font.render(self.__resolutions4_3[i], ANTI_ANILIASING, TEXT_COLOR)
                res_text_list.append(res_text)
                res_pos = res_text.get_rect()
                res_pos.centerx = background.get_rect().centerx
                res_pos.centery += (TEXT_Y + (i * TEXT_Y_MODIFIER))
                res_pos_list.append(res_pos)

                check_box_list.append(check_box)
                b_accept_pos = check_box.get_rect()
                b_accept_pos.centerx = res_pos.centerx - CHECK_BOX_OFFSET
                b_accept_pos.centery = res_pos.centery
                b_options.append(b_accept_pos)

        elif user_resolution == 3 / 2:
            for i in range(len(self.__resolutions3_2)):
                res_text = font.render(self.__resolutions3_2[i], ANTI_ANILIASING, TEXT_COLOR)
                res_text_list.append(res_text)
                res_pos = res_text.get_rect()
                res_pos.centerx = background.get_rect().centerx
                res_pos.centery += (TEXT_Y + (i * TEXT_Y_MODIFIER))
                res_pos_list.append(res_pos)

                check_box_list.append(check_box)
                b_accept_pos = check_box.get_rect()
                b_accept_pos.centerx = res_pos.centerx - CHECK_BOX_OFFSET
                b_accept_pos.centery = res_pos.centery
                b_options.append(b_accept_pos)
        else:
            print("Unsupported resolution")

        # Screen options
        full_text_pos = full_text.get_rect()
        full_text_pos.centerx = background.get_rect().centerx + SCREEN_OFFSET_TEXT
        full_text_pos.centery = FULL_SCREEN_Y
        check_box_list.append(check_box)
        b_accept_pos = check_box.get_rect()
        b_accept_pos.centerx = full_text_pos.centerx - SCREEN_CHECK_OFFSET_X
        b_accept_pos.centery = full_text_pos.centery - SCREEN_CHECK_OFFSET_Y
        b_options.append(b_accept_pos)

        window_text_pos = full_text.get_rect()
        window_text_pos.centerx = background.get_rect().centerx + SCREEN_OFFSET_TEXT
        window_text_pos.centery = WINDOWED_Y
        check_box_list.append(check_box)
        b_accept_pos = check_box.get_rect()
        b_accept_pos.centerx = window_text_pos.centerx - SCREEN_CHECK_OFFSET_X
        b_accept_pos.centery = window_text_pos.centery - SCREEN_CHECK_OFFSET_Y
        b_options.append(b_accept_pos)

        # Loads the icon and caption
        pygame.display.set_caption('16-Bit Hero Arcade')
        pygame.display.set_icon(icon)

        # Accept button
        b_accept_pos = accept_font.get_rect()
        b_accept_pos.centerx = background.get_rect().centerx
        b_accept_pos.centery = (background.get_rect().height - accept_font.get_rect().height - B_ACCEPT_Y)

        # Render font
        settings_font_pos = settings_font.get_rect()
        settings_font_pos.centerx = background.get_rect().centerx
        settings_font_pos.centery += 20

        # Red X
        red_x = pygame.transform.scale(red_x, (CHECK_BOX_SIZE, CHECK_BOX_SIZE))
        red_x_pos = check_box.get_rect()

        red_x_two = pygame.transform.scale(red_x, (CHECK_BOX_SIZE, CHECK_BOX_SIZE))
        red_x_two_pos = check_box.get_rect()

        while running:
            screen.fill(GREY)

            # Blits the fonts and window text
            screen.blit(settings_font, settings_font_pos)
            screen.blit(accept_font, b_accept_pos)
            screen.blit(full_text, full_text_pos)
            screen.blit(window_text, window_text_pos)

            # Blits the resolution text
            for i in range(len(res_text_list)):
                screen.blit(res_text_list[i], res_pos_list[i])

            # Blits check boxs
            for i in range(len(check_box_list)):
                screen.blit(check_box_list[i], b_options[i])

            # Gets the mouse x and y
            mouse_pos = pygame.mouse.get_pos()
            (on_click1, on_click2, on_click3) = pygame.mouse.get_pressed()

            # Get the users selection
            for i in range(len(b_options)):
                if b_options[i].collidepoint(mouse_pos) & on_click1 == CLICKED:

                    if user_resolution == 16 / 10 and i <= RESOLUTION_OPTIONS:
                        if len(self.__resolutions16_10[i]) == 9 or len(self.__resolutions16_10[i]) == 8:
                            screen_x = int(self.__resolutions16_10[i][0:4])
                            screen_y = int(self.__resolutions16_10[i][5:9])
                            x_choice = i

                        elif len(self.__resolutions16_10[i]) == 10:
                            screen_x = int(self.__resolutions16_10[i][1:5])
                            screen_y = int(self.__resolutions16_10[i][6:10])
                            x_choice = i
                        else:
                            screen_x = int(self.__resolutions16_10[i][0:2])
                            screen_y = int(self.__resolutions16_10[i][4:7])
                            x_choice = i

                    elif user_resolution == 16 / 9 and i <= RESOLUTION_OPTIONS:
                        if len(self.__resolutions16_9[i]) == 9 or len(self.__resolutions16_9[i]) == 8:
                            screen_x = int(self.__resolutions16_9[i][0:4])
                            screen_y = int(self.__resolutions16_9[i][5:9])
                            x_choice = i

                        elif len(self.__resolutions16_9[i]) == 10:
                            screen_x = int(self.__resolutions16_9[i][1:5])
                            screen_y = int(self.__resolutions16_9[i][6:10])
                            x_choice = i
                        else:
                            screen_x = int(self.__resolutions16_9[i][0:3])
                            screen_y = int(self.__resolutions16_9[i][4:7])
                            x_choice = i

                    elif user_resolution == 4 / 3 and i <= RESOLUTION_OPTIONS:
                        if len(self.__resolutions4_3[i]) == 9 or len(self.__resolutions4_3[i]) == 8:
                            screen_x = int(self.__resolutions4_3[i][0:4])
                            screen_y = int(self.__resolutions4_3[i][5:9])
                            x_choice = i

                        elif len(self.__resolutions4_3[i]) == 10:
                            screen_x = int(self.__resolutions4_3[i][1:5])
                            screen_y = int(self.__resolutions4_3[i][6:10])
                            x_choice = i
                        else:
                            screen_x = int(self.__resolutions4_3[i][0:2])
                            screen_y = int(self.__resolutions4_3[i][4:7])
                            x_choice = i

                    elif user_resolution == 3 / 2 and i <= RESOLUTION_OPTIONS:
                        if len(self.__resolutions3_2[i]) == 9 or len(self.__resolutions3_2[i]) == 8:
                            screen_x = int(self.__resolutions3_2[i][0:4])
                            screen_y = int(self.__resolutions3_2[i][5:9])
                            x_choice = i

                        elif len(self.__resolutions3_2[i]) == 10:
                            screen_x = int(self.__resolutions3_2[i][1:5])
                            screen_y = int(self.__resolutions3_2[i][6:10])
                            x_choice = i

                        else:
                            screen_x = int(self.__resolutions3_2[i][0:2])
                            screen_y = int(self.__resolutions3_2[i][4:7])
                            x_choice = i
                    else:
                        if i == WINDOWED_OPTION:
                            red_x_two_pos.centerx = b_options[WINDOWED_OPTION].centerx
                            red_x_two_pos.centery = b_options[WINDOWED_OPTION].centery
                            click_window_option = True
                            screen_setting = 0

                        elif i == FULL_SCREEN_OPTION:
                            red_x_two_pos.centerx = b_options[FULL_SCREEN_OPTION].centerx
                            red_x_two_pos.centery = b_options[FULL_SCREEN_OPTION].centery
                            click_window_option = True
                            screen_setting = 1

            if click_window_option:
                screen.blit(red_x_two, red_x_two_pos)

            if x_choice is not None:
                red_x_pos.centerx = b_options[x_choice].centerx
                red_x_pos.centery = b_options[x_choice].centery
                screen.blit(red_x, red_x_pos)

            for event in pygame.event.get():
                if event.type == QUIT:

                    running = False

            if b_accept_pos.collidepoint(mouse_pos) & on_click1 == CLICKED:
                users_settings.append(screen_x)
                users_settings.append(screen_y)
                users_settings.append(screen_setting)
                return users_settings

            # Updates the screen
            pygame.display.flip()
