#khời tạo modun phục vụ
import pygame,sys,random,math
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
        self.time_delay_lost = 1000 # thời gian tạm dừng khi thua
        self.time = pygame.time.get_ticks()
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

#khởi tạo bộ dữ liệu game
list_object = [] #các đối tượng địch
view = pygame.display.set_mode((game.width,game.height)) #màn hình
pygame.display.set_caption(game.name_game) #tên game
font = pygame.font.Font('freesansbold.ttf', 32) #font chữ
t_pause = font.render("PAUSE",True,color.black) #chữ khi pause
t_lost = font.render("YOU LOST",True, color.red) #chữ khi lost
t_diem = font.render("Diem {0} - Highest {1}".format(game.diem,game.diem_h),True, color.red)
dk_re = False

#tạo vị trí ngẫu nhiên ở các viền
def center_spon():
    di =random.randint(1,4)
    if di==1:
        return (10,random.randint(0,game.height))
    if di==2:
        return (random.randint(0,game.width),10)
    if di==3:
       return  (game.width-10,random.randint(0,game.height))
    return  (random.randint(0,game.width),game.height-10)

#xác định va chạm giữa cần bảo vệ và địch
def when_touch_m (obj):
    #xác định khoảng cách
    l_x = m_obj.x-obj.center[0]
    l_y = m_obj.y-obj.center[1]
    len = math.sqrt((l_x)**2+(l_y)**2)

    #điều kiện va chạm và thao tác
    if len < obj.w + m_obj.radius:
        # in chữ lost
        view.blit(t_lost,(100,100))
        #update chữ lost lên hình
        pygame.display.update()
        #xác định điểm cao nhất
        if(game.diem>game.diem_h):
            with open("Highest_scores.txt","w") as file2:
                file2.write("diem day {0}".format(game.diem))
                game.diem_h=game.diem
        #reset điểm và trả lại giá trị True để thực hiện tác vụ sau nó
        game.diem=0
        pygame.time.delay(game.time_delay_lost)
        return True


def when_touch_mouse (obj,where):
    #xd kcach
    l_x = game.mouse[0]-obj.center[0]
    l_y = game.mouse[1]-obj.center[1]
    len = math.sqrt((l_x)**2+(l_y)**2)

    #xd va cham và xóa đối tượng đó {để hiểu rõ hơn có thể tìm hiêu về phạm vi biến và  cách lấy dữ liệu của các function}
    if len < obj.w + game.r_mouse:
        game.diem+=game.dt_diem
        list_object.pop(where)
        return True

#hoạt họa khi pause
def pause(key):
    while key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                game.play=False
                print("continue")
                return False
        view.blit(t_pause,(0,0))
        pygame.display.update()
        game.FPS.tick(game.num_FPS_pause)

while True:
    game.play=pause(game.play)
    #xd khoảng time spon địch
    #vì time vẫn là giá trị tương đối nên không thể đặt điều kiện tuyệt đối
    #việc này có thể thực hiện bằng cách xác định khoảng time giữa 2 lần spon bằng cách xác định time ở 2 thời điểm đó để spon
    #ví dụ khi kcach time >1000 thì spon và set time hiện tại làm mốc
    #còn nếu hỏi vid sao tui không dùng cách này thì do mình thích tìm hiểu cách mới hơn
    if pygame.time.get_ticks() -game.time > game.time_create_obj :
        list_object.append( object_c(center_spon(), random.randint(game.width*0.05,game.width*0.07), 0.01*game.width , (m_obj.x,m_obj.y)) )
        game.time_create_obj = random.randint(100,random.randint(1000,3000))
        game.time = pygame.time.get_ticks()
    # lấy tọa độ chuột
    game.mouse = pygame.mouse.get_pos()
    #chọ này đơn giản khỏi gthich
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.play = True
                print("pause") 
    #khởi tạo các đối tượng để in
    view.fill(game.color)    
    pygame.draw.circle(view,m_obj.color,(m_obj.x,m_obj.y),m_obj.radius)
    pygame.draw.circle(view,color.black,(game.mouse[0],game.mouse[1]),game.r_mouse)
    t_diem = font.render("Diem {0} - Highest {1}".format(game.diem,game.diem_h),True, color.red)
    view.blit(t_diem,(0,0))
    #xử lý sự tương tác và tồn tại của các đối tượng
    obj = len(list_object)
    while obj>0:
        obj-=1
        ten =font.render(str(obj),True,color.black)
        pygame.draw.circle(view,list_object[obj].color,list_object[obj].center,list_object[obj].w)
        list_object[obj].move()
        view.blit(ten,list_object[obj].center)
        if when_touch_m(list_object[obj]):
            list_object.clear()
            break
        when_touch_mouse(list_object[obj],obj)
    #lim time in 1s (ý là sẽ sấp xỉ đâu đó thôi)
    game.FPS.tick(game.num_FPS)
    #in hết lên màn hình
    pygame.display.update()
