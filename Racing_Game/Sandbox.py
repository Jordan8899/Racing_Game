import pygame

pygame.init()

# Screen Width and Height
screen_width = 600
screen_height = 800

# Set screen display window
screen = pygame.display.set_mode((screen_width, screen_height))

back_track = "this_is_a_working_directory/music/stylish_rock_beat.mp3"
crash_audio = "music/car_crash"

music = True

while True:
    if music:
        try:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(back_track))
        
        except:
            # Prints into console one time
            # shows music file not located top of console
            print("\n***** Music file not located *****\n")
            music = False