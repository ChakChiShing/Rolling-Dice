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
player_money = 1000
money_font = pygame.font.SysFont(None,40)
money_text = money_font.render('Your money $' + str(player_money), True, (0,0,0))
window_surface.blit(money_text, (10, 550))

roll_button = pygame.font.SysFont(None, 50)
button = roll_button.render('Roll', True, ((255,255,255)))

pic_index = 0
width = window_surface.get_width()
height = window_surface.get_height()

dice_image = [pygame.image.load(r'C:\Users\user\Desktop\rolling dice\dice1.png'),pygame.image.load(r'C:\Users\user\Desktop\rolling dice\dice2.png'),pygame.image.load(r'C:\Users\user\Desktop\rolling dice\dice3.png'),pygame.image.load(r'C:\Users\user\Desktop\rolling dice\dice4.png'),pygame.image.load(r'C:\Users\user\Desktop\rolling dice\dice5.png'),pygame.image.load(r'C:\Users\user\Desktop\rolling dice\dice6.png')]

while True:
   
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+80:
                pic_index = random.randint(1,6)
                print(pic_index)

    mouse = pygame.mouse.get_pos()
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+80:
        pygame.draw.rect(window_surface,(170,170,170),[width/2-20, 330, 70, 40])
    else:
        pygame.draw.rect(window_surface,(100,100,100), [width/2-20, 330, 70, 40])
    
    window_surface.blit(dice_image[1], (300, 50))
    window_surface.blit(button,(width/2-20,height/2+30))

    if (player_money==0):
        print
        break
    pygame.display.update()

# flag = True
# money = 1000
# bid = input("Amount to bid:")
# if (bid <=0 or bid >money):
#     print("Invalid Input!")

# while (flag):
#     play = input("Please enter 1 to keep rolling dice, 0 to exit the game\n")
#     if (int(play)!=1):
#         print("Invalid input!")
#         input("Please enter 1 to keep rolling dice, 0 to exit the game\n")
#     elif (int(play) == 0):
#         flag = False

   
