import pygame,sys,random,math,time
pygame.init()

#bộ màu
class color:
    red =(255,0,0)
    black = (0,0,0)
    white= (255,255,255)

#thuộc tính game
class main_game:
    def __init__(self):
        #thuộc tính cửa sổ mở
        self.width = 500 #chiều rộng
        self.height =800 #chiều dài
        self.color = color.white #màu nền
        self.name_game = "Game nao khong biet" #tên game

        #thuộc tính game
        self.play =False #tình trạng đang chơi hay tạm dừng
        self.num_FPS = 70 #FPS game khi chơi
        self.num_FPS_pause = 20 #FPS game khi tamj dừng
        self.time_create_obj = 500 # thời gian lúc đầu để tạo 1 obj
        self.r_mouse =35 # bán kính lại bỏ quanh chuột

        #khởi tạo kiểm soát trò chơi
        self.FPS = pygame.time.Clock() #khởi tạo bộ đếm time
        self.mouse = pygame.mouse.get_pos() #trả về vị trí chuột lúc đầu

        #quản lí điểm
        self.diem = 0 # điểm mặc định
        self.diem_h = 0 # khởi tạo điểm cao nhất lúc đầu
        self.dt_diem = 1 #độ tăng điêmt
game = main_game() #khởi tạo đối tượng thuộc tính game

#thuộc tính đối tượng chính (bảo vệ)
class main_object:
    def __init__(self,x,y,r,c): #bộ dữ liệu nhập gồm tọa độ x,y bán kính, màu sắc
        self.x =x 
        self.y =y
        self.color = c
        self.radius =r
m_obj= main_object(game.width*0.5,game.height*0.5,0.1*game.width,color.red) #khởi tạo

#thuộc tính địch 
class object_c:
    def __init__(self,center,w,s,di):# vị trí, bán kính, tốc độ, tâm hướng di chuyển tới
        self.w= w 
        self.center= center
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255)) #bộ ngầu nhiên màu sắc
        self.speed = s

        #hàm xác định độ dịch chuyển trục x,y {di..[0],di..[1]}
        #xác định vector hướng
        l_x = di[0]-center[0]
        l_y = di[1]-center[1]
        #xác định tỉ số của tốc độ với khoảng cách từ đó lấy tỉ lệ các hướng x,y tương ứng 
        # ví dụ: có vector là (x0,y0) thì kcach là a=sqrt(x0**2+y0**2), với vận tốc bằng v 
        #        thì ta có tỉ số độ dài dchuyen sẽ bằng v/a, áp dụng tam giác đồng dạng thì ta xác định được độ dịch chuyển x,y
        len = math.sqrt((l_x)**2+(l_y)**2)/s
        l_x /= len
        l_y /= len

        #thiết lập vector dịch chuyển 2D
        self.di= (l_x,l_y)

    #dịch chuyển theo vector dchuyen
    def move(self):        
        self.center=(self.center[0] +self.di[0],self.center[1] +self.di[1])#cộng vector

#khởi tạo biến điểm cao nhất từng đạt bằng cách đọc file
try:#chạy trong này
    with open("Highest_scores.txt","r") as file: #lấy open file gán vào biến file để thao tác
        text=file.read() #với cấu trúc:"{a} {b} {x}" với x là số điểm cần tìm
        text=text.split()
        game.diem_h =int(text[2])

except:#nếu bị lỗi thì chạy trong này
    #khởi tạo file text lưu điểm cao nhất
    with open("Highest_scores.txt","w") as file: #lấy open file gán vào biến file để thao tác
        file.write("Diem day 0")

list_object = []
view = pygame.display.set_mode((game.width,game.height))
pygame.display.set_caption(game.name_game)
font = pygame.font.Font('freesansbold.ttf', 32)
t_pause = font.render("PAUSE",True,color.black)
t_lost = font.render("YOU LOST",True, color.red)

def center_spon():
    di =random.randint(1,4)
    if di==1:
        return (10,random.randint(0,game.height))
    if di==2:
        return (random.randint(0,game.width),10)
    if di==3:
       return  (game.width-10,random.randint(0,game.height))
    return  (random.randint(0,game.width),game.height-10)

def when_touch_m (obj,where):
    global m_obj, game
    l_x = m_obj.x-obj.center[0]
    l_y = m_obj.y-obj.center[1]
    len = math.sqrt((l_x)**2+(l_y)**2)
    if len < obj.w + m_obj.radius:
        view.blit(t_lost,(100,100))
        pygame.display.update()
        if(game.diem>game.diem_h):
            with open("Highest_scores.txt","w") as file2:
                file2.write("diem day {0}".format(game.diem))
                game.diem_h=game.diem
        game.diem=0
        time.sleep(2)
        return True


def when_touch_mouse (obj,where):
    l_x = game.mouse[0]-obj.center[0]
    l_y = game.mouse[1]-obj.center[1]
    len = math.sqrt((l_x)**2+(l_y)**2)
    if len < obj.w + game.r_mouse:
        game.diem+=game.dt_diem
        list_object.remove(obj)
        return True

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
        game.FPS.tick(game.num_FPS_pause)

t_diem = font.render("Diem {0} - Highest {1}".format(game.diem,game.diem_h),True, color.red)
dk_de = True
dk_re = False
while True:

    game.play=pause(game.play)
    if pygame.time.get_ticks() % game.time_create_obj <50 and dk_de:
        list_object.append( object_c(center_spon(), random.randint(game.width*0.05,game.width*0.07), 0.01*game.width , (m_obj.x,m_obj.y)) )
        game.time_create_obj = random.randint(200,random.randint(1500,3000))
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
            elif get_k == ord('x'):
                pygame.quit()
                sys.exit()
        elif get == pygame.MOUSEBUTTONDOWN:
            pass
        game.mouse = pygame.mouse.get_pos()
    
    view.fill(game.color)    
    pygame.draw.circle(view,m_obj.color,(m_obj.x,m_obj.y),m_obj.radius)
    pygame.draw.circle(view,color.black,(game.mouse[0],game.mouse[1]),game.r_mouse)
    t_diem = font.render("Diem {0} - Highest {1}".format(game.diem,game.diem_h),True, color.red)

    view.blit(t_diem,(0,0))
    obj = len(list_object)
    while obj>0:
        obj-=1
        pygame.draw.circle(view,list_object[obj].color,list_object[obj].center,list_object[obj].w)
        list_object[obj].move()
        if when_touch_mouse(list_object[obj],obj)!=True:
            if when_touch_m(list_object[obj],obj):
                list_object = []
    game.FPS.tick(game.num_FPS)
    pygame.display.update()
