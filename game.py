import pygame
import os
import time
import random
import sys
from pygame import mixer
pygame.init()
mixer.init()

zero = 0
if not os.path.exists('highscore.txt'):
    f = open('highscore.txt', 'w')
    f.write(str(zero))
    f.close

v = open('highscore.txt', 'r')
topScore = int(v.readline())
v.close()

crash_sound = pygame.mixer.Sound("Crash.wav")
_songs = ['song/Kirby_s Return to Dream Land Title Theme 8 Bit Remix.mp3',
'song/Clout [8 Bit Tribute to Offset feat. Cardi B] - 8 Bit Universe.mp3',
'song/Dave Rodgers - Déjà Vu 8Bit.mp3',
'song/A Thousand Miles [8 Bit Tribute to Vanessa Carlton] - 8 Bit Universe.mp3',
'song/Feels (8-Bit NES Remix).mp3',
'song/Harder Better Faster Stronger [8 Bit Cover Tribute to Daft Punk] - 8 Bit Universe.mp3',
'song/Manuel - Gas Gas Gas 8Bit.mp3']
_currently_playing_song = None
pause=False
gray=(99, 110, 114)
# gray=(178,190,195)
white=(255,255,255)
light_black=(30, 39, 46)
green=(46, 204, 113)
red=(194, 54, 22)
blue=(52, 152, 219)
bright_green=(76, 209, 55)
bright_red=(232, 65, 24)
bright_blue=(0, 168, 255)
black=(0,0,0)
display_width=1024
display_height= 800
crashimage=pygame.image.load("car6.png")
crashimg=pygame.image.load("car6.png")
gamedisplays=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Car Rush")
clock=pygame.time.Clock()
carimg = pygame.image.load('car2.png')
backgroundpic = pygame.image.load("download14.jpg")
yellow_strip=pygame.image.load("yellow-strip.jpg")
strip=pygame.image.load("strip.jpg")
car_width=60
intro_background =pygame.image.load("cargame.jpg")
end_background=pygame.image.load("instructions.jpg")





def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.ext()
        gamedisplays.blit(intro_background,(0,0))
        largetext=pygame.font.Font('8bit16.ttf', 115)
        TextSurf, TextRect=text_objects("CAR RUSH",largetext)
        TextRect.center=(530,75)
        gamedisplays.blit(TextSurf,TextRect)
        button("START",120,620,150,50, green, bright_green,"play")
        button("INSTRUCTION",395,620,250,50, blue, bright_blue,"intro")
        button("QUIT",770,620,150,50, red, bright_red,"quit")
        pygame.display.update()
        clock.tick(50)



def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()


    else:
        pygame.draw.rect(gamedisplays,ic,(x,y,w,h))
    smalltext=pygame.font.Font("8bit16.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)



def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(end_background, (0,0))
        largetext=pygame.font.Font('8bit16.ttf',80)
        mediumtext=pygame.font.Font('8bit16.ttf',40)
        smalltext=pygame.font.Font('8bit16.ttf',20)
        button("BACK",674,700,300,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)


def paused():
    pygame.mixer.music.pause()
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            pygame.draw.rect(gamedisplays, light_black, [240,300,550,300])
            largetext=pygame.font.Font('8bit16.ttf',115)
            TextSurf,TextRect=text_objects("PAUSED",largetext)
            TextRect.center=(524),(400)
            gamedisplays.blit(TextSurf,TextRect)
            button("CONTINUE",264,520,140,50, green, bright_green,"unpause")
            button("RESTART",452,520,140,50, blue, bright_blue,"play")
            button("MAIN MENU",630,520,140,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)


def unpaused():
    pygame.mixer.music.unpause()
    global pause
    pause=False


def countdown_background():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.47)
    y=(display_height*0.7)
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(920,0))
    gamedisplays.blit(yellow_strip,(512,0))
    gamedisplays.blit(yellow_strip,(512,100))
    gamedisplays.blit(yellow_strip,(512,200))
    gamedisplays.blit(yellow_strip,(512,300))
    gamedisplays.blit(yellow_strip,(512,400))
    gamedisplays.blit(yellow_strip,(512,500))
    gamedisplays.blit(yellow_strip,(512,600))
    gamedisplays.blit(yellow_strip,(512,700))
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(900,0))
    gamedisplays.blit(strip,(900,100))
    gamedisplays.blit(strip,(900,200))
    text=font.render("Passed: 0",True,black)
    score=font.render("Score: 0", True,white)
    highscore = font.render("HighScore:",True,white)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))
    gamedisplays.blit(highscore,(0,70))

def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('8bit16.ttf',115)
            TextSurf,TextRect=text_objects("3",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('8bit16.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('8bit16.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('8bit16.ttf',115)
            TextSurf,TextRect=text_objects("LEVEL 1 GO!!!!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()




def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

def stop_playist():
    pygame.mixer.music.stop()

def obstacle(obs_startx, obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("car4.png")
    elif obs==1:
        obs_pic=pygame.image.load("car5.png")
    elif obs==2:
        obs_pic=pygame.image.load("car3.png")
    elif obs==3:
        obs_pic=pygame.image.load("car2.png")
    elif obs ==4:
        obs_pic = pygame.image.load("car7.png")
    elif obs ==5:
        obs_pic = pygame.image.load("car8.png")
    elif obs ==6:
        obs_pic = pygame.image.load("car9.png")
    elif obs ==7:
        obs_pic = pygame.image.load("car10.png")
    elif obs ==8:
        obs_pic = pygame.image.load("car11.png")
    elif obs ==9:
        obs_pic = pygame.image.load("car12.png")
    elif obs ==10:
        obs_pic = pygame.image.load("car13.png")
    elif obs ==11:
        obs_pic = pygame.image.load("car14.png")
    elif obs ==12:
        obs_pic = pygame.image.load("car15.png")
    elif obs ==13:
        obs_pic = pygame.image.load("car16.png")
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))


def score_system(passed,score,topScore):
    font=pygame.font.SysFont(None,25)
    text=font.render("Passed "+str(passed),True,black)
    score=font.render("Score "+str(score),True,white)
    highscore=font.render("HighScore "+str(topScore),True,white)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))
    gamedisplays.blit(highscore,(0,70))





