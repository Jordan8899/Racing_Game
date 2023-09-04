# Imports
import pygame
import time
import random

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
lane_width = 10
lane_length = screen_height

lane_pos_x_1 = road_pos_x + 100 - (lane_width / 2)
lane_pos_x_2 = lane_pos_x_1 + 100
lane_pos_x_3 = lane_pos_x_2 + 100

lane_pos_y = 0

# Player Car Location and Size
car_pos_x = road_pos_x + lane_pos_x_1
car_pos_y = screen_height - 200

car_width = 50
car_length = 90

car_change_x = 0


# Game Icon and Name
game_name = pygame.display.set_caption("Racing Game")
game_icon = pygame.image.load("images/game_icon.png")
pygame.display.set_icon(game_icon)

# Clock used for FPS
clock = pygame.time.Clock()

# Enemy Racers Locations and Size
racer_width = car_width
racer_length = car_length

racer_car_1_pos_x = (lane_pos_x_1 - road_pos_x) / 2 + road_pos_x - (racer_width / 2)

racer_car_2_pos_x = lane_pos_x_2

racer_car_3_pos_x = lane_pos_x_3

racer_car_4_pos_x = lane_pos_x_3 + 50

racer_car_pos_y_1 = float(0 - racer_length)

racer_car_pos_y_2 = float(0 - racer_length)

racer_car_pos_y_3 = float(0 - racer_length)

racer_car_pos_y_4 = float(0 - racer_length)

# Speed Randomizer for Enemy Racers
speed_list = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Warm up Speed
speed_1 = 3
speed_2 = 7
speed_3 = 2 
speed_4 = 5
# Debug
debug = True

# Game Over Constant to allow game to play again
game_over = False

# Fonts

# Starting Score
score = 0


# Functions


# Randomizer Function
def randomizer():
    """
    
    This function will use speed_list to get access to all available speeds
    and randomly select one each time this function is called
    this function will return the speed and assign it to each car
    
    """
    speed_changes = len(speed_list) - 1
    randomized_number = random.randint(0, speed_changes)
    return speed_list[randomized_number]



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
                            [lane_pos_x_1, lane_pos_y, lane_width, lane_length])
    lane_2 = pygame.draw.rect(screen, colours["white"], 
                            [lane_pos_x_2, lane_pos_y, lane_width, lane_length])
    lane_3 = pygame.draw.rect(screen, colours["white"], 
                            [lane_pos_x_3, lane_pos_y, lane_width, lane_length])    
    
    
    # Player Car Model
    player_car = pygame.draw.rect(screen, colours["red"],
                                  [car_pos_x, car_pos_y, car_width, car_length])

    # Player Movement and Limiter Controller
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit_game = True
        
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          car_change_x = 5   
                     
        elif event.key == pygame.K_LEFT:
          car_change_x = -5
          
        elif event.key == pygame.K_ESCAPE:
          quit_game = True
            
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
          car_change_x = 0
    
    car_pos_x += car_change_x
    
    # Other Racers Model
    racer_1 = pygame.draw.rect(screen, colours["white"],
                               [racer_car_1_pos_x, racer_car_pos_y_1, racer_width, racer_length])
    racer_2 = pygame.draw.rect(screen, colours["white"],
                               [racer_car_2_pos_x, racer_car_pos_y_2, racer_width, racer_length])
    racer_3 = pygame.draw.rect(screen, colours["white"],
                               [racer_car_3_pos_x, racer_car_pos_y_3, racer_width, racer_length])
    racer_4 = pygame.draw.rect(screen, colours["white"],
                               [racer_car_4_pos_x, racer_car_pos_y_4, racer_width, racer_length])
       

    # Enemy Racers Movement
    if racer_car_pos_y_1 >= screen_height:
       racer_car_pos_y_1 = 0 - racer_length
       speed_1 = randomizer()
     
    if racer_car_pos_y_2 >= screen_height:
       racer_car_pos_y_2 = 0 - racer_length
       speed_2 = randomizer()
       
    if racer_car_pos_y_3 >= screen_height:
       racer_car_pos_y_3 = 0 - racer_length
       speed_3 = randomizer()
       
    if racer_car_pos_y_4 >= screen_height:
       racer_car_pos_y_4 = 0 - racer_length
       speed_4 = randomizer()

    racer_car_pos_y_1 += speed_1
    racer_car_pos_y_2 += speed_2
    racer_car_pos_y_3 += speed_3
    racer_car_pos_y_4 += speed_4

    # Collision Detection  
    if car_pos_x + car_width >= racer_car_1_pos_x and car_pos_x <= racer_car_1_pos_x + racer_width and car_pos_y + car_length >= racer_car_pos_y_1 and car_pos_y <= racer_car_pos_y_1 + racer_length:
       print("Death Car 1")
    
    elif car_pos_x + car_width >= racer_car_2_pos_x and car_pos_x <= racer_car_2_pos_x + racer_width and car_pos_y + car_length >= racer_car_pos_y_2 and car_pos_y <= racer_car_pos_y_2 + racer_length:
       print("Death Car 2")
       
    elif car_pos_x + car_width >= racer_car_3_pos_x and car_pos_x <= racer_car_3_pos_x + racer_width and car_pos_y + car_length >= racer_car_pos_y_3 and car_pos_y <= racer_car_pos_y_3 + racer_length:
       print("Death Car 3")
       
    elif car_pos_x + car_width >= racer_car_4_pos_x and car_pos_x <= racer_car_4_pos_x + racer_width and car_pos_y + car_length >= racer_car_pos_y_4 and car_pos_y <= racer_car_pos_y_4 + racer_length:
       print("Death Car 4")
       
    # Score


    # Highscore

    
    # Background Creation
    
    # Debug
    if debug == True:
      # Lane Locations
      print("\n*** Lane Strip Locations ***")
      print("Lane 1 ", lane_1)
      print("Lane 2 ", lane_2)
      print("Lane 3 ", lane_3)
      
      # Car Lane Lengths
      print("\n*** Car Lane Lengths ***")
      print("Car Lane Length 1 ", lane_pos_x_1 - road_pos_x)
      print("Car Lane Length 2 ", lane_pos_x_2 - (lane_pos_x_1 + lane_width))
      print("Car Lane Length 3 ", lane_pos_x_3 - (lane_pos_x_2 + lane_width))
      print("Car Lane Length 4 ", road_width + road_pos_x - (lane_pos_x_3 + lane_width))
      
      # Player Car and Opposistion Locations
      print("\n*** Player and other Car Locations ***")
      print("Player Car ", player_car)
      print("Racer 1 ", racer_1)
      
      # Stops the console from being overloaded with information
      debug = False


    # Pygame Display Update
    pygame.display.update()

    # FPS
    clock.tick(40)


# Game Over
