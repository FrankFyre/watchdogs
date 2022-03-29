import pygame
import random
import logging
import time
pygame.init()
pygame.font.init()

# Log settings/formatting
logging.basicConfig(filename='Proglog.log',level=logging.INFO, format='%(asctime)s :: %(message)s', filemode='w')

#window
screenwidth = 1475
screenheight = 500
screen = pygame.display.set_mode((screenwidth, screenheight))
#Set Game Name
pygame.display.set_caption("Purgatory")

#Define fonts
font= pygame.font.Font('Romanica.ttf', 24) 
fontsmall= pygame.font.Font('Romanica.ttf', 12) 
fontbig= pygame.font.Font('metro.ttf', 90) 

#Define colors
red    = (255,   0, 0)
green  = (  0, 255, 0)
black  = (  0,   0, 0)
white  = (255, 255,255)
Pink   = (241, 182,151)
darkpink =(164,41,111)

###store images
#background
bgimage= pygame.image.load("img/bg3.png").convert_alpha()
menu= pygame.image.load("img/menu.png").convert_alpha()

infopanel= pygame.image.load("img/infopanel2.png").convert_alpha()
attackpanel = pygame.image.load("img/panelfight.jpg").convert_alpha()

#Assets
tankselectimg= pygame.image.load("img/t.png").convert_alpha()
warselectimage= pygame.image.load("img/w.png").convert_alpha()
coinimg= pygame.image.load("img/coin.png").convert_alpha()

#potions
#Under Free use 
#<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
atkpotion= pygame.image.load("img/atkpotion.png").convert_alpha()
hppotion= pygame.image.load("img/hppotion.png").convert_alpha()
defpotion= pygame.image.load("img/defpotion.png").convert_alpha()

#other
nameplate= pygame.image.load("img/nameplate.png").convert_alpha()


#Button
attackbuttonimage= pygame.image.load("img/attack.png").convert_alpha()
targetbuttonimage= pygame.image.load("img/Target.png").convert_alpha()
startbutton= pygame.image.load("img/start.png").convert_alpha()
exitbutton=pygame.image.load("img/exit.jpg").convert_alpha()

#Units
playertankimg = pygame.image.load("img/tanker1.png").convert_alpha()
playerwarriorimg = pygame.image.load("img/warrior1.png").convert_alpha()
enemytankimg = pygame.image.load("img/tanker2.png").convert_alpha()
enemywarriorimg = pygame.image.load("img/warrior2.png").convert_alpha()


####CLASSES
# Unit Class
class MasterUnit():
    def __init__(self, x, y, img, name, max_hp, current_hp,attack, defence, exp, rank, typer, potion):
        self.name = name
        self.max_hp = max_hp
        self.hp = current_hp
        self.attack = attack
        self.defence = defence
        self.alive = True
        self.image = img
        self.exp = exp
        self.rank = rank
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.type=typer
        self.potion = potion
 
    #Calculate Damage
    def sasageyo(self, targetdef, targethp):
        #deal damage to enemy
        damage = self.attack - targetdef+ random.randint(-5,10)
        if damage<=0:
            return 0
        else:
            return damage


    #This function generate unit stats
    def generateunit(x,y,name,type,img,AIProgress):
        if img=="PT":
            imagename=playertankimg
        elif img=="PW":
            imagename=playerwarriorimg
        elif type=="tank" and img=="A":
            imagename=enemytankimg
        elif type=="war" and img=="A":
            imagename=enemywarriorimg
    
        if type=="war":
            unit = MasterUnit(x, y, imagename, name, 100,100, random.randint(5,20), random.randint(1,10), 0, 1+AIProgress ,("Warrior"),0)
        if type=="tank":
            unit = MasterUnit(x, y, imagename, name, 100,100, random.randint(1,10), random.randint(5,15), 0, +AIProgress,("Tanker"),0 )
        return unit 


    def draw(self):
        screen.blit(self.image, self.rect)

