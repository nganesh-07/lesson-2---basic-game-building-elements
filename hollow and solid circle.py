import pygame

pygame.init()

# create display surface object with its dimensions
window = pygame.display.set_mode((300, 400))

# fill screen with a color
window.fill((255, 255, 255))

# define colors
green = (0, 255, 0)

# draw a SOLID circle
pygame.draw.circle(window, green, (100, 300), 20)

# draw a HOLLOW circle
pygame.draw.circle(window, green, (200, 200), 20, 3)

# display surface object on screen
pygame.display.update()

# loop the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# quit pygame
pygame.quit()