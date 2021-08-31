import pygame
import random
import logging
pygame.init()
pygame.font.init()

# Log settings/formatting
logging.basicConfig(filename='Proglog.log',level=logging.INFO, format='%(asctime)s :: %(message)s', filemode='w')

#window
screenwidth = 1475
screenheight = 500

screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("Purgatory")



#define fonts - ALLEN
fontsize=24 #this is so that defdrawtext can use be space via font size
font= pygame.font.Font('Romanica.ttf', fontsize) 

# define colors - ALLEN
red    = (255,   0, 0)
green  = (  0, 255, 0)
black  = (  0,   0, 0)

#create function for drawing text - ALLEN
# def draw_text(text, font, text_col, x, y):
#     img = font.render(text, True, text_col)
#     screen.blit(img, (x, y))

def DrawText (Name,type,atk,defence,exp,rank,maxhp,currenthp, x,y):
    info= font.render(str(Name)+" | "+str(type),True, black)
    info2=font.render("Atk: "+str(atk)+"| Def: "+str(defence), True, black)
    info3=font.render("Rank: "+ str(rank)+"| EXP: "+str(exp),True, black)
    info4=font.render("HP: "+str(currenthp)+"/"+str(maxhp), True, black)
    screen.blit(info,(x,y))
    screen.blit(info2,(x,y+fontsize+4)) 
    screen.blit(info3,(x,y+ 2*fontsize+8))
    screen.blit(info4,(x,y+3*fontsize+12))


#function for drawing panels - ALLEN
def draw_panel():
    screen.blit(sideimage, (1175,0))
    screen.blit(sideimage, (0,0))
    #NEED PROPER UNIT LIST IN ORDER TO REPRESENT EACH UNIT'S NAME AND HEALTH
#store images
#background
bgimage= pygame.image.load("img/bg.png").convert_alpha()
sideimage= pygame.image.load("img/side1.png").convert_alpha()
attackbuttonimage= pygame.image.load("img/attack.png").convert_alpha()
#Units

playertankimg = pygame.image.load("img/tanker1.png").convert_alpha()
playerwarriorimg = pygame.image.load("img/warrior1.png").convert_alpha()

enemyTankerimg = pygame.image.load("img/tanker2.png").convert_alpha()
enemyWarriorimg = pygame.image.load("img/warrior2.png").convert_alpha()

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


### Unit Class
class MasterUnit():
    def __init__(self, x, y, img, name, max_hp, attack, defence, exp, rank, typer):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defence = defence
        self.alive = True
        self.image = img
        self.exp = exp
        self.rank = rank
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.type=typer
 

    def sasageyo(self, targetdef, targethp):
        #deal damage to enemy
        damage = self.attack - targetdef+ random.randint(-5,10)
        if damage<=0:
            return 0
        else:
            return damage

        
        return damage
        targethp -= damage

        #check if enemy has died
        # if targethp < 1:
        #     targethp = 0
            #target.alive = False
        #set var to attack animation
        # self.action = 1 
        # self.frame_index = 0
        # self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, self.rect)


### Player Unit Generation

#Unit def from Class
def genplayerwarrior(x,y,name):
    unit = MasterUnit(x, y, playerwarriorimg, name, 100, random.randint(5,20), random.randint(1,10), 0, 1 ,("Warrior"))
    return unit

def genplayertanker(x,y,name):
    unit = MasterUnit(x, y, playertankimg, name, 100, random.randint(1,10), random.randint(5,15), 0, 1,("Tanker") )
    return unit

#Creation of Units and storing into lists
PlayerUnitList=[]

#empty list after testing so player can generate and DELETET THIS
unitprofession= [genplayertanker,genplayerwarrior,genplayertanker]
unitname=[("P1"), ("P2"), ("P3") ]

# #Loop for Unit Generation 

# while (len(unitprofession) < 3):
#     print('Type W for warrior or T for tanker')
#     selectedunitproffesion = input('Select your unit type: ').upper()