# Fight night
class fightingphase():
    def __init__(self, Attacker, Target, AttackerList, Targetlist):
        self.attacking=Attacker
        self.targeting=Target
        self.Attackinglist=AttackerList
        self.Targetinglist=Targetlist

    #Attacking phase 
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


        #Draws Text for player attacking
        textpanel()
        text= (str(self.Attackinglist[self.attacking].name) + " dealt "+ str(dam)+" damage to " + str(self.Targetinglist[self.targeting].name ))
        rumble= font.render(text,True, white)
        screen.blit(rumble,(545,90))
        pygame.display.update()
        time.sleep(1.5)#On purpose to show text on screen


        logging.info(self.Attackinglist[self.attacking].name +" attacked "+ self.Targetinglist[self.targeting].name )
        logging.info('Damage dealt: ' + str(dam))
        logging.info("Extra Bonus exp percentage decimal: "+ str(extra))
        logging.info('Target Exp Earned: '+ str(TargetEXPEarned))

        return dam
      
    #AI Attack logic
    def Aiattacking(y1,y2,y3):
        APU=[]
        APU.clear()

        
        if Playerunit1.alive==True:
            APU.append(0)
        if Playerunit2.alive==True:
            APU.append(1)
        if Playerunit3.alive==True:
            APU.append(2)

        if AIUnit1.alive==True:
            y=random.choice(APU)
            slay=fightingphase(0,y, AIList,PlayerUnitList)
            slay.battlecalculation()
            pygame.display.update()
            time.sleep(1.5) 

        if AIUnit2.alive==True:
            y=random.choice(APU)
            slay=fightingphase(1,y, AIList,PlayerUnitList)
            slay.battlecalculation()
            pygame.display.update()
            time.sleep(1.5) #so user can see the text. Pc is too strong 

        if AIUnit3.alive==True:
            y=random.choice(APU)
            slay=fightingphase(2,y, AIList,PlayerUnitList)
            slay.battlecalculation()
         
            pygame.display.update()
            time.sleep(1.5) #so user can see the text. Pc is too strong     
        
#button class
class Button():
	def __init__(self, x, y, image):
		self.image=image
		self.rect=self.image.get_rect()
		self.rect.topleft=(x,y)
		self.clicked=False

	def draw(self):
		action=False
		#get mouse position
		position=pygame.mouse.get_pos()

		#Check mouse clicks
		if self.rect.collidepoint(position):
			if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
				self.clicked=True
				action=True

		if pygame.mouse.get_pressed()[0]==0:
			self.clicked=False

		#draw button on screen
		screen.blit(self.image,(self.rect.x,self.rect.y))

		return action
    
#Draw Unit's Informations
#Information panel
def DrawText (Name,type,atk,deff,exp,rank,currenthp,maxhp,x,y):
    n=font.render(str(Name),True, Pink)
    t=font.render(str(type),True, Pink)
    atk=font.render(str(atk),True, Pink)
    defence=font.render(str(deff),True, Pink)
    exp=font.render(str(round(exp)),True, Pink)
    rank=font.render(str(rank),True, Pink)
    hp=font.render(str(currenthp)+"/"+str(maxhp),True, Pink)
    

    screen.blit(n,(14+x,7+y))
    screen.blit(t,(200+x,7+y))
    screen.blit(atk,(72+x,42+y))
    screen.blit(defence,(194+x,42+y))
    screen.blit(exp,(72+x,75+y))
    screen.blit(rank,(194+x,75+y))
    screen.blit(hp,(70+x,107+y))
    
def unitinformation():
        if Playerunit1.alive==True:
            DrawText(Playerunit1.name,Playerunit1.type, Playerunit1.attack,Playerunit1.defence,Playerunit1.exp, Playerunit1.rank, Playerunit1.hp,Playerunit1.max_hp,0,300)
        if Playerunit2.alive==True:
            DrawText(Playerunit2.name,Playerunit2.type, Playerunit2.attack,Playerunit2.defence,Playerunit2.exp, Playerunit2.rank, Playerunit2.hp,Playerunit2.max_hp,0,150) 
        if Playerunit3.alive==True:
            DrawText(Playerunit3.name,Playerunit3.type, Playerunit3.attack,Playerunit3.defence,Playerunit3.exp, Playerunit3.rank, Playerunit3.hp,Playerunit3.max_hp,0,0) 
        if AIUnit1.alive==True:
            DrawText(AIUnit1.name,AIUnit1.type, AIUnit1.attack,AIUnit1.defence,AIUnit1.exp, AIUnit1.rank, AIUnit1.hp,AIUnit1.max_hp,1175,300)
        if AIUnit2.alive==True:
            DrawText(AIUnit2.name,AIUnit2.type, AIUnit2.attack,AIUnit2.defence,AIUnit2.exp, AIUnit2.rank, AIUnit2.hp,AIUnit2.max_hp,1175,150) 
        if AIUnit3.alive==True:
            DrawText(AIUnit3.name,AIUnit3.type, AIUnit3.attack,AIUnit3.defence,AIUnit3.exp, AIUnit3.rank, AIUnit3.hp,AIUnit3.max_hp,1175,0)  


