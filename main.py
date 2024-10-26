import pygame,sys,random,math
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
        self.FPS = pygame.time.Clock()
        self.num_FPS = 70
        self.time_create_obj = 500
game = main_game()

class main_object:
    def __init__(self,x,y,r,c):
        self.x =x
        self.y =y
        self.color = c
        self.radius =r

m_obj= main_object(game.width*0.5,game.height*0.5,0.1*game.width,color.red)

class object_c:
    def __init__(self,center,w,s,di):
        self.w= w 
        self.center= center
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))#color.black
        self.speed = s


        l_x = di[0]-center[0]
        l_y = di[1]-center[1]
        len = math.sqrt((l_x)**2+(l_y)**2)/s
        l_x /= len
        l_y /= len
        self.direction = (l_x,l_y)

    def move(self):        
        self.center=(self.center[0] +self.direction[0],self.center[1] +self.direction[1])


        

list_object = []
view = pygame.display.set_mode((game.width,game.height))


font = pygame.font.Font('freesansbold.ttf', 32)
t_pause = font.render("PAUSE",True,color.black)

def center_spon():
    di =random.randint(1,4)
    if di==1:
        return (10,random.randint(0,game.height))
    if di==2:
        return (random.randint(0,game.width),10)
    if di==3:
       return  (game.width-10,random.randint(0,game.height))
    return  (random.randint(0,game.width),game.height-10)

def pause(key):
    while key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print("continue")
                return False
        view.blit(t_pause,(0,0))
        pygame.display.update()
        game.FPS.tick(20)

dk_de = True
while True:
    game.play=pause(game.play)

    if pygame.time.get_ticks() % game.time_create_obj <50 and dk_de:
        list_object.append( object_c(center_spon(), random.randint(game.width*0.05,game.width*0.07), 0.01*game.width , (m_obj.x,m_obj.y)) )
        game.time_create_obj = random.randint(200,5000)
        dk_de = False
    elif pygame.time.get_ticks() % game.time_create_obj >50 and dk_de==False:
        dk_de=True

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
        elif get == pygame.MOUSEBUTTONDOWN:
            pass
    view.fill(game.color)

    for obj in list_object:
        pygame.draw.circle(view,obj.color,obj.center,obj.w)
        obj.move()
    pygame.draw.circle(view,m_obj.color,(m_obj.x,m_obj.y),m_obj.radius)
    print(len(list_object))
    game.FPS.tick(game.num_FPS)
    pygame.display.update()