#     if selectedunitproffesion == 'W':
#         selectedname = input('Enter Unit name: ')
#         unitname.append(selectedname)
#         unitprofession.append(genplayerwarrior)

#     elif selectedunitproffesion == 'T':
#         selectedname = input('Enter Unit name: ')
#         unitname.append(selectedname)
#         unitprofession.append(genplayertanker)

#     else:
#         print ('Don\'t be lame, choose only W or T leh...')


Playerunit1 =unitprofession[0](380, 390, unitname[0] )
Playerunit2 =unitprofession[1](510, 350, unitname[1] )
Playerunit3 =unitprofession[2](640, 310, unitname[2] )


PlayerUnitList.append(Playerunit1)
PlayerUnitList.append(Playerunit2)
PlayerUnitList.append(Playerunit3)

#Code for testing in CMD
# #Unit Generation Preview
# for nameOfUnit in range(len(PlayerUnitList)):
#     print('\nName: ', PlayerUnitList[nameOfUnit].name, 'HP: ', PlayerUnitList[nameOfUnit].hp, 'Attack: ', PlayerUnitList[nameOfUnit].attack)
#     print('Defence: ', PlayerUnitList[nameOfUnit].defence, 'EXP: ', PlayerUnitList[nameOfUnit].exp, 'Rank: ', PlayerUnitList[nameOfUnit].rank)
#     print('Type: ', PlayerUnitList[nameOfUnit].type)


### Ai Generation and Drawing

#def to generate units from class
def AIGEenWar(x,y,name):
    unit = MasterUnit(x,y, enemyWarriorimg, name, 100, random.randint(5,20), random.randint(1,10), 0, 1 ,("Warrior"))
    return unit

def AIGenTank(x,y,name):
    unit = MasterUnit(x,y, enemyTankerimg, name, 100, random.randint(1,10), random.randint(5,15), 0, 1,("Tanker") )
    return unit

#Generate units and store in lists
AIList = []
typelist=[AIGEenWar,AIGenTank]


AIUnit1 =random.choice(typelist)(1080, 390,  'AI ' + str(random.randint(0,9)) + str(random.randint(0,9)))
AIUnit2 =random.choice(typelist)( 950, 350,  'AI ' + str(random.randint(0,9)) + str(random.randint(0,9)))
AIUnit3 =random.choice(typelist)( 820, 310,  'AI ' + str(random.randint(0,9)) + str(random.randint(0,9)))

AIList.append(AIUnit1)
AIList.append(AIUnit2)
AIList.append(AIUnit3)

#Early Test CMD
# for nameOfaiUnit in range (len(AIList)):
#     print('\nName: ', AIList[nameOfaiUnit].name, '\nHP: ', AIList[nameOfaiUnit].hp, '\nAttack: ', AIList[nameOfaiUnit].attack)
#     print('\nDefence: ', AIList[nameOfaiUnit].defence, '\nEXP: ', AIList[nameOfaiUnit].exp, '\nRank: ', AIList[nameOfaiUnit].rank)
#     print('Type: ', AIList[nameOfaiUnit].type)


#Draw Unit's Informations
def drawunit():
        constant=0 #constant is to seprate diff unit in Y axis
        #Player Units
        for x in PlayerUnitList:
            DrawText(x.name,x.type, x.attack,x.defence,x.exp, x.rank, x.hp,x.hp, 15,0+constant)
            constant=constant+150
        
        constant=0
        #AI Units
        for x in AIList:
            DrawText(x.name,x.type, x.attack,x.defence,x.exp, x.rank, x.hp,x.hp, 1190,0+constant)
            constant=constant+150



###Button Creation

#button class
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		screen.blit(self.image, (self.rect.x, self.rect.y))

		return action
    
#P/AI= player/AI, U=Unit, digit=designation

PU1 = Button( 200, 50, attackbuttonimage,1)
PU2 = Button( 200, 200, attackbuttonimage,1)
PU3 = Button( 200, 350, attackbuttonimage,1)



AIU1 = Button( 1370, 50, attackbuttonimage,1)
AIU2 = Button( 1370, 200, attackbuttonimage,1)
AIU3 = Button( 1370, 350, attackbuttonimage,1)




