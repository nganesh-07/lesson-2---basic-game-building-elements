import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("my first game screen.")

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (0, 255, 255), pygame.Rect(70, 80, 100, 100))

    pygame.display.flip()