def text_objects(text,font):
    textsurface=font.render(text,True,white)
    return textsurface,textsurface.get_rect()


def message_display(text):
    largetext=pygame.font.Font("8bit16.ttf", 100)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

def crash(score,topScore):
    stop_playist()
    crash_sound.play()
    message_display("YOU CRASHED")




def background():
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(920,0))
    gamedisplays.blit(yellow_strip,(512,0))
    gamedisplays.blit(yellow_strip,(512,100))
    gamedisplays.blit(yellow_strip,(512,200))
    gamedisplays.blit(yellow_strip,(512,300))
    gamedisplays.blit(yellow_strip,(512,400))
    gamedisplays.blit(yellow_strip,(512,500))
    gamedisplays.blit(yellow_strip,(512,600))
    gamedisplays.blit(yellow_strip,(512,700))
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(900,0))
    gamedisplays.blit(strip,(900,100))
    gamedisplays.blit(strip,(900,200))

def car(x,y):
    gamedisplays.blit(carimg,(x,y))





def game_loop():
    global pause
    play_a_different_song()
    x=(display_width*0.47)
    y=(display_height*0.7)
    x_change=0
    obstacle_speed=10
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=100
    obs_height=150
    passed=0
    level=1
    score=0
    y2=10
    fps=120
    bumped=False
    zero = 0
    max_up = 10
    max_down = 5
    if not os.path.exists('highscore.txt'):
        f = open('highscore.txt', 'w')
        f.write(str(zero))
        f.close

    v = open('highscore.txt', 'r')
    topScore = int(v.readline())
    v.close()

    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    paused()
                if event.key==pygame.K_LEFT:
                    x_change-=7.5
                if event.key==pygame.K_RIGHT:
                    x_change=7.5
                if event.key==pygame.K_UP:
                    obstacle_speed+=0.1
                if event.key==pygame.K_DOWN:
                    obstacle_speed-=0.1
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        x+=x_change
        pause =True
        gamedisplays.fill(gray)

        rel_y=y2%backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic,(922,rel_y-backgroundpic.get_rect().width))
        if rel_y<1024:
            gamedisplays.blit(backgroundpic,(0,rel_y))
            gamedisplays.blit(backgroundpic,(0,rel_y))
            gamedisplays.blit(backgroundpic,(0,rel_y))
            gamedisplays.blit(backgroundpic,(922,rel_y+100))
            gamedisplays.blit(yellow_strip,(512,rel_y-100))
            gamedisplays.blit(yellow_strip,(512,rel_y-200))
            gamedisplays.blit(yellow_strip,(512,rel_y-300))
            gamedisplays.blit(yellow_strip,(512,rel_y))
            gamedisplays.blit(yellow_strip,(512,rel_y+100))
            gamedisplays.blit(yellow_strip,(512,rel_y+200))
            gamedisplays.blit(yellow_strip,(512,rel_y+300))
            gamedisplays.blit(yellow_strip,(512,rel_y+400))
            gamedisplays.blit(yellow_strip,(512,rel_y+500))
            gamedisplays.blit(yellow_strip,(512,rel_y+600))
            gamedisplays.blit(yellow_strip,(512,rel_y+700))
            gamedisplays.blit(strip,(120,rel_y-200))
            gamedisplays.blit(strip,(120,rel_y+20))
            gamedisplays.blit(strip,(120,rel_y+30))
            gamedisplays.blit(strip,(900,rel_y-100))
            gamedisplays.blit(strip,(900,rel_y+20))
            gamedisplays.blit(strip,(900,rel_y+30))

        y2+=obstacle_speed


        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score, topScore)
        if x>880-car_width or x <20:
            gamedisplays.blit(crashimg,(x,y))
            crash(score, topScore)
        if x>display_width-(car_width+120) or x<120:
            gamedisplays.blit(crashimg,(x,y))
            crash(score, topScore)
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,14)
            passed=passed+1
            score=passed*10
            if score > topScore:
                g = open("highscore.txt", "w")
                g.write(str(score))
                g.close()
                topScore = score

            if int(passed)%10==0:
                level=level+1;
                obstacle_speed+=5
                largetext=pygame.font.Font("8bit16.ttf", 100)
                textsurf,textrect=text_objects("LEVEL "+str(level),largetext)
                textrect.center=((display_width/2),(display_height/2))
                gamedisplays.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(3)

        if y<obs_starty+obs_height:
            if x>obs_startx and x<obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                 gamedisplays.blit(crashimg,(x,y))
                 crash(score, topScore)

        pygame.display.update()
        clock.tick(fps)

intro_loop()
game_loop()
pygame.quit()
quit()