def infopanels():
    if Playerunit1.alive==True:
        screen.blit(infopanel, (0,300))
    if Playerunit2.alive==True:
       screen.blit(infopanel, (0,150)) 
    if Playerunit3.alive==True:
       screen.blit(infopanel, (0,0))
   
    if AIUnit1.alive==True:
        screen.blit(infopanel, (1175,300))
    if AIUnit2.alive==True:
        screen.blit(infopanel, (1175,150)) 
    if AIUnit3.alive==True:
        screen.blit(infopanel, (1175,0))


###Button Creation
#P/AI= player/AI, U=Unit, digit=designation
PU1 = Button( 220, 410, attackbuttonimage)
PU2 = Button( 220, 260, attackbuttonimage)
PU3 = Button( 220, 110, attackbuttonimage)


AIU1 = Button( 1396, 410, targetbuttonimage)
AIU2 = Button( 1396, 260, targetbuttonimage)
AIU3 = Button( 1396, 110, targetbuttonimage)

#Potions Buttons
hppot=Button(10, 460, hppotion)
atkpot=Button(100, 460, atkpotion)
defpot=Button(190, 460, defpotion)


#Other buttons 
start=Button( 550, 320, startbutton)
exit=Button( 775, 320, exitbutton)


warriorselect=Button( 540,210, warselectimage)
tankerselect=Button( 770,210, tankselectimg)

#function for drawing panels

def textpanel():
    screen.blit(attackpanel, (520,87))    

#Funtion to check AI deaths     
def checkenemydeath():
    if AIUnit1.hp <= 0:
        AIUnit1.alive=False
        AIUnit1.hp=0
       
    if AIUnit2.hp <= 0:
        AIUnit2.alive=False
        AIUnit2.hp=0

    if AIUnit3.hp <= 0:
        AIUnit3.alive=False
        AIUnit3.hp=0

    if AIUnit1.alive ==False and AIUnit2.alive==False and AIUnit3.alive ==False:

        return True

#Funtion to check Players unit deaths 
def checkplayerdeath():
    if Playerunit1.hp <= 0:
        Playerunit1.alive = False
        Playerunit1.hp=0
       
    if Playerunit2.hp <= 0:
        Playerunit2.alive = False
        Playerunit2.hp=0

    if Playerunit3.hp <= 0:
        Playerunit3.alive = False
        Playerunit3.hp=0

    if Playerunit1.alive ==False and Playerunit2.alive==False and Playerunit3.alive ==False:
        return True

#Count player turns
def turnslefttext():
    turnsinfo= font.render("Turns left: "+str(playerturncounter),True, Pink)
    screen.blit(turnsinfo,(310,0))

#Draw textbox to type in names
def unitnameinput():
    screen.blit(nameplate, (650, 160))
    text_surface = font.render(unitname, True, white)
    screen.blit(text_surface, (656, 157))

#Potions 
def potionsfunc(type):
    for unit in PlayerUnitList:
        if type==1:
            logging.info('Healing Potion used')
            if unit.hp <= 95:
                unit.hp += 5
            elif unit.hp >=95:
                unit.hp = 100
        elif type==2:
            logging.info('Attack Potion used')
            unit.attack+=5   
        elif type ==3:
            logging.info('Defence Potion used')
            unit.defence+=5     

#coins 
def coins():
    screen.blit(coinimg,(310,30))
    coincounter = font.render("x"+str(totalcoins),True, white)
    screen.blit(coincounter,(345,30))

#Unit Level Up
def unitLVL(P):
    if P.exp >= 100:
        P.rank += 1
        P.exp = 0
        P.attack += 4
        P.defence += 3
        P.exp = 0
        P.hp += 15
        logging.info('One of your unit(s) have ranked up')
        if P.hp >= 100:
            P.hp = 100

#Game Over screen        
def show_gameover():
    screen.blit(menu,(0,0))
    gg = fontbig.render("G A M E O V E R",True, white)
    screen.blit(gg,(380,90))

#Fps setter
def fpslock():
    FPS = 60 # frames per second setting
    fpsClock = pygame.time.Clock()
    fpsClock.tick(FPS)        
   
