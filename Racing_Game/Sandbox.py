import pygame

pygame.init()

# Screen Width and Height
screen_width = 600
screen_height = 800

# Set screen display window
screen = pygame.display.set_mode((screen_width, screen_height))

colours = {
    "dark_green": (14, 181, 36),
    "red": (255, 0, 0),
    "gray": (161, 161, 161),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "pink": (255, 0, 239)
}

print(colours)

while True:
    screen.fill(colours["dark_green"])
    pygame.display.update()