class fightingphase():
    def __init__(self, Attacker, Target, AttackerList, Targetlist):
        self.attacking=Attacker
        self.targeting=Target
        self.Attackinglist=AttackerList
        self.Targetinglist=Targetlist


    def battlecalculation(self):
        dam= self.Attackinglist[self.attacking].sasageyo(self.Targetinglist[self.targeting].defence, self.Targetinglist[self.targeting].hp)
        self.Targetinglist[self.targeting].hp=self.Targetinglist[self.targeting].hp  - dam
        self.Attackinglist[self.attacking].exp+=dam

        if dam >10:
            extra=1.2

        elif dam<=0:
            extra=1.5

        else:
            extra=1
        
        TargetEXPEarned=self.Targetinglist[self.targeting].defence*extra

        self.Targetinglist[self.targeting].exp+=TargetEXPEarned

        #Logging for player atk, dealt and enemy xp earned
        logging.info(self.Attackinglist[self.attacking].name+" attacked "+ self.Targetinglist[self.targeting].name )
        logging.info('Damage dealt: ' + str(dam))
        logging.info("Extra Bonus exp percentage decimal: "+ str(extra))
        logging.info('Target Exp Earned: '+ str(TargetEXPEarned))

        print("-------")
        print(self.Attackinglist[self.attacking].name+" attacked "+ self.Targetinglist[self.targeting].name )
        print("Damage dealt: ",dam)
        print("Extra Bonus exp percentage decimal: ",extra)
        print("Target Exp Earned: ",TargetEXPEarned)
        print("-------")
        x=1
        

        


total_warriors = 6
action_cooldown = 0
action_wait_time = 90
attack = False
potion = False
clicked = False

def turnslefttext():
    turnsinfo= font.render("Turns left: "+str(playerturncounter),True, black)
    screen.blit(turnsinfo,(0,450))


#define game variables fior attacking
masterplayercounter=0
playerturncounter = 3
enemyturncounter =3
playerattackingunit=0
defendingAIdef=0
defendingAIhp=0

class whichplayerselected():
    def __init__(self):
        self.v1=self.selected.x
        self.v2=self.selected.y

    def selected(self,x,y):
        if PU1.draw():
            x=3
        if PU2.draw():
            x=3
        if PU3.draw():
            x=3
        if AIU1.draw():
            y=1
        if AIU2.draw():
            y=1
        if AIU3.draw():
            y=1
        

def button1_clicked():
   print("Button 1 clicked")

x=0
y=0
playerselectunit=0
enemyturn=1
selectenemy=1
battlephase=0
playerfighting=20

def unitLVL(P):
    if P.exp >= 100:
        P.rank += 1
        P.exp = 0
        P.attack += 4
        P.defence += 3
        P.exp = 0
        P.hp = 100
    

