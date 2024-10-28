import pygame
import sys
import math,random
# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Màu sắc
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Đối tượng main
d=0
rect_x = 50
rect_y = 50
rect_width = 50
rect_height = 50
xspeed = 5
player_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
font = pygame.font.Font('freesansbold.ttf', 32)
stop=True

# Tọa độ mục tiêu
rect2_x =400
rect2_y =300
rect2_width = 50
rect2_height = 50
target_rect = pygame.Rect(rect2_x, rect2_y, rect2_width, rect2_height)
end= False

# Vòng lặp chính
pause=True
while True:
    t_pause = font.render("DIEM:{0}-({1};{2})".format(d,player_rect.x,player_rect.y),True,(0,0,0))
    pausegame = font.render("PAUSE",True,(0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                screen.blit(pausegame,(600,0))
                pygame.display.flip()
                pause= False
            if event.key == pygame.K_r:
                pause = True
    if pause==False: 
        pass
    if pause==True:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[ord('a')]:
            player_rect.x -= xspeed
          
        if keys[pygame.K_RIGHT] or keys[ord('d')]:
            player_rect.x += xspeed
        if keys[pygame.K_UP] or keys[ord('w')]:
            player_rect.y -= xspeed
        if keys[pygame.K_DOWN] or keys[ord('s')]:
            player_rect.y += xspeed
        if player_rect.x <-50 :
            player_rect = pygame.Rect(player_rect.x + 900, player_rect.y, rect_width, rect_height)
        elif player_rect.x >850 :
            player_rect = pygame.Rect(player_rect.x - 900, player_rect.y, rect_width, rect_height)
        if player_rect.y <-50:
            player_rect = pygame.Rect(player_rect.x, player_rect.y + 700, rect_width, rect_height)
        elif player_rect.y >650:
            player_rect = pygame.Rect(player_rect.x, player_rect.y - 700, rect_width, rect_height)
    # Kiểm tra va chạm
        if player_rect.colliderect(target_rect):
            d=d+1
            if xspeed<10:
                xspeed+=0.1
            rect2_x=random.randint(25,775)
            rect2_y=random.randint(25,575)
            target_rect = pygame.Rect(rect2_x, rect2_y, 50, 50)
    # Vlại màn hình
        screen.fill(white)
        pygame.draw.rect(screen, blue, player_rect)  # Đối tượng
        pygame.draw.rect(screen, red, target_rect)    # Mục tiêu
        screen.blit(t_pause,(50,0))
        pygame.display.flip()
    # Giới hạn tốc độ khung hình
    pygame.time.Clock().tick(60)

