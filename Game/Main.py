import pygame 
import random 
pygame.init()

# testing

#window
screenwidth = 1475
screenheight = 500

screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Darren's Breakdown ")

#define game variables
    current_warrior = 3
    total_warriors = 6
    action_cooldown = 0
    action_wait_time = 90
    attack = False
    potion = False
    clicked = False

#define fonts - ALLEN
font = pygame.font.SysFont('Times New Roman', 26)

# define colors - ALLEN
red = (255, 0, 0)
green = (0, 255, 0)

#create function for drawing text - ALLEN
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#function for drawing panels - ALLEN
def draw_panel():
    screen.blit(sideimage, (1175,0))
    screen.blit(sideimage, (0,0))
    #NEED PROPER UNIT LIST IN ORDER TO REPRESENT EACH UNIT'S NAME AND HEALTH
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

    def update(self):
        animation_cooldown = 100
        #update image
        self.image = self.animation_list[self.action][self.frame_index]
        #check time since update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #rest if anim runs out of time
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def idle(self):
        #set var to attack animation
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def attack(self, enemy):
        #deal damage to enemy
        random = random.randint(5, 20)
        damage = self.strength + rand
        enemy.hp -= damage
        #check if enemy has died
        if enemy.hp < 1:
            enemy.hp = 0
            enemy.alive = False
        #set var to attack animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()        
        
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
        
        #player actions//reset action var
        attack = False
        potion = False
        target = None
        #cursor is visible
        pygame.mouse.set_visible(True)
        pos = pygame.mouse.get_pos()
        for count, enemy in enumerate(enemy_list)
            if enemy.rect.collidepoint(pos):
                #click to attack 
                if clicked == True
                    attack = True
                    target = enemy_list[count]

        #player's move 
        if warrior.alive == True:
        if current_warrior == 3:
            action_cooldown += 1
            if action_cooldown >= action_wait_time:
                #attack
                if attack == True and target != None:
                    warrior.attack(target)
                    current_warrior += 3
                    action_cooldown = 0

        #enemy action
        for count, enemy in enumerate(enemy_list):
            if current_warrior == 3 + count
                if enemy.alive  == True:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        #attack
                        enemy.attack(warrior1)
                        current_warrior += 1
                        action_cooldown = 0
                else:
                    current_warrior += 1

        #warriors make a turn then reset
        if current_warrior > total_warriors:
            current_warrior = 3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
  main()
