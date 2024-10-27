import pygame,random,sys,math
pygame.init()

class game_main:
    def __init__(self):
        self.width = 500
        self.height = 800
        self.m_color = (255,255,255)
        self.name_game = "di_chuyen_toi_chuot"
        self.mouse = (0,0)
        self.st_obj = 0
        self.time = pygame.time.get_ticks()
        self.time_spon = 10
        self.FPS = pygame.time.Clock()
        self.num_FPS = 120
game = game_main() 

def center_spon():
    di =random.randint(1,4)
    if di==1:
        return (10,random.randint(0,game.height))
    if di==2:
        return (random.randint(0,game.width),10)
    if di==3:
       return  (game.width-10,random.randint(0,game.height))
    return  (random.randint(0,game.width),game.height-10)

class object:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.m_color = (0,0,0)
        self.name_game = "object_{0}".format(game.st_obj);game.st_obj +=1
        self.center = center_spon()
        self.speed = random.randint(1,10)
    def move(self,di):
        l_x = di[0]-self.center[0]
        l_y = di[1]-self.center[1]
        len = math.sqrt((l_x)**2+(l_y)**2)/self.speed
        if len>0.5:
            l_x /= len
            l_y /= len
            self.center = (self.center[0]+l_x,self.center[1]+l_y)

list_obj = []

view = pygame.display.set_mode((game.width,game.height))
pygame.display.set_caption(game.name_game)

while True:
    for event  in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            sys.exit()
    game.mouse = pygame.mouse.get_pos()

    if pygame.time.get_ticks() - game.time >game.time_spon:
        list_obj.append(object())
        game.time = pygame.time.get_ticks()
    view.fill((255,255,255))
    print(len(list_obj))
    for obj in list_obj:
        pygame.draw.rect(view,obj.m_color,(obj.center[0],obj.center[1],obj.width,obj.height))
        obj.move(game.mouse)

    game.FPS.tick(game.num_FPS)
    pygame.display.update()
