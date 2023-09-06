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
    "black": (0, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "pink": (255, 0, 239)
    
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

lane_pos_x_1 = road_pos_x + 100 - (lane_width / 2) - 2.5
lane_pos_x_2 = lane_pos_x_1 + 100 + 2.5
lane_pos_x_3 = lane_pos_x_2 + 100 + 2.5

lane_pos_y = 0

# Player Car Location and Size
car_pos_x = screen_width / 2
car_pos_y = screen_height - 200

car_width = 60
car_length = 100

car_change_x = 0

# Player Movement Limiter
move_left = True
move_right = True

# Game Icon and Name
game_name = pygame.display.set_caption("Racing Game")
game_icon = pygame.image.load("images/game_icon.png")
pygame.display.set_icon(game_icon)

# Fonts
font = pygame.font.Font("freesansbold.ttf", 25)

# Clock used for FPS
clock = pygame.time.Clock()

# Enemy Racers Locations and Size
racer_width = car_width
racer_length = car_length

racer_car_1_pos_x = (lane_pos_x_1 - road_pos_x) / 2 + road_pos_x - (racer_width / 2)

racer_car_2_pos_x = racer_car_1_pos_x + 102.5

racer_car_3_pos_x = racer_car_1_pos_x + 205

racer_car_4_pos_x = racer_car_1_pos_x + 307.5

racer_car_pos_y_1 = 0 - racer_length

racer_car_pos_y_2 = 0 - racer_length

racer_car_pos_y_3 = 0 - racer_length

racer_car_pos_y_4 = 0 - racer_length

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

# Highscore Function
def load_high_score(score):
        
    """
    
    This function will test to see if a highscore
    file exists and then create one if one does not
    if one does exist it just uses the existing one
    then it'll write the score in the file and update
    if the score is greater than the one stored already
    
    """

    try:
      hi_score_file = open("Highscore.txt", "r")
    except:
      hi_score_file = open("Highscore.txt", "w")
      hi_score_file.write("0")
    hi_score_file = open("Highscore.txt", "r")
    value = hi_score_file.read()

    if score > int(value):
      hi_score_file = open("Highscore.txt", "w")
      hi_score_file.write(str(score))
      value = score
    
    hi_score_file.close()
    return value

# Message / Text Display Function
def display_text(msg, txt_colour, bkgd_colour, is_score, is_highscore):
    
    """
    
    This function displays a text onto the screen for
    the user to read, this includes score, highscore
    and death messages
    
    Scope includes: the message being displayed
    the text colour
    the background colour
    bool if this display is for the score
    bool if this display is for the highscore
    
    """

    if is_score == True:
      txt = font.render(msg, True, txt_colour)
      text_box = txt.get_rect(center = ((screen_width / screen_width + 50), 
                                        (screen_height / screen_height + 25)))


    elif is_highscore == True:
      txt = font.render(msg, True, txt_colour)
      text_box = txt.get_rect(center = ((screen_width - 100), 
                                        (screen_height / screen_height + 25)))

    
    else:
      txt = font.render(msg, True, txt_colour, bkgd_colour)
      text_box = txt.get_rect(center = ((screen_width / 2), 
                                        (screen_height / 2)))
    

    screen.blit(txt, text_box)

# Racer Creation
def racer_creation(x_pos, y_pos):
   
   """
   
   Racer Creation takes the x_pos and y_pos of the enemy racer
   and uses racer_width and racer_length already in the function
   this then will return the racer so that it appears on screen
   
   """
   
   racer = pygame.Rect(x_pos, y_pos, racer_width, racer_length)
   return racer

# Racer Moving Car Image
def racer_image(racer, image):
    
    """
    
    Racer image takes the enemy racer's location
    and takes the car image wanted to replace it
    and creates the image of a car being raced against
    
    """
    
    racer_car_image = pygame.image.load(image).convert_alpha()
    resized_racer = pygame.transform.smoothscale(racer_car_image, [racer_width, racer_length])
    screen.blit(resized_racer, racer)
    
# Enemy Racer movement and randomizing speed after resetting posistion
def enemy_racer_movement(racer_y, speed, score):
    
    """
    
    Enemy Racer movement grabs racer_y posistion to return the car to start 
    posistion for when it reaches the end of the road
    then grabs speed value which gets randomized for a different speed
    then grabs score to add to the score
    
    """
    if racer_y >= screen_height:
       racer_y = 0 - racer_length
       speed = randomizer()
       score += 1
    return racer_y, speed, score

# Collision Detection and Game Over
def collision_detection(racer_x, racer_y, game_over):
    if car_pos_x + car_width >= racer_x and car_pos_x <= racer_x + racer_width and car_pos_y + car_length >= racer_y and car_pos_y <= racer_y + racer_length:
       print("Death")
       game_over = True
    return game_over
    
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
    player_car = pygame.Rect(car_pos_x, car_pos_y, car_width, car_length)
    player_car_image = pygame.image.load("images/car_1.png").convert_alpha()
    resized_car = pygame.transform.smoothscale(player_car_image, [car_width, car_length])
    screen.blit(resized_car, player_car)

    # Player Movement and Limiter Controller
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit_game = True
        
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and move_right == True:
          car_change_x = 5   
                     
        elif event.key == pygame.K_LEFT and move_left == True:
          car_change_x = -5
            
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
          car_change_x = 0
          
        if car_pos_x <= road_pos_x:
           move_left = False
           
        if car_pos_x + car_width >= road_pos_x + road_width:
           move_right = False
    
    # Moves car depending on what key is pressed
    car_pos_x += car_change_x
    
    # Player Movement Limiter
    if car_pos_x <= road_pos_x:
       move_left = False
       car_change_x = 0
       
    elif car_pos_x + car_width >= road_pos_x + road_width:
       move_right = False
       car_change_x = 0
    
    else:
       move_left = True
       move_right = True
       
    
    # Other Racers Model
    racer_1 = racer_creation(racer_car_1_pos_x, racer_car_pos_y_1)
    racer_2 = racer_creation(racer_car_2_pos_x, racer_car_pos_y_2)
    racer_3 = racer_creation(racer_car_3_pos_x, racer_car_pos_y_3)
    racer_4 = racer_creation(racer_car_4_pos_x, racer_car_pos_y_4)
    
    # Enemy Racers Car Image Change
    racer_1_image = racer_image(racer_1, "images/car_2.png")
    racer_2_image = racer_image(racer_2, "images/car_3.png")
    racer_3_image = racer_image(racer_3, "images/car_4.png")
    racer_4_image = racer_image(racer_4, "images/car_5.png")
    
    # Enemy Racers Movement
    racer_car_pos_y_1, speed_1, score = enemy_racer_movement(racer_car_pos_y_1, speed_1, score)
    racer_car_pos_y_2, speed_2, score = enemy_racer_movement(racer_car_pos_y_2, speed_2, score)
    racer_car_pos_y_3, speed_3, score = enemy_racer_movement(racer_car_pos_y_3, speed_3, score)
    racer_car_pos_y_4, speed_4, score = enemy_racer_movement(racer_car_pos_y_4, speed_4, score)

    # Random Speed for movement
    racer_car_pos_y_1 += speed_1
    racer_car_pos_y_2 += speed_2
    racer_car_pos_y_3 += speed_3
    racer_car_pos_y_4 += speed_4

    # Collision Detection  
    game_over = collision_detection(racer_car_1_pos_x, racer_car_pos_y_1, game_over)
    game_over = collision_detection(racer_car_2_pos_x, racer_car_pos_y_2, game_over)
    game_over = collision_detection(racer_car_3_pos_x, racer_car_pos_y_3, game_over)
    game_over = collision_detection(racer_car_4_pos_x, racer_car_pos_y_4, game_over)
       
    # Score
    display_text("Score: {}".format(score), colours["black"], None, True, False)

    # Highscore
    highscore = load_high_score(score)
    display_text("Highscore: {}".format(highscore), colours["black"], None, False, True)
    
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
      print("Racer 2 ", racer_2)
      print("Racer 3 ", racer_3)
      print("Racer 4 ", racer_4)
      
      # Racer Car Locations within lanes
      print("\n *** Race Car Between Lane Locations ***")
      print("Racer 1 Lane Location ", ((racer_width / 2) + racer_car_1_pos_x) - road_pos_x)
      print("Racer 2 Lane Location ", ((racer_width / 2) + racer_car_2_pos_x) - (lane_pos_x_1 + lane_width))      
      print("Racer 3 Lane Location ", ((racer_width / 2) + racer_car_3_pos_x) - (lane_pos_x_2 + lane_width))      
      print("Racer 4 Lane Location ", ((racer_width / 2) + racer_car_4_pos_x) - (lane_pos_x_3 + lane_width))      

      # Stops the console from being overloaded with information
      debug = False


    # Pygame Display Update
    pygame.display.update()

    # FPS
    clock.tick(40)


# Game Over
print("Game Quit")