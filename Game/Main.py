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

# Create Warrior Class with random attackPoint and defensePoint
class Warrior():
    def __init__(self, x, y, img, name, max_hp, attack, defence, exp, rank):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = random.randint(5,20)
        self.defence = random.randint(1,10)
        self.alive = True
        self.image = img
        self.exp = exp
        self.rank = rank
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Create Tanker Class with random attackPoint and defensePoint
class Tanker():
    def __init__(self, x, y, img, name, max_hp, attack, defence, exp, rank):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = random.randint(1,10)
        self.defence = random.randint(5,20)
        self.alive = True
        self.image = img
        self.exp = exp
        self.rank = rank
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)    
  
    def draw(self):
        screen.blit(self.image, self.rect)
       

#Warrior Unit Generator
def genWarrior(nameOfUnit):
    unit = Warrior(400, 260, 0, nameOfUnit, 100, 0, 0, 0, 1 )
    return unit

#Tanker Unit Generator
def genTanker(nameOfUnit):
    unit = Tanker(1100, 260, 0, nameOfUnit, 100, 0, 0, 0, 1 )
    return unit

#List of Units
unitList = []

#Loop for Unit Generation
while (len(unitList) < 3):
    print('Type W for warrior or T for tanker')
    typeOfUnit = input('Select your unit type: ').upper()

    if typeOfUnit == 'W':
        warrior_name = input('Enter Unit name: ')
        warriorman = genWarrior(warrior_name)
        unitList.append(warriorman)

    elif typeOfUnit == 'T':
        tanker_name = input('Enter Unit name: ')
        tankerman = genTanker(tanker_name)
        unitList.append(tankerman)
    
    else:
        print ('Don\'t be lame, choose only W or T leh...')

#Unit Generation Preview
for nameOfUnit in range(len(unitList)):
    print('\nName: ', unitList[nameOfUnit].name, 'HP: ', unitList[nameOfUnit].hp, 'Attack: ', unitList[nameOfUnit].attack)
    print('Defence: ', unitList[nameOfUnit].defence, 'EXP: ', unitList[nameOfUnit].exp, 'Rank: ', unitList[nameOfUnit].rank)

#List of AI Units
aiList = []

while (len(aiList) < 3):
    aiName = 'AI' + str(random.randint(0,9)) + str(random.randint(0,9))
    aiGen = random.choice (['W','T'])

    if aiGen == 'W':
        aiWarrior = genWarrior(aiName)
        aiList.append(aiWarrior)

    elif aiGen == 'T':
        aiTanker = genTanker(aiName)
        aiList.append(aiTanker)


for nameOfaiUnit in range (len(aiList)):
    print('\nName: ', aiList[nameOfaiUnit].name, 'HP: ', aiList[nameOfaiUnit].hp, 'Attack: ', aiList[nameOfaiUnit].attack)
    print('Defence: ', aiList[nameOfaiUnit].defence, 'EXP: ', aiList[nameOfaiUnit].exp, 'Rank: ', aiList[nameOfaiUnit].rank)


#To Keep window up 
def main():
    
    run = True 
    while run:
        fpslock()
        loadimages()
        
        #draw Warrior
        playerwar.draw()
        
        #draw Tanker
        playertank.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
  main()
