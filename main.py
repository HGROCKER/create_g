import pygame,sys,random
pygame.init()

class main_game:
    def __init__(self):
        self.width = 500
        self.height =800
        self.color = (255,255,255)
        self.play =False
        self.time = pygame.time.Clock()
game = main_game()

class object_c:
    def __init__(self,x,y,w):
        self.w= w 
        self.x = x
        self.y = y
        self.color = (0,0,0)

view = pygame.display.set_mode((game.width,game.height))

def pause(key):
    while key:
        game.time.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print("continue")
                return False
while True:
    game.play=pause(game.play)
    for event in pygame.event.get():
        get = event.type
        if get == pygame.QUIT :
            pygame.quit()
            sys.exit()
        elif get == pygame.KEYDOWN:
            game.play=False
            get_k = event.key
            if get_k == ord(' '):
                game.play = True
                print("pause")
    view.fill(game.color)
    pygame.display.update()
                
