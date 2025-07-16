import pygame

# define a function for all these basic precursor things so u can access later in program (bc it's a large program)

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("color changing sprite")

    colors = {
        "red": pygame.Color("red"),
        "green": pygame.Color("green"),
        "blue": pygame.Color("blue"),
        "yellow": pygame.Color("yellow"),
        "white": pygame.Color("white")
    }
    current = colors["white"]

    # set starting position on board and sprite size
    x, y = 30, 30
    sprite_width, sprite_height = 60, 60
    
    # just smth to do usually w games like this
    clock = pygame.time.Clock()
    
    # standard for letting game know when user is done
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        # to identify which keys were pressed
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x = -3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3

        # readjusting position on board
        x = min(max(0,x), screen_width - sprite_width)
        y = min(max(0,y), screen_height - sprite_height)

        # change color based on boundary contacted
        if x == 0: current = colors["blue"]
        elif x == screen_width - sprite_width: current = colors["yellow"]
        elif y == 0: current = colors["red"]
        elif y == screen_height - sprite_height: 
            current = colors["green"]
        else:
            current = colors["white"]
        
        # filling screen color
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current, (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)
    
    pygame.quit()

if __name__ == "__main__":
    main()