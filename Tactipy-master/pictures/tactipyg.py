import pygame
pygame.mixer.pre_init(22050,16,2,4096)
pygame.init()

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]

villan_walk_right = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                     pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                     pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png')]

villan_walk_left = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                    pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                    pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png')]




bridge = pygame.image.load("bridge.png")
ground = pygame.image.load("ground.png")
fire=pygame.image.load("fire1.png")
log=pygame.image.load('Log.png')
info_board=pygame.image.load("info board.png")
info_image=pygame.image.load("info.png")
gameover=pygame.image.load("gameover.png")
left_stand = pygame.image.load("R1.png")
right_stand = pygame.image.load("L1.png")
life_heart=pygame.image.load("life.png")
signboard=pygame.image.load("ques_board.png")
music=pygame.mixer.music.load("music.mp3")
marsh=pygame.image.load('marsh.png')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1.0)





       # LEVEL 1
output_question = pygame.image.load("bg2.png")
background=pygame.image.load("bgquestion.png")
bg = pygame.image.load('foggy forest 4.jpg')

       # LEVEL 2
bg_2 = pygame.image.load('foggy forest 2.jpg')
background2=pygame.image.load('bgquestion2.png')
info_level2=pygame.image.load("bgquestio9.png")
       # LEVEL_3
bg_3 = pygame.image.load('beach.jpg')
background3=pygame.image.load('lv3 ques.jpeg')
shark=pygame.image.load('shark.png')
ifinfo=pygame.image.load('if info.png')


       # LEVEL 4
bg_4=pygame.image.load('foggy forest 3.jpg')
villan_count=100
villan_run=True
v = 0
w = 0
flag = 1


        # LEVEL 5
cuoriocity_question=pygame.image.load("bennett_question.png")
bennett=pygame.image.load("BU.jpeg")
q5=pygame.image.load("q5.png")
tick=pygame.image.load("tick.jpg")
level_5_tick=False



        # LEVEL 6
bg_6=pygame.image.load("bg_6.jpg")
witch=pygame.image.load("witch.png")
W_x=594
W_y=400
rotate=1
up=1
rotate_right=False
rotate_left=True
w_up=True
w_down=False
fire_vel=5
spike=pygame.image.load("spike.png")
stand=pygame.image.load("standing.png")
fly=False
fly_function=False
zombie_R=[pygame.image.load("1.png"), pygame.image.load("2.png"), pygame.image.load("3.png"), pygame.image.load("4.png"), pygame.image.load("5.png"),
        pygame.image.load("6.png"), pygame.image.load("7.png"), pygame.image.load("8.png"), pygame.image.load("9.png"), pygame.image.load("10.png"),
         pygame.image.load("11.png"), pygame.image.load("12.png"), pygame.image.load("13.png"), pygame.image.load("14.png"), pygame.image.load("15.png"),
         pygame.image.load("16.png")]
thought=pygame.image.load("thought.png")
dark_signboard=pygame.image.load("dark_signboard.png")
skull=pygame.image.load("skull.png")
i=0

def zombie_hands():
    global i
    win.blit(zombie_R[i],(450,420))
    win.blit(zombie_R[i], (550,420))
    win.blit(dark_signboard, (410,520))
    win.blit(skull,(422,520))
    win.blit(signboard, (100, 515))
    i+=1
    if i>=16:
        i=0








walkSteps = 0
villan_walkSteps=0
x = 0
y = 510
V_x=600
V_y=510
vel = 5
jump = True
life=3
isBridge = False
islog=False
Walk = True
left = False
right = False
jumpCount = 10
isJump = False
iscount=True
forcmp=True
Level_1=True
Level_2=False
Level_3=False
Level_4=False
Level_5=False
Level_6=False
Numbers=[]
compare=[]
ans=[1,4,2,3]
ans2=[1,4,3,2,5]
ans3=[3,2,1,4]

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption(" game body ")


