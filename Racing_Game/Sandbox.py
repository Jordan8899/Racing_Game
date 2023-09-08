import pygame, random

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

# Speed List
speed_list = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Functions
def randomizer():
    """
    
    This function will use speed_list to get access to all available 
    speeds and randomly select one each time this function is called
    this function will return the speed and assign it to each car
    
    """
    speed_changes = len(speed_list) - 1
    randomized_number = random.randint(0, speed_changes)
    
    return speed_list[randomized_number]

for i in range(0, 10):
    speed = randomizer()
    print(speed)

while True:
    screen.fill(colours["dark_green"])
    pygame.display.update()    