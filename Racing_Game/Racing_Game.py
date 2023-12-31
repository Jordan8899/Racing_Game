# Imports
import pygame, sys
import random, time
from pygame import mixer

#  ************************* Constants *************************

 
# Pygame Initilisation so that pygame works through the code
pygame.init()

# Audio Mixer allow background music to be in the game
mixer.init()

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

# Set screen display window
screen = pygame.display.set_mode((screen_width, screen_height))

# Music Audio File Load into program
# Music created by ComaStudio
# Copyright Free given by Pixabay
back_track = "music/stylish_rock_beat.mp3"

# Crash Audio made and supplied Royalty Free by Pixabay
crash_audio = "music/crash.mp3"

# Music Volume Set
mixer.music.set_volume(0.2)

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

# Player Car Starting Location and all car sizes
car_width = 60
car_length = 100

car_pos_x = screen_width / 2 - (car_width / 2)
car_pos_y = screen_height - 200

car_change_x = 0

# Player Movement Limiter allowing player to move left and right
move_left = True
move_right = True

# Game Icon and Name makes sure icon file is readable
game_name = pygame.display.set_caption("Racing Game")

try:
    game_icon = pygame.image.load("images/game_icon.png")
    pygame.display.set_icon(game_icon)
    
except:
   print("Game Icon Image not found")

# Fonts and font size
try:
    font = pygame.font.Font("freesansbold.ttf", 25)

except:
    print("\nFont not found")

# Clock used for FPS
clock = pygame.time.Clock()

# Enemy Racer Car X Posistions
racer_x_1 = (lane_pos_x_1 - road_pos_x) / 2 + road_pos_x - (car_width / 2)
racer_x_2 = racer_x_1 + 102.5
racer_x_3 = racer_x_1 + 205
racer_x_4 = racer_x_1 + 307.5

# Enemy Racer Y Starting Posistions
racer_y_1 = 0 - car_length
racer_y_2 = 0 - car_length
racer_y_3 = 0 - car_length
racer_y_4 = 0 - car_length

# Speed Randomizer for Enemy Racers
speed_list = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Warm up Speed (Starting Speed)
speed_1 = 3
speed_2 = 7
speed_3 = 2 
speed_4 = 5

# Debug Variable for Statistics on game piece locations
# Music sends an error message if file is not located
# but plays music if file is located
debug = True
music = True

# Game Over Variable to allow game to quit
game_over = False

# Play Again is so that the game can repeat even after crashing
play_again = True

# Crash for collision detection and allowing game to play again
crash = False

# Starting Score
score = 0


# ************************* Functions *************************


