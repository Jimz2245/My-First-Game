import pygame
from sys import exit

pygame.init() #starts pygame and initiates all sub-parts, must be put before any other pygame command, opposite to pygame.quit()
screen = pygame.display.set_mode((800,400)) #creates the screen with ((width, height))
pygame.display.set_caption("My First Game") #names game screen tab
clock = pygame.time.Clock() #creates a clock to establish time in the game
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)#creates font with (font_type, size)

test_surf = pygame.Surface((100,200)) #creates a surface with the width of 100px from the left and height of 200px from the top
sky_surf = pygame.image.load("graphics/Sky.png").convert() #converts to file pygame can work with more easily
ground_surf = pygame.image.load("graphics/Ground.png").convert()
test_surf.fill("Blue")#makes test_surface blue

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha() #converts image to pygame friendly file while also removing alpha values (black and white behind pic)
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf =pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
#pygame.Rect() creates a rectangle with (left, top, width, height)
player_rect = player_surf.get_rect(midbottom = (80,300)) #takes a surface and draws a rectangle around it which you can then use its points and sides to position it anywhere

score_surf = test_font.render("Score", False, (64,64,64)) #text you want to display, anti-alias(smooth the edges of the text), color), make the text surface
score_rect = score_surf.get_rect(center = (400, 50))

while(True): 
    #always true so the game will continue to run until it breaks the loop from the inside
    #draw all our elements
    #update everything
    for event in pygame.event.get(): #loops through all possible events
        if event.type == pygame.QUIT:
            pygame.quit()#stops the game, opposite to pygame.init()
            exit()#stops error caused by quitting python while while(True) is still running and trying to run pygame.display.update
        #if event.type == pygame.MOUSEMOTION: #gives us mouse position when moving the mouse
        #    print(event.pos) #returns the position of the mouse
        #if event.type == pygame.MOUSEBUTTONUP: returns if the mouse button is released from being pressed down
        #    print("mouse up")
        #if event.type == pygame.MOUSEBUTTONDOWN: returns if the mouse button is pressed down
        #    print("mouse down")
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos): #checks if the mouse is over the player rectangle
                print("collision")
    screen.blit(sky_surf, (0,0))#puts one surface onto another (surface, position) #(0,0) for pygame is at the top left, not the middle or bottom left
    screen.blit(ground_surf, (0, 300))#would go in front the sky image as it is made after
    pygame.draw.rect(screen, "#c0e8ec", score_rect) #pygame.draw tells pygame you're drawing, rect(what you're drawing on, color, what you're drawing,optional: radius) tells it to draw a rectangle
    #pygame.draw.line(screen, "gold", (0,0), (800,400), 10) draws a line on the screen from (0,0) to (800, 400) that is gold and has a thickness of 10
    pygame.draw.ellipse(screen, "brown", pygame.Rect(50, 200, 100, 100)) #(where to draw, color, bounding box #Rect(length from left, length from top, width, height)

    screen.blit(score_surf, score_rect)

    snail_rect.x -= 4 #changes the snail's x position by 4
    if snail_rect.right <= 0:
        snail_rect.left = 800 #takes the snail back to the right side when it reaches too far left
    screen.blit(snail_surf,snail_rect)
    player_rect.left += 1
    screen.blit(player_surf, player_rect)

    #if player_rect.colliderect(snail_rect): #returns 0 w/o collision, returns 1 with collision 
    #    print("collision")

    #mouse_pos = pygame.mouse.get_pos() #gives the x and y position of the mouse
    #if player_rect.collidepoint(mouse_pos): #rect1.collidepoint(x,y) checks if a rectangle collides with a point ex. clicking a rect with your mouse
    #    print("collision")
    #    print(pygame.mouse.get_pressed()) #returns which mouse buttons are being pressed (L, M, R)


    pygame.display.update() #updates the display/makes the new updated frames
    clock.tick(60)#the while loop should not run more than 60 times per second, (60 fps)

