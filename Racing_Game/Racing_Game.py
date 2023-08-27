# Imports
import pygame

# Constants


# Pygame Initilisation so that pygame works through the code
pygame.init()

# Colour Dictonary with colour values used within this game
colours = {
    "dark_green": (14, 181, 36),
    "red": (255, 0, 0),
    "gray": (161, 161, 161),
    "white": (255, 255, 255),
    "black": (0, 0, 0)
    
    }


# Screen Width and Height
screen_width = 600
screen_height = 800

# Set screen display
screen = pygame.display.set_mode((screen_width, screen_height))

# Road Location and Size
road_pos_x = 100
road_pos_y = 0

road_width = 400
road_length = screen_height

# Lanes Location and Size
lane_width = 20
lane_length = screen_height

lane_pos_x = road_pos_x - lane_width + 100
lane_pos_y = 0

# Player Car Location and Size
car_pos_x = road_pos_x + lane_pos_x
car_pos_y = screen_height - 200

car_width = 50
car_length = 90

car_change_x = 0

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
    
    # Road Creation
    road = pygame.draw.rect(screen, colours["gray"], 
                            [road_pos_x, road_pos_y, road_width, road_length])
    
    # Lanes Creation
    lane_1 = pygame.draw.rect(screen, colours["white"], 
                            [lane_pos_x, lane_pos_y, lane_width, lane_length])
    lane_2 = pygame.draw.rect(screen, colours["white"], 
                            [lane_pos_x + 100 + lane_width, lane_pos_y, lane_width, lane_length])
    lane_3 = pygame.draw.rect(screen, colours["white"], 
                            [lane_pos_x + 200 + lane_width, lane_pos_y, lane_width, lane_length])    
    
    
    # Player Car Model
    player_car = pygame.draw.rect(screen, colours["red"],
                                  [car_pos_x, car_pos_y, car_width, car_length])

    # Player Movement and Limiter Controller
    for event in pygame.event.get():
      
      if event.type == pygame.QUIT:
        quit_game = True
        
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          car_change_x = -10   
                     
        elif event.key == pygame.K_LEFT:
          car_change_x = 10
          
        elif event.key == pygame.K_ESCAPE:
          quit_game = True
    
    car_pos_x += car_change_x
    # Other Racers Model


    # Other Racers Movement


    # Score


    # Highscore

    
    # Background Creation
    
    # Pygame Display Update
    pygame.display.update()

# Game Over