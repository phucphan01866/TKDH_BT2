import matplotlib.pyplot as plt
#hoang khanh
#thienphuc


                
                
def draw_line_2(x,y,x1,y1,x2,y2,Dx,Dy,D1,D2,d):
    count0, count1 = 0 , 0
    count0_max, count1_max= 3 , 1
    if (Dx>Dy):
        while x < x2:
            X,Y=x,y
            if d < 0:
                d += D1
                if(y1>y2):
                    y-=1
                else:
                    y+=1
            else:
                d += D2
            x+=1
            if count0!=count0_max:
                plt.plot([X,x],[Y,y], linestyle='solid', color='c')
                count0+=1
            elif count1!=count1_max:
                plt.plot([X,x],[Y,y], linestyle='none')
                count1+=1
            else:
                count0=0
                count1=0
    else:
        while y < y2:
            X,Y=x,y
            if d < 0:
                d += D1
                if(x1>x2):
                    x-=1
                else:
                    x+=1
            else:
                d += D2
            y+=1
            if count0!=count0_max:
                plt.plot([X,x],[Y,y], linestyle='solid', color='c')
                count0+=1
            elif count1!=count1_max:
                plt.plot([X,x],[Y,y], linestyle='none')
                count1+=1
            else:
                count0=0
                count1=0

def draw_line_3(x,y,x1,y1,x2,y2,Dx,Dy,D1,D2,d):
    count0, count1, count2 = 0 , 0 , 0
    count0_max, count1_max, count2_max= 3 , 1 , 1
    
    if (Dx>Dy):
        while x < x2:
            X,Y=x,y
            if d < 0:
                d += D1
                if(y1>y2):
                    y-=1
                else:
                    y+=1
            else:
                d += D2
            x+=1
            if count0!=count0_max:
                plt.plot([X,x],[Y,y], linestyle='solid', color='c')
                count0+=1
            elif count1!=count1_max:
                plt.plot([X,x],[Y,y], linestyle='none')
                count1+=1
            elif count2!=count2_max:
                plt.plot([X,x],[Y,y], linestyle='solid', color='c')
                count2+=1
                count1=0
            else:
                count0=0
                count1=0
                count2=0
    else:
        while y < y2:
            X,Y=x,y
            if d < 0:
                d += D1
                if(x1>x2):
                    x-=1
                else:
                    x+=1
            else:
                d += D2
            y+=1
            if count0!=count0_max:
                plt.plot([X,x],[Y,y], linestyle='solid', color='c')
                count0+=1
            elif count1!=count1_max:
                plt.plot([X,x],[Y,y], linestyle='none')
                count1+=1
            elif count2!=count2_max:
                plt.plot([X,x],[Y,y], linestyle='solid', color='b')
                count2+=1
                count1=0
            else:
                count0=0
                count1=0
                count2=0


def draw_line_1(x1,y1,x2,y2,Dx,Dy,D1,D2,d):
    x,y=x1,y1
    print("Hai điểm được nhập vào là: " + str(x1) + "," + str(y1) + " và " + str(x2) + "," + str(y2))
    
    if (Dx>Dy):
        Dx = x2 - x1
        Dy = y2 - y1
        d  = 2*Dy -   Dx
        D1 = 2*Dy - 2*Dx 
        D2 = 2*Dy
        while x < x2:
            X,Y=x,y
            if d > 0:
                d += D1
                if(y1>y2):
                    y-=1
                else:
                    y+=1
            else:
                d += D2
            x+=1
            plt.plot([X,x],[Y,y], linestyle='solid', color='c')
    else:
        Dx = x2 - x1
        Dy = y2 - y1
        d  = 2*Dx -   Dy
        D1 = 2*Dx - 2*Dy 
        D2 = 2*Dx
        while y < y2:
            
            X,Y=x,y
            if d < 0:
                d += D2               
            else:
                d += D1
                if(x1>x2):
                    x-=1
                else:
                    x+=1
            y+=1
            plt.plot([X,x],[Y,y], linestyle='solid', color='c')

def line1(x1, y1, x2, y2):
    
    if(x1>x2):
        x_swap, y_swap=x1,y1
        x1,y1=x2,y2
        x2,y2=x_swap,y_swap
    
    Dx = x2 - x1
    Dy = y2 - y1
    d  = 2*Dy -   Dx
    D1 = 2*Dy - 2*Dx 
    D2 = 2*Dy

    print("D:" +str(D1))
    print("D:" +str(D2))
    print("D:" +str(d))


    draw_line_1(x1,y1,x2,y2,Dx,Dy,D1,D2,d)
                
    plt.plot(x1,y1, marker='o', color='c')
    plt.plot(x2,y2, marker='o',color='c')
    
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
        d = bi - dx

        while x != x2:
            if d >= 0:
                x += xi
                y += yi
                d += ai
            else:
                d += bi
                x += xi

            line.append((x, y))
    else:
        ai = (dx - dy) * 2
        bi = dx * 2
        d = bi - dy

        while y != y2:
            if d >= 0:
                x += xi
                y += yi
                d += ai
            else:
                d += bi
                y += yi

            line.append((x, y))

    x_values, y_values = zip(*line)
    ax.plot(x_values, y_values, color='black', linestyle='-', linewidth=2)

# Thiết lập kích thước của hình vẽ
fig, ax = plt.subplots(figsize=(10, 10))


# Vẽ lưới
ax.grid(True, linestyle='--', alpha=0.7)


plt.grid(True)
plt.title('Hệ tọa độ 2D')


def get_user_input():
    x1, y1 = 0 , 0
    x2, y2 = 100, 200
    return x1, y1, x2, y2
# Get user input
user_input = get_user_input()

axis(ax, int(-1.3*(max(user_input[0],user_input[2]))), 0, int(1.3*(max(user_input[0],user_input[2]))), 0)  # Trục X
axis(ax, 0, int(-1.3*(max(user_input[1],user_input[3]))), 0, int(1.3*(max(user_input[1],user_input[3]))))  # Trục Y

line1(*user_input)
plt.show()