def disp_fire():
    pygame.time.delay(10)
    if Level_1:
        win.blit(fire, (330, 570))
        win.blit(fire, (340, 570))
        win.blit(fire, (360, 570))
        win.blit(fire, (390, 570))
        win.blit(fire, (420, 570))
        win.blit(fire, (450, 570))
        win.blit(fire, (480, 570))
        win.blit(fire, (510, 570))
        win.blit(fire, (520, 570))


def log_disp():
    win.blit(log, (345, 574))
    win.blit(log, (371, 574))
    win.blit(log, (396, 574))
    win.blit(log, (420, 574))
    win.blit(log, (445, 574))
    win.blit(log, (470, 574))
    win.blit(log, (495, 574))
    win.blit(log, (520, 574))
    win.blit(log, (545, 574))

def lifedisp():
    global x
    global y
    global run
    if life==3:
        win.blit(life_heart,(x,y-7))
        win.blit(life_heart,(x+20,y-7))
        win.blit(life_heart,(x+40,y-7))
    elif(life==2):
        win.blit(life_heart,(x,y-7))
        win.blit(life_heart,(x+20,y-7))
    elif(life==1):
        win.blit(life_heart,(x,y-7))


def background_items():
    if Level_1:
        win.blit(bg, (0, 0))



    if Level_3:
        win.blit(bg_3, (0,0))


    win.blit(ground, (-25, 570))
    win.blit(ground, (0, 570))
    win.blit(ground, (150, 570))
    win.blit(ground, (550, 570))  # 150  and 550
    win.blit(ground, (600, 570))
    win.blit(signboard, (250, 515))
    win.blit(info_board, (100, 515))