#Define global variables to be used in Main
unitname=""  
masterplayercounter=0
playerturncounter = 3
playerattackingunit=0
defendingAIdef=0
defendingAIhp=0
x=0
y=0
playerselectunit=0
enemyturn=0
selectenemy=1
battlephase=0
playerfighting=30
gamephase=False
menuselection=False
selectunit=True
ppu1=1
total_warriors = 6
action_cooldown = 0
action_wait_time = 90
attack = False
potion = False
clicked = False
mainmenu=True
enemyturncounter=0
generateAIunit=False
checkingPlayerDeath=False
AIList = []
PlayerUnitList=[]
checkingAIDeath=False
AIProgress=0
totalcoins=0


def main():
    run = True
    while run:
        #Allow Main to access global Variables
        global PlayerUnitList,selectunit,menuselection,unitname,gamephase,playerfighting,selectenemy,battlephase
        global playerselectunit,playerturncounter,masterplayercounter,enemyturn,playerattackingunit,defendingAIdef,defendingAIhp,x,y
        global Playerunit1,Playerunit2,Playerunit3,ppu1,mainmenu,enemyturncounter
        global AIList,AIUnit1,AIUnit2,AIUnit3,generateAIunit,checkingAIDeath,checkingPlayerDeath,AIProgress,totalcoins
        fpslock()
        
        #Main Menu Loop
        while mainmenu==True: 
            screen.blit(menu,(0,0))
            Welcome= fontbig.render("P U R G A T O R Y",True, white)
            screen.blit(Welcome,(380,90))
            if start.draw():
                mainmenu=False
                menuselection=True

            if exit.draw():
                run=False
            else:
                break
        if menuselection==True: #Unit Selection Loop
            totalcoins=0 #Resets Coin Count After Death
            if selectunit==True:
                screen.blit(menu, (0, 0))
                line1= font.render("Enter a name (Max 10 Character)",True, white)
                line2= font.render("Then click a profession",True, white)
                line3= font.render("Unit "+str(ppu1),True, Pink)
                
                screen.blit(line1,(570,50))
                screen.blit(line2,(615,85))
                screen.blit(line3,(699,115))

                screen.blit(playerwarriorimg, (540,260))
                screen.blit(playertankimg, (770,260))
                
                unitnameinput()
                PlayerUnitList.clear()
                #Generate unit when clcik
                if ppu1==1:
                    if warriorselect.draw():
                        Playerunit1=MasterUnit.generateunit(380,390,unitname,"war","PW",0)
                        ppu1+=1

                    if tankerselect.draw():
                        Playerunit1=MasterUnit.generateunit(380,390,unitname,"tank","PT",0)
                        ppu1+=1
                if ppu1==2:    
                    if warriorselect.draw():
                        Playerunit2=MasterUnit.generateunit(510, 350,unitname,"war","PW",0)
                        ppu1+=1
                      
            
                    if tankerselect.draw():
                        Playerunit2=MasterUnit.generateunit(510, 350,unitname,"tank","PT",0)
                        ppu1+=1
                if ppu1==3:
                    if warriorselect.draw():
                        Playerunit3=MasterUnit.generateunit(640, 310,unitname,"war","PW",0)
                        ppu1+=1
                      
            
                    if tankerselect.draw():
                        Playerunit3=MasterUnit.generateunit(640, 310,unitname,"tank","PT",0)
                        ppu1+=1
                if ppu1==4:
                    PlayerUnitList.append(Playerunit1)
                    PlayerUnitList.append(Playerunit2)
                    PlayerUnitList.append(Playerunit3)
                    selectunit=False  
                    generateAIunit=True
                    gamephase=True
                    menuselection=False
        #Generates AI Stats/Info           
        if generateAIunit==True: 
            AIList=[]
            #Generate AI
            typelist=["war","tank"]

            AIUnit1 =MasterUnit.generateunit(1080, 390,  'AI ' + str(random.randint(0,9)) + str(random.randint(0,9)),random.choice(typelist),"A",AIProgress)
            AIUnit2 =MasterUnit.generateunit( 950, 350,  'AI ' + str(random.randint(0,9)) + str(random.randint(0,9)),random.choice(typelist),"A",AIProgress)
            AIUnit3 =MasterUnit.generateunit( 820, 310,  'AI ' + str(random.randint(0,9)) + str(random.randint(0,9)),random.choice(typelist),"A",AIProgress)

            AIList.insert(0,AIUnit1)
            AIList.insert(1,AIUnit2)
            AIList.insert(2,AIUnit3)
            AIProgress+=1
            gamephase=True
            generateAIunit=False
            logging.info('AI has been generated')
                       
        #Main Game Loop      
        while gamephase==True: 
            
            screen.blit(bgimage,(0,0))
            checkenemydeath()
            unitinformation()
            infopanels()
            turnslefttext()
            coins()
            unitLVL(Playerunit1)
            unitLVL(Playerunit2)
            unitLVL(Playerunit3)
            unitLVL(AIUnit1)
            unitLVL(AIUnit2)
            unitLVL(AIUnit3)

            for unit in PlayerUnitList:
                if unit.alive==True:
                    unit.draw()
            for unit in AIList:
                if unit.alive==True:
                    unit.draw()
            if totalcoins>40:
                hp= fontsmall.render("Hp: 50c ",True, white)
                screen.blit(hp,(45,470))
                if hppot.draw():
                    potionsfunc(1)
                    totalcoins-=50
            if totalcoins>20:
                atk= fontsmall.render("Atk: 20c ",True, white)
                screen.blit(atk,(135,470))
                if atkpot.draw():
                    potionsfunc(2)
                    totalcoins-=20
            if totalcoins>30:
                defp = fontsmall.render("Def: 30c ",True, white)
                screen.blit(defp,(220,470))
                if defpot.draw():
                    potionsfunc(3)
                    totalcoins-=30
    
            #Fighting game loop
            if checkingAIDeath==False and checkingPlayerDeath==False:
                if 1<=playerturncounter<=3: #This checks player turns and attacks
                    while playerselectunit==0:
                        if Playerunit1.alive==True:
                            if PU1.draw():
                                x=0
                     
                                battlephase+=1
                                playerselectunit+=1
                                selectenemy=0
                     
                        if Playerunit2.alive==True:
                            if PU2.draw():
                                x=1
                     
                                battlephase+=1
                                playerselectunit+=1
                                selectenemy=0
                     
                        if Playerunit3.alive==True:
                            if PU3.draw():
                                x=2
                     
                                battlephase+=1
                                playerselectunit+=1
                                selectenemy=0
                     

                            else:
                                break
                        else:
                            break
                    while selectenemy==0:
                        if AIUnit1.alive==True:
                            if AIU1.draw():
                                y=0
                            
                                battlephase+=1
                                selectenemy+=1
                            
                        if AIUnit2.alive==True:
                            if AIU2.draw():
                                y=1
                            
                                battlephase+=1
                                selectenemy+=1
                            
                        if AIUnit3.alive==True:
                            if AIU3.draw():
                                y=2
                            
                                battlephase+=1
                                selectenemy+=1
                            
                            else:
                                break
                        else:
                            break
                    while battlephase==2:
                        krope= fightingphase(x,y,PlayerUnitList,AIList)
                        totalcoins+=krope.battlecalculation()
                        battlephase=0    
                        playerselectunit=0
                        playerturncounter-=1
                        enemyturn+=1
                        if checkenemydeath()==True:
                            checkingAIDeath=True
                        
                    else:
                        break
                #Ai turns and Attacks
                if playerturncounter==0: 
                    while enemyturn>0:
                        if checkplayerdeath()==True:
                            checkingPlayerDeath=True
                        fightingphase.Aiattacking(90,115,140)
                        playerturncounter+=3
                        enemyturn-=3
                        if checkplayerdeath()==True:
                            checkingPlayerDeath=True
    
                    else:
                        break
                
            #Checks AI Death     
            if checkingAIDeath==True: 
                enemyturncounter=0
                gamephase=False
                generateAIunit=True
                checkingAIDeath=False
                playerturncounter = 3

        #Checks players death 
        if checkingPlayerDeath==True:
            gamephase=False
            show_gameover()
            if start.draw():
                menuselection=True
                enemyturncounter=0
                gamephase=False
                playerturncounter = 3
                checkingPlayerDeath=False
                selectunit=True
                ppu1=1


            if exit.draw():
                run=False

       
            

        #Event Handler ALl code in main should be above this
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
            else:
                clicked= False
            
            
            if event.type == pygame.KEYDOWN:
            # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    unitname = unitname[:-1]
                else:
                    unitname += event.unicode
            

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
  main()
