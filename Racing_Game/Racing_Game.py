# Imports
import pygame

# Constants


# Pygame Initilisation so that pygame works through the code
pygame.init()

# Colour Dictonary with colour values used within this game
colours = {
    "dark_green": (14, 181, 36),
    "red": (255, 0, 0),
    "gray": (161, 161, 161)
    
    }


# Screen Width and Height
screen_width = 600
screen_height = 800

# Set screen display
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Icon and Name
game_name = pygame.display.set_caption("Racing Game")
game_icon = pygame.image.load("images/game_icon.png")
pygame.display.set_icon(game_icon)


# Game Over Constant to allow game to play again
game_over = False

# Fonts

# Starting Score
score = 0



# Functions


# Movement Function




# Main Routine


# Play Again Loop
while not game_over:
    
    # Background Colour
    screen.fill(colours["dark_green"])
    
    
    # Player Car Model

    # Other Racers Model

    # Other Racers Movement

    # Player Movement and Limiter Controller

    # Score

    # Highscore

    # Road Creation

    # Lanes Creation

    # Background Creation
    
    # Pygame Display Update
    pygame.display.update()

# Game Over