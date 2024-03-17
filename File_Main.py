import matplotlib.pyplot as plt
#hoang khanh
#thienphuc

#Vẽ nét đứt
def draw_net_dut(count0, count1, count0_max, count1_max, X, Y, x, y):
    if count0!=count0_max:
       plt.plot([X,x],[Y,y], linestyle='solid', color='c')
       count0+=1
    elif count1!=count1_max:
        plt.plot([X,x],[Y,y], linestyle='none')
        count1+=1
    else:
        count0=0
        count1=0
    return count0, count1

#Vẽ nét gạch 1 chấm
def draw_1_cham_gach(count0, count1, count2, count0_max, count1_max, count2_max, X, Y, x, y):
    if count0!=count0_max:
        plt.plot([X,x],[Y,y], linestyle='solid', color='c')
        count0+=1
    elif count1!=count1_max:
        plt.plot([X,x],[Y,y], linestyle='none')
        count1+=1
    elif count2!=count2_max:
        plt.plot([X,x],[Y,y], linestyle='solid', color='c')
        count2+=1
        if count2==count2_max:
            count1=0
    else:
        count0=0
        count1=0
        count2=0
    return count0, count1, count2

#Vẽ nét gạch 2 chấm
def draw_2_cham_gach(count0, count1, count2, count3, count0_max, count1_max, count2_max, count3_max, X, Y, x, y):
    if count0!=count0_max:
        plt.plot([X,x],[Y,y], linestyle='solid', color='c')
        count0+=1
    elif count1!=count1_max:
        plt.plot([X,x],[Y,y], linestyle='none')
        count1+=1
    elif count2!=count2_max:
        plt.plot([X,x],[Y,y], linestyle='solid', color='c')
        count2+=1
        if count3==count3_max and count2==count2_max:
            count1=0
    elif count3!=count3_max:
        plt.plot([X,x],[Y,y], linestyle='none')
        count3+=1
        if count3==count3_max:
            count2=0
    else:
        count0=0
        count1=0
        count2=0
        count3=0
    return count0, count1, count2, count3

#Hàm chính, nhập các giá trị độ dài tại đây (từ tọa độ 2 điểm ban đầu), tính toán vị trí để putpixel
def draw(x1,y1,x2,y2,choice):
    Dx = abs(x2 - x1)
    Dy = abs(y2 - y1)
    
    if choice==1: # ---_---_---
        count0, count1 = 0 , 0
        count0_max, count1_max= 3 , 1 
    elif choice==2: # -----___-___-----
        count0, count1, count2 = 0 , 0 , 0
        count0_max, count1_max, count2_max= 5 , 3 , 1
    elif choice==3: # -------____-__-____-------
        count0, count1, count2, count3 = 0, 0, 0, 0
        count0_max, count1_max, count2_max, count3_max= 7 , 4 , 1, 2
    
#Xác định hướng vẽ
    if(y1<y2):
        y_change=+1
    else:
        y_change=-1
    if(x1<x2):
        x_change=1
    else:
        x_change=-1
    
    # x,y là hai biến tạm, dùng trong quá trình putpixel
    x,y=x1,y1
    
    if (Dx>=Dy):
        p  = 2*Dy -   Dx
        D1 = 2*Dy - 2*Dx
        D2 = 2*Dy
            
        while x != x2:
            X,Y=x,y
            if p > 0:
                p += D1
                y+=y_change
            else:
               p += D2
            x+=x_change
            #----___----
            if choice==0:
                plt.plot([X,x],[Y,y], linestyle='solid', color='c')
            elif choice==1: #Chọn vẽ nét đứt
                count0, count1 = draw_net_dut(count0, count1,count0_max, count1_max, X, Y, x, y)
            elif choice==2: #Chọn vẽ nét gạch chấm
                count0, count1, count2 = draw_1_cham_gach(count0, count1, count2, count0_max, count1_max, count2_max, X, Y, x, y)
            elif choice==3: #Chọn vẽ nét gạch hai chấm
                count0, count1, count2, count3 = draw_2_cham_gach(count0, count1, count2, count3, count0_max, count1_max, count2_max, 
count3_max, X, Y, x, y)
            
    else:
        p  = 2*Dx -   Dy
        D1 = 2*Dx - 2*Dy
        D2 = 2*Dx
        
        while y!=y2:
            X,Y=x,y
            if p > 0:
                p += D1
                x+=x_change
            else:
                p+= D2
            y+=y_change
            
            if choice==0:
                plt.plot([X,x],[Y,y], linestyle='solid', color='c')
            elif choice==1: #Chọn vẽ nét đứt
                count0, count1 = draw_net_dut(count0, count1,count0_max, count1_max, X, Y, x, y)
            elif choice==2: #Chọn vẽ nét gạch chấm
                count0, count1, count2 = draw_1_cham_gach(count0, count1, count2, count0_max, count1_max, count2_max, X, Y, x, y)
            elif choice==3: #Chọn vẽ nét gạch hai chấm
                count0, count1, count2, count3 = draw_2_cham_gach(count0, count1, count2, count3, count0_max, count1_max, count2_max, count3_max, X, Y, x, y)
    if choice!=0:
        #Chấm 2 chấm tại điểm đầu và cuối
        plt.plot(x1,y1, marker='o', color='r')
        plt.plot(x2,y2, marker='o',color='b')            