def villan_walk():
    global V_x
    global V_y
    global villan_walkSteps
    global villan_count
    pygame.time.delay(17)
    if villan_count>0:
        win.blit(villan_walk_right[villan_walkSteps//3],(V_x,V_y))
        V_x+=1
    if villan_count<0:
        win.blit(villan_walk_left[villan_walkSteps//3],(V_x,V_y))
        V_x-=1
    bullets()

    villan_walkSteps+=1
    if villan_walkSteps+1 > 27:
        villan_walkSteps=0

    villan_count-=1
    if villan_count == -100:
        villan_count=100


def bullets():
    global x
    global y
    global v
    global w
    global flag
    global life

    win.blit(fire, (v + 40, w + 510))
    win.blit(fire, (v + 170, w + 510))
    win.blit(fire, (v + 300, w + 510))
    win.blit(fire, (v + 430, w + 510))
    win.blit(fire, (v + 570, w + 510))

    if v < 100 and flag == 1:
        v += 5
        w -= 5
        if v == 100:
            flag = 0
    elif flag == 0:
        v -= 5
        w += 5
        if v == 0:
            flag = 1

    if x >= v + 25 + 10 and x <= v + 55 + 10 and y >= w + 500 and y <= w + 520:
        life -= 1
        x = 0
        y = 510
    if x >= v + 155 + 10 and x <= v + 185 + 10 and y >= w + 500 and y <= w + 520:
        life -= 1
        x = 0
        y = 510
    if x >= v + 285 + 10 and x <= v + 315 + 10 and y >= w + 500 and y <= w + 520:
        life -= 1
        x = 0
        y = 510

    if x >= v + 415 + 10 and x <= 445 + 10 and y >= w + 500 and y <= w + 520:
        life -= 1
        x = 0
        y = 510
    if x >= v + 555 + 10 and x <= v + 585 + 10 and y >= w + 500 and y <= w + 520:
        life -= 1
        x = 0
        y = 510

game_start=True
start_info=True


run = True
while (run):
    if Level_1:
        background_items()
        disp_fire()
        lifedisp()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()


    if Level_1:
        if isBridge == False and x > 330 and x < 550 and y == 510:
            life -= 1
            x = 0
            y = 510


        if walkSteps + 1 >= 27:
            walkSteps = 0

        if keys[pygame.K_UP]:
            isJump = True

        if keys[pygame.K_LEFT] and x > 0:
            x = x - vel
            win.blit(walkLeft[walkSteps // 3], (x, y))
            walkSteps += 1
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x <= 745:
            x = x + vel
            win.blit(walkRight[walkSteps // 3], (x, y))
            walkSteps += 1
            left = False
            right = True
        else:
            if right:
                win.blit(left_stand, (x, y))
            elif left:
                win.blit(right_stand, (x, y))

        if isJump:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1

            else:
                jumpCount = 10
                isJump = False
        if (y == 510) and (x >= 210 and x <= 250) and iscount == True:
            if keys[pygame.K_1]:
                Numbers.append(1)
            if keys[pygame.K_2]:
                Numbers.append(2)
            if keys[pygame.K_3]:
                Numbers.append(3)
            if keys[pygame.K_4]:
                Numbers.append(4)
            for i in Numbers:
                if i not in compare:
                    compare.append(i)
            if len(compare) == 4:
                if ans == compare:
                    isBridge = True
                    iscount = False
                    compare=[]
                    Numbers=[]
                else:
                    compare = []
                    Numbers = []
                    life -= 1

        if isBridge:
            win.blit(bridge, (345, 526))
            iscount = False
        if (y == 510) and (x >= 210 and x <= 250):
            win.blit(background, (0, 0))

        if life == 0:
            x = p
            y = j
            win.blit(gameover, (300, 280))
            run = False
        if x > 80 and x < 110 and y == 510:
            win.blit(info_image, (0, -2))

        if x==750 and y<=510 and y>=450:
            Level_1=False
            Level_2=True
            x=0
            y=510
        p = x
        j = y

    if Level_2:
        pygame.time.delay(10)
        win.blit(bg_2, (0, 0))
        win.blit(ground, (-25, 570))
        win.blit(ground, (0, 570))
        win.blit(ground, (150, 570))
        win.blit(ground, (550, 570))  # 150  and 550
        win.blit(ground, (600, 570))
        win.blit(signboard, (250, 515))
        win.blit(info_board, (100, 515))
        win.blit(marsh, (340, 568))
        lifedisp()

        iscount=True


        if walkSteps + 1 >= 27:
            walkSteps = 0

        if keys[pygame.K_UP]:
            isJump = True

        if keys[pygame.K_LEFT] and x > 0:
            x = x - vel
            win.blit(walkLeft[walkSteps // 3], (x, y))
            walkSteps += 1
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x <= 745:
            x = x + vel
            win.blit(walkRight[walkSteps // 3], (x, y))
            walkSteps += 1
            left = False
            right = True
        else:
            if right:
                win.blit(left_stand, (x, y))
            elif left:
                win.blit(right_stand, (x, y))

        if isJump:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1

            else:
                jumpCount = 10
                isJump = False

        if (y == 510) and (x >= 210 and x <= 250) and iscount == True:
            if keys[pygame.K_1]:
                Numbers.append(1)
            if keys[pygame.K_2]:
                Numbers.append(2)
            if keys[pygame.K_3]:
                Numbers.append(3)
            if keys[pygame.K_4]:
                Numbers.append(4)
            if keys[pygame.K_5]:
                Numbers.append(5)
            for i in Numbers:
                if i not in compare:
                    compare.append(i)
            if len(compare) == 5:
                if ans2 == compare:
                    islog = True
                    iscount = False
                    compare=[]
                    Numbers=[]
                else:
                    compare = []
                    Numbers = []
                    life -= 1
        if islog:
            log_disp()
        if islog == False and x > 330 and x < 550:
            y+=1.5
            if y==600:
                life -= 1
                x = 0
                y = 510
        if x > 80 and x < 110 and y == 510:
            win.blit(info_image, (0, -2))
        if (y == 510) and (x >= 210 and x <= 250):
            win.blit(background2, (-25, -1))
        if life == 0:
            x = p
            y = j
            win.blit(gameover, (200, 200))
            run = False
        if x==750 and y<=510 and y>=450:
            Level_2=False
            Level_3=True
            compare=[]
            Numbers=[]
            islog=False
            x=0
            y=510




    def log_displv3():
        win.blit(log, (345, 230))
        win.blit(log, (371, 270))
        win.blit(log, (396, 310))
        win.blit(log, (420, 350))
        win.blit(log, (445, 390))
        win.blit(log, (470, 430))
        win.blit(log, (495, 470))
        win.blit(log, (520, 510))
        win.blit(log, (545, 550))


    if Level_3:
        pygame.time.delay(5)
        background_items()
        lifedisp()
        win.blit(shark, (330, 550))

        iscount = True


        if walkSteps + 1 >= 27:
            walkSteps = 0

        if keys[pygame.K_UP]:
            isJump = True

        if keys[pygame.K_LEFT] and x > 0:
            x = x - vel
            win.blit(walkLeft[walkSteps // 3], (x, y))
            walkSteps += 1
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x <= 745:
            x = x + vel
            win.blit(walkRight[walkSteps // 3], (x, y))
            walkSteps += 1
            left = False
            right = True
        else:
            if right:
                win.blit(left_stand, (x, y))
            elif left:
                win.blit(right_stand, (x, y))

        if isJump:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1

            else:
                jumpCount = 10
                isJump = False
        if (y == 510) and (x >= 210 and x <= 250) and iscount == True:
            if keys[pygame.K_1]:
                Numbers.append(1)
            if keys[pygame.K_2]:
                Numbers.append(2)
            if keys[pygame.K_3]:
                Numbers.append(3)
            if keys[pygame.K_4]:
                Numbers.append(4)


            for i in Numbers:
                if i not in compare:
                    compare.append(i)

            if len(compare) == 4:
                print(compare)
                if compare == ans3:
                    islog = True
                    iscount = False
                    compare=[]
                    Numbers=[]
                else:
                    compare = []
                    Numbers = []
                    life -= 1
        if islog:
            log_disp()
        else:
            log_displv3()
        if islog == False and x > 330 and x < 550:
            y += 1.5
            if y == 600:
                life -= 1
                x = 0
                y = 510
        if x > 80 and x < 110 and y == 510:
            win.blit(ifinfo, (-14, -2))

        if (y == 510) and (x >= 210 and x <= 250):
            win.blit(background3, (-15, -1))
        if life == 0:
            x = p
            y = j
            win.blit(gameover, (200, 200))
            run = False
        if x == 750 and y <= 510 and y >= 450:
            Level_3 = False
            Level_4 = True
            x = 0
            y = 510
                    # LEVEL 3



    if Level_4:
        win.blit(bg_4, (0,0))
        win.blit(ground, (-25, 570))
        win.blit(ground, (0, 570))
        win.blit(ground, (320, 570))
        win.blit(ground, (150, 570))
        win.blit(ground, (380, 570))
        win.blit(ground, (550, 570))  # 150  and 550
        win.blit(ground, (600, 570))
        win.blit(life_heart, (745,535))
        if villan_run:
            villan_walk()
        if x==V_x and y==V_y:
            villan_run=False
        if x<800 and x>720 and y>500 and y<570:
            if life==3:
                pass
            else:
                life+=1




        if walkSteps + 1 >= 27:
            walkSteps = 0

        if keys[pygame.K_UP]:
            isJump = True

        if keys[pygame.K_LEFT] and x > 0:
            x = x - vel
            win.blit(walkLeft[walkSteps // 3], (x, y))
            walkSteps += 1
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x <= 745:
            x = x + vel
            win.blit(walkRight[walkSteps // 3], (x, y))
            walkSteps += 1
            left = False
            right = True
        else:
            if right:
                win.blit(left_stand, (x, y))
            elif left:
                win.blit(right_stand, (x, y))

        if isJump:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1

            else:
                jumpCount = 10
                isJump = False

        lifedisp()
        if x==750 and y==510:
            Level_4=False
            Level_5=True
            x=0
            y=510

        if life<=0:
            win.blit(gameover,(200,200))
            run=False

    if Level_5:
        pygame.time.delay(7)
        win.blit(bennett,(0,0))
        win.blit(ground, (-25, 570))
        win.blit(ground, (0, 570))
        win.blit(ground, (320, 570))
        win.blit(ground, (150, 570))
        win.blit(ground, (380, 570))
        win.blit(ground, (550, 570))  # 150  and 550
        win.blit(ground, (600, 570))
        win.blit(signboard,(380,518))
        win.blit(signboard,(200,518))
        if x>=185 and x<=210:
            win.blit(cuoriocity_question,(-25,0))

        if x>=365 and x<=385 and y==510:
            win.blit(q5,(0,0))
            if level_5_tick == True:
                win.blit(tick, (300, 200))
            if keys[pygame.K_1]:
                life-=1
            if keys[pygame.K_4]:
                life -= 1
            if keys[pygame.K_3]:
                life -= 1
            if keys[pygame.K_2] and x>=365 and x<=385 and y==510:
                level_5_tick=True

            if keys[pygame.K_5]:
                life -= 1
            if keys[pygame.K_6]:
                life -= 1
            if keys[pygame.K_7]:
                life -= 1
            if keys[pygame.K_8]:
                life -= 1
            if keys[pygame.K_9]:
                life -= 1


        if walkSteps + 1 >= 27:
            walkSteps = 0

        if keys[pygame.K_UP]:
            isJump = True

        if keys[pygame.K_LEFT] and x > 0:
            x = x - vel
            win.blit(walkLeft[walkSteps // 3], (x, y))
            walkSteps += 1
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x <= 745:
            x = x + vel
            win.blit(walkRight[walkSteps // 3], (x, y))
            walkSteps += 1
            left = False
            right = True
        else:
            if right:
                win.blit(left_stand, (x, y))
            elif left:
                win.blit(right_stand, (x, y))

        if isJump:
            if jumpCount >= -10:
                y -= (jumpCount * abs(jumpCount)) * 0.5
                jumpCount -= 1

            else:
                jumpCount = 10
                isJump = False
        if x==750 and y==510:
            Level_5=False
            Level_6=True
            x = 0
            y = 510


    if Level_6:
        win.blit(bg_6,(0,0))
        win.blit(ground, (-25, 570))
        win.blit(ground, (0, 570))
        win.blit(ground, (320, 570))
        win.blit(ground, (150, 570))
        win.blit(ground, (380, 570))
        win.blit(ground, (550, 570))  # 150  and 550
        win.blit(ground, (600, 570))
        zombie_hands()
        if rotate_left==True and rotate>= -5:
            rotate-=0.5
            if rotate==-5:
                rotate_left=False
                rotate_right=True
        if rotate_right==True and rotate<= 5:
            rotate+=0.5
            if rotate==5:
                rotate_right=False
                rotate_left=True


        if w_up==True and W_y>=250:
            W_y-=1
            if W_y==250:
                w_up=False
                w_down=True
        if w_down==True and W_y<=450:
            W_y+=1
            if W_y==450:
                w_down=False
                w_up=True

        image2=pygame.transform.rotozoom(witch,rotate,up)
        win.blit(image2,(W_x,W_y))

        if fly==False:
            if walkSteps + 1 >= 27:
                walkSteps = 0

            if keys[pygame.K_UP]:
                isJump = True

            if keys[pygame.K_LEFT] and x > 0:
                x = x - vel
                win.blit(walkLeft[walkSteps // 3], (x, y))
                walkSteps += 1
                left = True
                right = False
            elif keys[pygame.K_RIGHT] and x <= 745:
                x = x + vel
                win.blit(walkRight[walkSteps // 3], (x, y))
                walkSteps += 1
                left = False
                right = True
            else:
                if right:
                    win.blit(left_stand, (x, y))
                elif left:
                    win.blit(right_stand, (x, y))

            if isJump:
                if jumpCount >= -10:
                    y -= (jumpCount * abs(jumpCount)) * 0.5
                    jumpCount -= 1

                else:
                    jumpCount = 10
                    isJump = False

        if fly==False:
            lifedisp()
        if life<=0:
            run=False

        if x>=500 and x<=700 :
            fly=True
            win.blit(stand,(x,W_y))
            win.blit(thought, (x-150, W_y-150))

    pygame.display.update()

pygame.quit()