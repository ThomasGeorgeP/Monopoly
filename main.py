import pygame as pg
from sys import exit
import random
import time

class User():

    def __init__(self,name,icon_index):

        self.display_name=name
        self.picture=icons[icon_index]
        self.pic_rect=icon_rects[icon_index]
        
        self.index=len(players)

        self.money=1500
        self.no_of_houses=0
        self.no_of_hotels=0
        self.properties=[]
        self.current_roll=''
        self.double_counter=0

def spacecont():
    '''Makes the user click enter between each iteration.'''
    flag=1
    while flag!=0:
        for event in pg.event.get():
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_RETURN:
                    flag=0
            elif event.type==pg.MOUSEBUTTONDOWN:
                if event.button==1:
                    flag=0
            if event.type==pg.QUIT:
                exit()

def textmake(text:str='',size:int=10,font:str='Pixeltype.ttf',color:tuple=(64,64,64)):
    x=pg.font.Font(font,size=size)
    y=x.render(text,False,color)
    return y

def rolldice(position=(1195, 223)):
    global roll
    First_Dice=random.choice(dices)
    Second_Dice=random.choice(dices)    
    screen.blit(First_Dice,position)
    screen.blit(Second_Dice,(position[0]+120,position[1]))
    if gamestate!=2:
        roll=dices.index(First_Dice)+dices.index(Second_Dice)+2
        players[current_turn].current_roll=(roll)
    elif gamestate==2:
        if (dices.index(First_Dice)+dices.index(Second_Dice)+2) not in roll:
            roll.append(dices.index(First_Dice)+dices.index(Second_Dice)+2)
        else:
            rolldice()
        players[current_turn].current_roll=(roll[-1])
        rolls[roll[-1]]=current_turn

pg.init()

clock=pg.time.Clock()
font=pg.font.Font('Pixeltype.ttf',100)
screen=pg.display.set_mode((1500,800))
pg.display.set_caption('MONOPOLY CANT BE PIRATED SO IM MAKING IT')
screen.fill('white')
root=pg.transform.rotozoom(pg.image.load('map.jpg').convert_alpha(),0,0.4)
map=root

nami=pg.image.load('Icons/nami.png').convert_alpha()
arlong=pg.transform.rotozoom(pg.image.load('Icons/arlong.png').convert_alpha(),0,0.8)
brook=pg.transform.rotozoom(pg.image.load('Icons/brook.png').convert_alpha(),0,0.8)
chopper=pg.image.load('Icons/chopper.png').convert_alpha()
franky=pg.transform.rotozoom(pg.image.load('Icons/franky.png').convert_alpha(),0,0.75)
luffy=pg.transform.rotozoom(pg.image.load('Icons/luffy.png').convert_alpha(),0,0.65)
robin=pg.image.load('Icons/robin.png').convert_alpha()
sanji=pg.image.load('Icons/sanji.png').convert_alpha()
sunny=pg.image.load('Icons/sunny.png').convert_alpha()
usopp=pg.image.load('Icons/usopp.png').convert_alpha()
vivi=pg.image.load('Icons/vivi.png').convert_alpha()
zoro=pg.image.load('Icons/zoro.png').convert_alpha()

D1=pg.image.load('Dice/1_dot.png').convert_alpha()
D2=pg.image.load('Dice/2_dots.png').convert_alpha()
D3=pg.image.load('Dice/3_dots.png').convert_alpha()
D4=pg.image.load('Dice/4_dots.png').convert_alpha()
D5=pg.image.load('Dice/5_dots.png').convert_alpha()
D6=pg.image.load('Dice/6_dots.png').convert_alpha()

dices=[D1,D2,D3,D4,D5,D6]
dices=[pg.transform.rotozoom(i,0,0.75) for i in dices]

surround_icon_rect=pg.Rect(940,150,320,600)

icons=[nami,arlong,brook,chopper,franky,luffy,robin,sanji,sunny,usopp,vivi,zoro]

