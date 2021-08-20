import pygame 

pygame.init()




#window
screenwidth = 875
screenheight = 500

screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Battle ")

#store images
#background image
bgimage= pygame.image.load("img/bg.png").convert_alpha()


#Load images
def drawbg():
    screen.blit(bgimage, (0,0))

#prevent lag on slower computers
def fpslock(fps):
    clock =pygame.time.Clock()
    fps = 60 
    clock.tick(fps)

#To Keep window up 
def main():
    
    run = True 
    while run:
        fpslock()
        drawbg()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
  main()