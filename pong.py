import pygame
import random

WIDTH = 800
HEIGHT = 600
#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#initialize window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
done = False
clock = pygame.time.Clock()

def paddle_1():
    pygame.draw.line(screen, GREEN, [paddle_x, paddle_y_top], [paddle_x, paddle_y_bottom], 10)

def paddle_2():
    pygame.draw.line(screen, BLUE, [paddle2_x, paddle2_y_top], [paddle2_x, paddle2_y_bottom], 10)

font_name = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surf, text_rect)

def show_go_screen():
    draw_text(screen, "Apple Tennis!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "P1(green): Q:up A:down P2(blue): Up:up Down:down ", 22, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Press any key to begin game. ", 18, WIDTH /2, HEIGHT * 3/4)
    pygame.display.update()
    waiting = True
    while waiting: 
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
                
def ball():
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius, 0)
    
game_over = True    
#gameloop
while not done:
    if game_over:
        show_go_screen()
        game_over = False
        ball_x = 400
        ball_y = 300
        ball_radius = 20
        ball_mvmnt_x = 0
        ball_mvmnt_y = 0
        paddle_x = 1
        paddle2_x = 794
        paddle_y_top = 260
        paddle_y_bottom = 340
        paddle2_y_top = 260
        paddle2_y_bottom = 340

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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    ball()
    paddle_1()
    paddle_2()
    clock.tick(60)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if paddle2_y_top > 0:
            paddle2_y_top -= 10
            paddle2_y_bottom -= 10
    if pressed[pygame.K_DOWN]:
        if paddle2_y_bottom < 600:
            paddle2_y_top += 10
            paddle2_y_bottom += 10
    if pressed[pygame.K_q]:
        if paddle_y_top > 0:
            paddle_y_top -= 10
            paddle_y_bottom -= 10
    if pressed[pygame.K_a]:
        if paddle_y_bottom < 600:
            paddle_y_top += 10
            paddle_y_bottom += 10
    
    ball_x += ball_mvmnt_x
    ball_y += ball_mvmnt_y

    paddle_top = range(paddle_y_top, paddle_y_top + 1)
    paddle_bottom = range(paddle_y_bottom, paddle_y_bottom - 1)
    paddle2_top = range(paddle2_y_top, paddle2_y_top + 1)
    paddle2_bottom = range(paddle2_y_bottom, paddle2_y_bottom -1)  
    #right wall logic
    if ball_x + ball_radius == WIDTH +20 :
        if ball_y <= paddle2_y_bottom and ball_y >= paddle2_y_top:
            if ball_y not in paddle2_top and ball_y not in paddle2_bottom:
                options = random.randint(1, 2)
                if options == 1:
                    ball_mvmnt_y += random.randint(1, 7)
                    ball_mvmnt_x = -ball_mvmnt_x
                else:
                    ball_mvmnt_y -= random.randint(1, 7)
                    ball_mvmnt_x = -ball_mvmnt_x
            else: 
                ball_mvmnt_x = -ball_mvmnt_x
        else:
            game_over = True             
    #floor logic
    if ball_y + ball_radius > HEIGHT:
        ball_mvmnt_y = -ball_mvmnt_y
    #ceiling logic
    if ball_y - ball_radius < 0:
        ball_mvmnt_y = -ball_mvmnt_y    
    #left wall logic
    if ball_x - ball_radius == -20: 
        if  ball_y <= paddle_y_bottom and ball_y >= paddle_y_top:
            if ball_y not in paddle_top and ball_y not in paddle_bottom:
                options = random.randint(1, 2)
                if options == 1:
                    ball_mvmnt_y += random.randint(1, 7)
                    ball_mvmnt_x = -ball_mvmnt_x
                else:
                    ball_mvmnt_y -= random.randint(1, 7)
                    ball_mvmnt_x = -ball_mvmnt_x
            else:
                ball_mvmnt_x = -ball_mvmnt_x
        
        else:
            game_over = True
              
    pygame.display.update()

pygame.quit()


