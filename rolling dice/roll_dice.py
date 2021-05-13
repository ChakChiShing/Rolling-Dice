import sys
import random
import pygame
from pygame.locals import QUIT

# initialize a game
pygame.init()
# set the length and width of display window
window_surface = pygame.display.set_mode((800, 600))
# set the titile of the window
pygame.display.set_caption('Rolling Dice')
# set the background color 
window_surface.fill((50, 168, 82))

#load dice icon
# image = pygame.image.load(r'C:\Users\user\Desktop\rolling dice\dice.png')
# window_surface.blit(image, (320, 50))

# title of the game
head_font = pygame.font.SysFont(None, 60)
text_surface = head_font.render('Casino', True, (0,0,0))
window_surface.blit(text_surface, (350,10))

#display player`s current value
global player_point
player_point = 0
money_font = pygame.font.SysFont(None,40)
money_text = money_font.render('Your point $' + str(player_point), True, (0,0,0))


#render big text
big_font = pygame.font.SysFont(None,40)
big_text = big_font.render('Big',True, (255,255,255))

#render small text
small_font = pygame.font.SysFont(None,40)
small_text = small_font.render('Small',True, (255,255,255))

#roll text button
roll_button = pygame.font.SysFont(None, 50)
button = roll_button.render('Roll', True, ((255,255,255)))

# to store the rand int output
pic_index = 0
#get width and height of the screen
# later use in setting mouse click checking
width = window_surface.get_width()
height = window_surface.get_height()

# a list to storet the image
dice_image = [pygame.image.load(r'C:\Users\user\Desktop\rolling dice\dice1.png'),pygame.image.load(r'C:\Users\user\Desktop\rolling dice\dice2.png'),pygame.image.load(r'C:\Users\user\Desktop\rolling dice\dice3.png'),pygame.image.load(r'C:\Users\user\Desktop\rolling dice\dice4.png'),pygame.image.load(r'C:\Users\user\Desktop\rolling dice\dice5.png'),pygame.image.load(r'C:\Users\user\Desktop\rolling dice\dice6.png')]

biding_choice = []
setSmall = False
setBig = False
flag = False
while True:
    for event in pygame.event.get():
        flag = False
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+80:
                pic_index = random.randint(1,6)
                print("the pic_index is : " ,pic_index)
                for i in biding_choice:
                    if (int(i)==pic_index):
                        flag = True
                        player_point = player_point + 1
                        print("i bid correctly" , player_point)

                if(flag == False):
                    player_point = player_point - 1

                print(player_point)
                set = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if (150<= mouse[0] <= 250) and (450 <= mouse[1] <= 490):
                biding_choice = [1, 2, 3]
                setSmall = True
                setBig = False
            elif (600<= mouse[0] <= 700) and (450 <= mouse[1] <= 490):
                biding_choice = [4, 5, 6]
                setBig = True
                setSmall =False

    # get the position of mouse
    mouse = pygame.mouse.get_pos()

    # clickable roll text button
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+80:
        pygame.draw.rect(window_surface,(170,170,170),[width/2-20, 330, 70, 40])
    else:
        pygame.draw.rect(window_surface,(100,100,100), [width/2-20, 330, 70, 40])
    
    # dynamically change the dice image
    pygame.draw.rect(window_surface, (50, 168, 82), (300, 50, 255, 255))
    window_surface.blit(dice_image[pic_index-1], (300, 50))
    # position of button 
    window_surface.blit(button,(width/2-20,height/2+30))

    # interact with small button
    if (150<= mouse[0] <= 250) and (450 <= mouse[1] <= 490):
        pygame.draw.rect(window_surface, (141, 207, 227), (150, 450, 100, 40))
    elif(setSmall):
        pygame.draw.rect(window_surface, (141, 227, 198), (150, 450, 100, 40))
    else:
        pygame.draw.rect(window_surface, (227, 147, 141), (150, 450, 100, 40))

    # interact with big button
    if (600<= mouse[0] <= 700) and (450 <= mouse[1] <= 490):
        pygame.draw.rect(window_surface, (141, 207, 227), (600, 450, 100, 40))
    elif(setBig):
        pygame.draw.rect(window_surface, (141, 227, 198), (600, 450, 100, 40))
    else:
        pygame.draw.rect(window_surface, (227, 147, 141), (600, 450, 100, 40))

    # display big and small text option
    window_surface.blit(big_text,(620,455))
    window_surface.blit(small_text,(165,455))
    # to refresh the screen
    pygame.draw.rect(window_surface, (50, 168, 82), (10, 550, 200, 40))
    # to print the point
    money_text = money_font.render('Your point $' + str(player_point), True, (0,0,0))
    window_surface.blit(money_text, (10, 550))

    pygame.display.update()
