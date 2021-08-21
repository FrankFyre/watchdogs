import pygame 
import random 
pygame.init()


#window
screenwidth = 1475
screenheight = 500

screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Darren's Breakdown ")

#store images
#background
bgimage= pygame.image.load("img/bg.png").convert_alpha()
sideimage= pygame.image.load("img/side1.png").convert_alpha()

#Units

playertankimg = pygame.image.load("img/tanker1.png").convert_alpha()
playerwarriorimg = pygame.image.load("img/warrior1.png").convert_alpha()

enemytankimg = pygame.image.load("img/tanker2.png").convert_alpha()
enemywarriorimg = pygame.image.load("img/warrior2.png").convert_alpha()

#Load images
def loadimages():
    screen.blit(bgimage, (300,0))
    screen.blit(sideimage, (0,0))
    screen.blit(sideimage, (1175,0))

#prevent lag on slower computers
def fpslock():
    FPS = 60 # frames per second setting
    fpsClock = pygame.time.Clock()
    fpsClock.tick(FPS)

#Attack for Warrior
attack = random.randint(5, 20)

#Warrior class
class Warrior():
    def __init__(self, x, y, img, name, max_hp, attack, potions):
        self.name = name 
        self.max_hp = max_hp 
        self.hp = max_hp
        self.attack = attack
        self.start_potions = potions
        self.potions = potions 
        self.alive = True 
        self.image = img 
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
  
    def draw(self):
        screen.blit(self.image, self.rect)



knight = Warrior(200,260,playertankimg, 0 , 10, 10, 10 )



#To Keep window up 
def main():
    
    run = True 
    while run:
        fpslock()
        loadimages()
        
        #draw Warrior
        knight.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
  main()
