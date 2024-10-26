import pygame,sys,random,time
pygame.init()

class color:
    red =(255,0,0)
    black = (0,0,0)
    white= (255,255,255)

class main_game:
    def __init__(self):
        self.width = 500
        self.height =800
        self.color = color.white
        self.play =False
        self.time = pygame.time.Clock()
game = main_game()

class main_object:
    def __init__(self,x,y,r,c):
        self.x =x
        self.y =y
        self.color = c
        self.radius =r

m_obj= main_object(game.width*0.5,game.height*0.5,0.2*game.height,color.black)

class object_c:
    def __init__(self,x,y,w,s,di):
        self.w= w 
        self.x = x
        self.y = y
        self.color = color.black
        self.speed = s
        self.direction = di
    def move(self):
        pass
list_object = []
list_object.append(object_c(random.randint(0,game.width), random.randint(0,game.height), random.randint(game.width*0.1,game.width*0.2),0.1*game.width, (m_obj.x,m_obj.y)))

view = pygame.display.set_mode((game.width,game.height))


font = pygame.font.Font('freesansbold.ttf', 32)
t_pause = font.render("PAUSE",True,color.black)
 
def pause(key):
    while key:
        list_object.append(object_c(random.randint(0,game.width), random.randint(0,game.height), random.randint(game.width*0.1,game.width*0.2),0.1*game.width, (m_obj.x,m_obj.y)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print("continue")
                return False
        view.blit(t_pause,(0,0))
        pygame.display.update()
        game.time.tick(20)

while True:
    game.play=pause(game.play)
    # list_object.append(object_c(random.randint(0,game.width), random.randint(0,game.height), random.randint(game.width*0.1,game.width*0.2),0.1*game.width, (m_obj.x,m_obj.y)))

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
    # for obj in list_object:
    #     view.blit(pygame.draw.circle(obj.))
    pygame.display.update()