icons=[pg.transform.rotozoom(i,0,0.75) for i in icons]
icon_rects=[icons[i].get_rect(center=(1000+(i%2)*200,200+(i//2)*100)) for i in range(len(icons))]
animate_coff=0

for i in range(0,6):
        
        for event in pg.event.get():
            if event.type==pg.QUIT:
                exit()
        pg.display.update()
        screen.blit(map,(0,0))
        map=pg.transform.rotozoom(map,30,0.85)

pg.display.update()

map=pg.transform.rotozoom(map,0,0.33)

screen.blit(font.render('MONOPOLY',False,'black'),(1100,100))
screen.blit(font.render('-by Thomas',False,(64,64,64)),(1100,200))
screen.blit(pg.font.Font('Pixeltype.ttf',50).render('Click Enter to Continue',False,(64,64,64)),(1150,600))

pg.display.update()
Number_of_Players=''
spacecont()

gamestate=0
player_name_counter=0
players=[]
Name_Temp='Enter Text Here'
current_turn=0

first_roll=True
roll=[]
draw={}
selected_icon=None
rolls={}

#main game loop

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            exit()
        if gamestate==1:
            if event.type==pg.KEYDOWN:
                if event.key!=pg.K_BACKSPACE and event.key!=pg.K_RETURN:
                    Name_Temp+=event.unicode
                elif event.key==pg.K_BACKSPACE:
                    Name_Temp=Name_Temp[:-1]
                elif event.key==pg.K_RETURN and draw.get(True,None) not in [None,[]] and Name_Temp!='Enter Text Here':
                    New_Player=User(Name_Temp,draw[True])
                    Name_Temp='Enter Text Here'
                    player_name_counter+=1
                    del icons[draw[True]]
                    del icon_rects[draw[True]]
                    del draw[True]
                    players.append(New_Player)
                    if player_name_counter==Number_of_Players:
                        gamestate=2
                        screen.fill('white')
            elif event.type==pg.MOUSEBUTTONDOWN and event.button==1:
                collision=[i for i in range(len(icons)) if icon_rects[i].collidepoint(pg.mouse.get_pos())]
                if collision!=[]:
                    draw[True]=collision[0]
                elif cls_button_rect.collidepoint(pg.mouse.get_pos()):
                    Name_Temp=''
            

    
    if gamestate==0: #INPUTTING NUMBER OF PLAYERS
        pressed_keys=pg.key.get_pressed()
        screen.fill('white')

        if Number_of_Players!='' and Number_of_Players!='Invalid Number':
            screen.blit(textmake('Click Enter to Continue.',60),(1050,700))
            
        if Number_of_Players!='' and Number_of_Players!='Invalid Number' and pressed_keys[pg.K_RETURN]==True:
            Number_of_Players=int(Number_of_Players)
            gamestate=1
            continue
        
        screen.blit(textmake('How Many Players?(2-5) ',100),(500,100))
        screen.blit(textmake(Number_of_Players,100),(800,400))
        if pressed_keys[pg.K_2]==True:
            Number_of_Players=2
        elif pressed_keys[pg.K_3]==True:
            Number_of_Players=3
        elif pressed_keys[pg.K_4]==True:
            Number_of_Players=4
        elif pressed_keys[pg.K_5]==True:
            Number_of_Players=5
        elif True in pressed_keys and pressed_keys[pg.K_RETURN]!=True:
            Number_of_Players='Invalid Number'
        Number_of_Players=str(Number_of_Players)         
        
    elif gamestate==1: #INPUTTING NAME OF PLAYERS and icons

        Name_Temp_Rect=textmake(Name_Temp,100).get_rect(center=(400,350))
        cls_button=textmake('Clear',50)
        cls_button_rect=cls_button.get_rect(center=(600,500))
        
        screen.fill('white')
        screen.blit(cls_button,cls_button_rect)
        pg.draw.rect(screen,(139, 178, 240),Name_Temp_Rect)
        screen.blit(textmake(f'Enter Name of Player {player_name_counter + 1}                         Choose Your Icon',80),(100,80))
        screen.blit(textmake(Name_Temp,100),Name_Temp_Rect)
        screen.blit(textmake(f'{15-len(Name_Temp)} Characters Remaining. ',70),(100,700))
        pg.draw.rect(screen,(185, 205, 237),surround_icon_rect)
        if draw.get(True,None) not in [None,[]]:
            pg.draw.rect(screen,(196, 86, 86),icon_rects[draw[True]])
        [screen.blit(icons[i],icon_rects[i]) for i in range(len(icons))]

        if len(Name_Temp)>15:
            Name_Temp=Name_Temp[:15]
        if draw.get(True,None) not in [None,[]] and Name_Temp!='Enter Text Here':
            screen.blit(textmake('Click Enter to Continue',50),(1000,760))


    elif gamestate==10:
        screen.fill('white')
        screen.blit(textmake('In Dev',100),(500,500))
        screen.blit(root,(0,0))
        pg.display.update()    
        spacecont()

    elif gamestate==2: #highest roll
        
        screen.blit(textmake('Highest Roll Plays First! ',90),(100,76))
        if current_turn==len(players):
            
            screen.blit(textmake('Game Loading...',100),(800,600))
            pg.display.update()
            time.sleep(3)
            players=[players[i] for i in {rolls[x]:x for x in sorted(list(rolls.keys()),reverse=True)}]
            [print(i.display_name) for i in players]
            gamestate=10
            roll=0
            continue
            
        elif first_roll!=True:
            rolldice()
            current_turn+=1
            
        else:
            first_roll=False
        for i in range(len(players)):
            screen.blit(textmake(f'{players[i].display_name}: {players[i].current_roll}',70),(150,200+i*100))
            screen.blit(players[i].picture,players[i].picture.get_rect(center=(700,220+i*100)))
        pg.display.update()
        spacecont()
        
        
        
    pg.display.update()
    clock.tick(60)          

    
    
