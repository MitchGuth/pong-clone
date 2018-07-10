import pygame
import random

def you_lose():
    print "You have lost the game, good luck next time. "

def game():
    arena_width = 800
    arena_height = 600
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    done = False
    clock = pygame.time.Clock()

    ball_x = 400
    ball_y = 300
    ball_radius = 20
    ball_mvmnt_x = 0
    ball_mvmnt_y = 0
    paddle_x = 1
    paddle_y_top = 340
    paddle_y_bottom = 260
    
    def paddle_1():

        pygame.draw.line(screen, (0,255, 0), [paddle_x, paddle_y_top], [paddle_x, paddle_y_bottom], 10)

    tipoff = random.randint(1, 6)
    if tipoff == 1:
        ball_mvmnt_x += 10
        ball_mvmnt_y += 10
    elif tipoff == 2:
        ball_mvmnt_x += ball_mvmnt_x - 10
        ball_mvmnt_y += ball_mvmnt_y - 10
    elif tipoff == 3:
        ball_mvmnt_x += 10
    elif tipoff == 4: 
        ball_mvmnt_x += ball_mvmnt_x - 10
    elif tipoff == 5: 
        ball_mvmnt_x += 10
        ball_mvmnt_y += ball_mvmnt_y - 10
    elif tipoff == 6:
        ball_mvmnt_x += ball_mvmnt_x - 10
        ball_mvmnt_y += 10

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius, 0)
        paddle_1()
        pygame.display.update()
        clock.tick(60)


        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            paddle_y_top -= 10
            paddle_y_bottom -= 10
        if pressed[pygame.K_DOWN]:
            paddle_y_top += 10
            paddle_y_bottom += 10
        
        ball_x += ball_mvmnt_x
        ball_y += ball_mvmnt_y

        if ball_x + ball_radius > arena_width:
            ball_mvmnt_x = -ball_mvmnt_x
        if ball_y + ball_radius > arena_height:
            ball_mvmnt_y = -ball_mvmnt_y
        if ball_x == paddle_x and ball_y - ball_radius>= paddle_y_bottom and ball_y - ball_radius <= paddle_y_top :
            ball_mvmnt_x = -ball_mvmnt_x 
        if ball_y - ball_radius < 0:
            ball_mvmnt_y = -ball_mvmnt_y
        if ball_x - ball_radius < 0: 
            if  ball_y <= paddle_y_top and ball_y >= paddle_y_bottom:
                ball_mvmnt_x = -ball_mvmnt_x
            #define middle and then adjust y mvmnt based on middle  
            else:
                you_lose()
                break
        # if ball_x - ball_radius == paddle_x and ball_y <= paddle_y_top and ball_y >= paddle_y_bottom:
        #      ball_mvmnt_x = -ball_mvmnt_x
        # elif ball_x - ball_radius < 0 and ball_y > paddle_y_top and ball_y < paddle_y_bottom :
        #     you_lose()
        #     break
        

pygame.quit()

game()