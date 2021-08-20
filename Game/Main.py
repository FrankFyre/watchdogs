import pygame 
import random 
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
    
#Attack for Warrior
attack = random.randint(5, 20)

#Warrior class
class Warrior():
    def __init__(self, x, y, name, max_hp, attack, potions)
    self.name = name 
    self.max_hp = max_hp 
    self.hp = max_hp
    self.attack = attack
    self.start_potions = potions
    self.potions = potions 
    self.alive = True 
    self.image = pygame.image.load() #Load image of Warrior
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    
  
def draw(self):
    screen.blit(self.image, self.rect)
    
knight = Warrior(200,260, 'Warrior', 100, attack)


#To Keep window up 
def main():
    
    run = True 
    while run:
        fpslock()
        drawbg()
        
        #draw Warrior
        knight.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
  main()