# Randomizer Function
def randomizer():
    """
    
    This function will use speed_list to get access to all available 
    speeds and randomly select one each time this function is called
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
    
    try:
        if is_score:
          txt = font.render(msg, True, txt_colour)
          text_box = txt.get_rect(center = ((screen_width / screen_width + 50), 
                            (screen_height / screen_height + 25)))


        elif is_highscore:
          txt = font.render(msg, True, txt_colour)
          text_box = txt.get_rect(center = ((screen_width - 100), 
                             (screen_height / screen_height + 25)))

    
        else:
          txt = font.render(msg, True, txt_colour, bkgd_colour)
          text_box = txt.get_rect(center = ((screen_width / 2), 
                                            (screen_height / 2)))
    

        screen.blit(txt, text_box)
    
    except:
        print("Font not found")


# Racer Creation
def racer_creation(x_pos, y_pos):
   
   """
   
   Racer Creation takes the x_pos and y_pos of the enemy racer
   and uses car_width and car_length already in the function
   this then will return the racer so that it appears on screen
   
   """
   
   racer = pygame.Rect(x_pos, y_pos, car_width, car_length)
   
   return racer


# Racer Moving Car Image
def racer_image(racer, image):
    
    """
    
    Racer image takes the enemy racer's location
    and takes the car image wanted to replace it
    and creates the image of a car being raced against
    
    """
    try:
        racer_car_image = pygame.image.load(image).convert_alpha()
        resized_racer = pygame.transform.smoothscale(racer_car_image, 
                                                 [car_width, car_length])
    
        screen.blit(resized_racer, racer)
    
    except:
       while True:
            screen.fill(colours["black"])
            display_text("Error Image Files not found", colours["white"], 
                         None, False, False)
            print("\n *** Car Images Not Found *** \n")
       
    
# Enemy Racer movement and randomizing speed after resetting posistion
def racer_movement(racer_y, speed, score):
    
    """
    
    Enemy Racer movement grabs racer_y posistion to return the car 
    to start posistion for when it reaches the end of the road
    then grabs speed value which gets randomized for a different speed
    then grabs score to add to the score
    
    """
    
    if racer_y >= screen_height:
       racer_y = 0 - car_length
       speed = randomizer()
       score += 1
       
    return racer_y, speed, score


# Collision Detection and Game Over
def collision_detection(racer_x, racer_y, crash):
    
    """

    Collision Detection (x posistion), y posistion, crash (bool))
    required for area collision
    
    """

    if (car_pos_x + car_width >= racer_x and car_pos_x <= racer_x 
        + car_width and car_pos_y + car_length 
        >= racer_y and car_pos_y <= racer_y + car_length):
       
        # Background Music Stops            
        mixer.music.pause()
        
        # Crash Audio plays unless file cannot be found
        # Stops an error from occuring if file is not found
        try:
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(crash_audio))
            time.sleep(1.5)
        
        except:
            print("\n*** Crash Audio File not found ***")
                
        print("\nDeath")
        crash = True
        
    return crash
           
# ************************* Main Routine *************************

# How to play the game
screen.fill(colours["black"])

display_text("Left and Right Arrow Keys to move, don't crash", 
             colours["white"], None, False, False)

pygame.display.update()

# Timer Sleep so that people have time to read instructions
time.sleep(5)

# Play Again Loop
while not game_over:
    
    # Music Plays unless file is not located
    if music:
        try:
            pygame.mixer.Channel(0).play(pygame.mixer.Sound(back_track))
        
        except:
            # Prints into console one time
            # shows music file not located top of console
            print("\n***** Music file not located *****\n")
            music = False

    # Actual Game Loop
    while play_again:    
        
        # Background Colour (Either side of road)
        screen.fill(colours["dark_green"])
    
        # Road Creation
        road = pygame.draw.rect(screen, colours["gray"], 
                                [road_pos_x, road_pos_y, 
                                 road_width, road_length])
        
    
        # Lanes Creation
        lane_1 = pygame.draw.rect(screen, colours["white"], 
                                [lane_pos_x_1, lane_pos_y, 
                                 lane_width, lane_length])
        
        lane_2 = pygame.draw.rect(screen, colours["white"], 
                                [lane_pos_x_2, lane_pos_y, 
                                 lane_width, lane_length])
        
        lane_3 = pygame.draw.rect(screen, colours["white"], 
                                [lane_pos_x_3, lane_pos_y, 
                                 lane_width, lane_length])    
    
    
        # Player Car Model (pl stands for player)
        pl_car = racer_creation(car_pos_x, car_pos_y)
        pl_car_image = racer_image(pl_car, "images/car_1.png")

        # Player Movement and Limiter Controller
        for event in pygame.event.get():
          
            if event.type == pygame.QUIT:
                quit_game = True
                sys.exit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and move_right:
                    car_change_x = 5   
                     
                elif event.key == pygame.K_LEFT and move_left:
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
        racer_1 = racer_creation(racer_x_1, racer_y_1)
        racer_2 = racer_creation(racer_x_2, racer_y_2)
        racer_3 = racer_creation(racer_x_3, racer_y_3)
        racer_4 = racer_creation(racer_x_4, racer_y_4)
    
        # Enemy Racers Car Image Change
        racer_1_image = racer_image(racer_1, "images/car_2.png")
        racer_2_image = racer_image(racer_2, "images/car_3.png")
        racer_3_image = racer_image(racer_3, "images/car_4.png")
        racer_4_image = racer_image(racer_4, "images/car_5.png")
    
        # Enemy Racers Movement
        racer_y_1, speed_1, score = racer_movement(racer_y_1, speed_1, score)
        racer_y_2, speed_2, score = racer_movement(racer_y_2, speed_2, score)
        racer_y_3, speed_3, score = racer_movement(racer_y_3, speed_3, score)
        racer_y_4, speed_4, score = racer_movement(racer_y_4, speed_4, score)

        # Random Speed for movement
        racer_y_1 += speed_1
        racer_y_2 += speed_2
        racer_y_3 += speed_3
        racer_y_4 += speed_4

        # Collision Detection  
        crash = collision_detection(racer_x_1, racer_y_1, crash)
        crash = collision_detection(racer_x_2, racer_y_2, crash)
        crash = collision_detection(racer_x_3, racer_y_3, crash)
        crash = collision_detection(racer_x_4, racer_y_4, crash)
       
        # Score
        display_text("Score: {}".format(score), colours["black"], 
                     None, True, False)

        # Highscore
        highscore = load_high_score(score)
        display_text("Highscore: {}".format(highscore), colours["black"], 
                     None, False, True)
    
        # Debug
        if debug:
          # Lane Locations
          print("\n*** Lane Strip Locations ***")
          print("Lane 1 ", lane_1)
          print("Lane 2 ", lane_2)
          print("Lane 3 ", lane_3)
      
          # Car Lane Lengths
          print("\n*** Car Lane Lengths ***")
          
          print("Car Lane Length 1 ", lane_pos_x_1 - road_pos_x)
          
          print("Car Lane Length 2 ", lane_pos_x_2 - (lane_pos_x_1 
                                                      + lane_width))
          
          print("Car Lane Length 3 ", lane_pos_x_3 - (lane_pos_x_2 
                                                      + lane_width))
          
          print("Car Lane Length 4 ", (road_width + road_pos_x 
                                       - (lane_pos_x_3 + lane_width)))
      
          # Player Car and Opposistion Locations
          print("\n*** Player and other Car Locations ***")
          print("Player Car ", pl_car)
          print("Racer 1 ", racer_1)
          print("Racer 2 ", racer_2)
          print("Racer 3 ", racer_3)
          print("Racer 4 ", racer_4)
      
          # Racer Car Locations within lanes
          print("\n *** Race Car Between Lane Locations ***")
          
          print("Racer 1 Lane Location ", (((car_width / 2) 
                                            + racer_x_1) - road_pos_x))
          
          print("Racer 2 Lane Location ", (((car_width / 2) + racer_x_2) 
                                           - (lane_pos_x_1 + lane_width)))
          
          print("Racer 3 Lane Location ", (((car_width / 2) + racer_x_3) 
                                           - (lane_pos_x_2 + lane_width)))
          
          
          print("Racer 4 Lane Location ", (((car_width / 2) + racer_x_4) 
                                           - (lane_pos_x_3 + lane_width)))
          

          # Stops the console from being overloaded with information
          debug = False

        # Player Death / Car Crash
        if crash:
            # Game loop stops until user decides to play again or not
            play_again = False

        # Pygame Display Update
        pygame.display.update()
    
        # FPS
        clock.tick(40)
    
    
    # ************************* Play Again *************************
    screen.fill(colours["dark_green"])
    display_text("Press R to Play Again and Q to Quit Score: {}".format(score), 
                 colours["black"], colours["dark_green"], False, False)
    
    pygame.display.update()
    
    for event in pygame.event.get():
       
        if event.type == pygame.KEYDOWN:
          
            # Play Game Again
            if event.key == pygame.K_r:
                print("Play Again")
            
                # Game Reset Function resets car posistions
                score = 0
                racer_y_1 = 0 - car_length
                racer_y_2 = 0 - car_length
                racer_y_3 = 0 - car_length
                racer_y_4 = 0 - car_length
                
                speed_1 = 3
                speed_2 = 7
                speed_3 = 2
                speed_4 = 5
                
                car_change_x = 0         
                car_pos_x = screen_width / 2 - (car_width / 2)
    
                play_again = True
                crash = False
            
            # Game Quits
            elif event.key == pygame.K_q:
                print("\nQuit Game")
                game_over = True

# ************************* Game Over *************************
pygame.quit()
print("\nGame Quit")