#Hàm vẽ HCN
def draw_rect(x1,y1,x2,y2):
    if x1 > x2:
        swap_x, swap_y=x1, y1
        x1,y1=x2,y2
        x2,y2=swap_x,swap_y
    
    x,y=x1,y1
    H=y1-y2
    
    while x!=x2:
        plt.plot([x,x],[y,y+H], linestyle='solid', color='b')
        plt.plot([x,x+1],[y,y], linestyle='solid', color='c')
        plt.plot([x,x+1],[y+H,y+H], linestyle='solid', color='c')
        x+=1
    plt.plot([x1,x1],[y,y+H], linestyle='solid', color='c')
    plt.plot([x2,x2],[y,y+H], linestyle='solid', color='c')
    
    
#Hàm trung chuyển giữa vẽ đường thẳng và chữ nhật
def Input_draw(x1,y1,x2,y2, choice):
    if choice < 4:
        draw(x1,y1,x2,y2,choice)
    elif choice == 4:
        print('here1')
        draw_rect(x1,y1,x2,y2)
           
def axis(ax, x1, y1, x2, y2):
    line = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    if x1 < x2:
        xi = 1
    else:
        xi = -1

    if y1 < y2:
        yi = 1
    else:
        yi = -1

    x = x1
    y = y1

    line.append((x, y))

    if dx > dy:
        ai = (dy - dx) * 2
        bi = dy * 2
        p = bi - dx

        while x != x2:
            if p >= 0:
                x += xi
                y += yi
                p += ai
            else:
                p += bi
                x += xi

            line.append((x, y))
    else:
        ai = (dx - dy) * 2
        bi = dx * 2
        p = bi - dy

        while y != y2:
            if p >= 0:
                x += xi
                y += yi
                p += ai
            else:
                p += bi
                y += yi

            line.append((x, y))

    x_values, y_values = zip(*line)
    ax.plot(x_values, y_values, color='black', linestyle='-', linewidth=2)

# Thiết lập kích thước của hình vẽ
fig, ax = plt.subplots(figsize=(9, 9))
ax.set_box_aspect(aspect=1)

# Vẽ lưới
ax.grid(True, linestyle='--', alpha=0.7)


plt.grid(True)
plt.title('Hệ tọa độ 2D')

def get_user_input():
    x1, y1 = -200, -100
    x2, y2 = 100, -100
    return x1, y1, x2, y2
# Get user input
user_input = get_user_input()
choice=2
Input_draw(*user_input, choice)
# 1. Vẽ đường thẳng nét đứt
# 2. Vẽ đường thẳng nét gạch chấm
# 3. Vẽ đường thẳng nét gạch hai chấm
# 4. Vẽ HCN

axis_x=(max(abs(user_input[0]),abs(user_input[2])))
axis_y=(max(abs(user_input[1]),abs(user_input[3])))

axis_x_max, axis_x_min=min(-10,int(-1.3*axis_x)), max(10,int(1.3*axis_x))
axis_y_max, axis_y_min=min(-10,int(-1.3*axis_y)), max(10,int(1.3*axis_y))
axis(ax, axis_x_min, 0, axis_x_max, 0)  # Trục X
axis(ax, 0, axis_y_min, 0, axis_y_max)  # Trục Y    
plt.show()

