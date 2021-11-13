from ursina import *
import numpy as np

app = Ursina()

w, h = 20, 20

# 창 설정
window.borderless = False
window.color = color._50

# 카메라 설정
camera.orthographic = True      # 2D
camera.fov = 23
camera.position = (w//2, h//2)

Entity(model=Grid(w+1, h+1), scale=w+1, color=color.black, x=w//2-0.5, y=h//2-0.5, z=0.1)
map_size = 20
Omok_map = np.zeros([map_size, map_size])

row = 0 
col = 0
down_Diagonal = 0 
up_Diagonal = 0
fin = 0

def is_num(x, y, num):
    if Omok_map[x][y] != num:
        return False
    else:
        return True
    
def game_over(i, j, num):
    global fin
    fin = num


def rule_chek(i, j, num, row, col, down_Diagonal, up_Diagonal):

    for k in range(5):
        if is_num(i, j + k, num) == False:
            break
        else:
            row = row + 1

    for k in range(5):
        if is_num(i + k, j, num) == False:
            break
        else:
            col = col + 1

    for k in range(5):
        if is_num(i + k, j + k, num) == False:
            break
        else:
            down_Diagonal = down_Diagonal + 1

    for k in range(5):
        if is_num(i - k, j + k, num) == False:
            break
        else:
            up_Diagonal = up_Diagonal + 1

    
    if row == 5 or col == 5 or down_Diagonal == 5 or up_Diagonal == 5:
        game_over(i, j, num)


    row = 0 
    col = 0 
    down_Diagonal = 0 
    up_Diagonal = 0


def who_win():
    for i in range(10):
        for j in range(10):
            if Omok_map[i][j] == 1:
                rule_chek(i, j, 1, row, col ,down_Diagonal, up_Diagonal)
            elif Omok_map[i][j] == 2:
                rule_chek(i, j, 2, row, col ,down_Diagonal ,up_Diagonal)



board_buttons = [[None for x in range(w)] for y in range(h)]

global flag
flag = True
for y in range(h):
    for x in range(w):
        b = Button(parent=scene, position=(x, y), color=color.clear, model='circle', scale=0.9)
            
        board_buttons[y][x] = b
        def on_mouse_enter(b=b):
            if  b.collision:
                b.color = color._100
        
        def on_mouse_exit(b=b):
            if b.collision:
                b.color = color.clear

        # 마우스 커서에 돌 확인
        b.on_mouse_enter = on_mouse_enter
        b.on_mouse_exit = on_mouse_exit

        def click(b=b):
            if fin == 1:
                print("흑돌이 이겼습니다!")
            elif fin == 2:
                print("백돌이 이겼습니다!")
            else:
                global flag
                if flag == True:
                    b.text = "B"
                    b.color = color.black
                    b.collision = False
                    flag = False
                    Omok_map[19 - int(b.position.y) ][int(b.position.x)] = 1
                    who_win()
                
                    
                else:
                    b.text = "W"
                    b.text_color = color.black
                    b.color = color.white
                    b.collision = False 
                    flag = True
                    Omok_map[19 - int(b.position.y)][int(b.position.x)] = 2
                    who_win()

        b.on_click = click

app.run()