def main():
    run = True
    while run:
        #Allow Main to access global Variables
        global playerfighting,selectenemy,battlephase,playerselectunit,playerturncounter,masterplayercounter,enemyturncounter,playerattackingunit,defendingAIdef,defendingAIhp, AIList,x,y
        fpslock()
        loadimages()
        drawunit()
        turnslefttext()
        #draw Warrior
        for unit in PlayerUnitList:
            unit.draw()

        for unit in AIList:
            unit.draw()
       
        playeraction=0
        t=0

        PU1ATK=fightingphase(0,0,PlayerUnitList,AIList)

        unit1slected=False

   
    
        
      
        while t==0:
            if playerfighting >0:
                while playerselectunit==0:
                    if PU1.draw():
                        x=0
                        print(x)
                        battlephase+=1
                        playerselectunit+=1
                        selectenemy=0
                        print(battlephase)
                    if PU2.draw():
                        x=1
                        print(x)
                        battlephase+=1
                        playerselectunit+=1
                        selectenemy=0
                        print(battlephase)

                    if PU3.draw():
                        x=2
                        print(x)
                        battlephase+=1
                        playerselectunit+=1
                        selectenemy=0
                        print(battlephase)

                    else:
                        break
                
                while selectenemy==0:
                    if AIU1.draw():
                        y=0
                        print(y)
                        battlephase+=1
                        selectenemy+=1
                        print(battlephase)
                    if AIU2.draw():
                        y=1
                        print(y)
                        battlephase+=1
                        selectenemy+=1
                        print(battlephase)
                    if AIU3.draw():
                        y=2
                        print(y)
                        battlephase+=1
                        selectenemy+=1
                        print(battlephase)
                    else:
                        break
                
                while battlephase==2:
                    krope= fightingphase(x,y,PlayerUnitList,AIList)
                    krope.battlecalculation()
                    print("End fighting")
                    battlephase=0    
                    playerselectunit=0
                    playerfighting-=1
                    
                   

                        
                else:
                    break
        
            else:
                break

        unitLVL(Playerunit1)
        unitLVL(Playerunit2)
        unitLVL(Playerunit3)
        unitLVL(AIUnit1)
        unitLVL(AIUnit2)
        unitLVL(AIUnit3)
        



            
    
        # if PU1.draw():
        #     P1=True
        # if PU2.draw():
        #     P2=True
        # if PU3.draw():
        #     P3=True

        # if AIU1.draw():
        #     A1=True
        # if AIU2.draw():
        #     A2=True
        # if AIU3.draw():
        #     A3=True

        # if P1 or P2 or P3 != False:           
        #     print(P1,P2,P3,A1,A2,A3)    
        
        
        #Attack Sequence
        # clciked=0

        # if masterplayercounter !=6:
        #         if PU1.draw():
        #             Attacker=int(0)
        #         if PU2.draw():
        #             Attacker=int(1)
        #         if PU3.draw():
        #             Attacker=int(2)

        #         if AIU1.draw():
        #             Target=int(0)
        #         if AIU2.draw():
        #             Target=int(1)
        #         if AIU3.draw():
        #             Target=int(2)

        #     while playerturncounter!=0:
                
    
            
            # while enemyturncounter!=0:
            #     Attacker= random.randint(0,2)
            #     Target= random.randint(0,2)
            #     dam= AIList[Attacker].sasageyo(PlayerUnitList[Target].defence, PlayerUnitList[Target].hp)
            #     PlayerUnitList[Target].hp=PlayerUnitList[Target].hp  - dam
            #     AIList[Attacker].exp+=dam
               
            #     if dam >10:
            #         extra=1.2

            #     elif dam<=0:
            #         extra=1.5

            #     else:
            #         extra=1

            #     TargetEXPEarned=PlayerUnitList[Target].defence*extra
            
            #     PlayerUnitList[Target].exp+=TargetEXPEarned
            
                
            #     print("-------")
            #     print(AIList[Attacker].name+" attacked "+PlayerUnitList[Target].name )
            #     print("Damage dealt: ",dam)
            #     print("Extra Bonus exp percentage decimal: ",extra)
            #     print("Target Exp Earned: ",TargetEXPEarned)
            #     print("-------")
                
            #     enemyturncounter-=1
            #     masterplayercounter +=1

             
             
        

        # aihealth=0

        # if masterplayercounter!=3:
            #aihealth.hp- attackingunit.attack
        

                    
           

            # if defenceenemycounter!=0:
            #     if AIU1.draw():
            #         print("1")
            #         defenceenemycounter -=1
            #         defendingAIdef=AIUnit1.defence
            #         defendingAIhp=AIUnit1.hp

                    
            #     elif AIU2.draw():
            #         print('2')
            #         defendingAIdef=AIUnit2.defence
            #         defendingAIhp=AIUnit2.hp
                    
            #     elif AIU3.draw():
            #         print("3")
            #         defendingAIdef=AIUnit3.defence
            #         defendingAIhp=AIUnit3.hp
                    
            # else:  

            #     defenceenemycounter=1
            #     masterplayercounter+=1

        # 

   

        #Event Handler ALl code in main should be above this
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
            else:
                clicked= False
    
            

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
  main()
