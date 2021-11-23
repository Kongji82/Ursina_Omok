from ursina import *
from setting import *
import numpy as np

app = Ursina()

global flag, ux, uy
flag = True
w, h = 20, 20
board_buttons = [[None for x in range(w)] for y in range(h)]

# 창 설정
window.borderless = False
window.color = color._50

# 카메라 설정
camera.orthographic = True      # 2D
camera.fov = 23
camera.position = (w//2, h//2)

map_size = 21
Omok_map = np.zeros([map_size, map_size])

Entity(model=Grid(w+1, h+1), scale=w+1, color=color.black, x=w//2-0.5, y=h//2-0.5, z=0.1)   

def show_winner(won_player):
    Panel(z=1, scale=10, model='quad')
    show_player = ""
    if won_player == 1:
        show_player = "Black"
    elif won_player == 2:
        show_player = "Black"
    t = Text(f'{show_player} Win!', scale=3, origin=(0, 0), background=True)
    t.create_background(padding=(.5,.25), radius=Text.size/2)
    b1.text_color = color.clear


b1 = Button(text="Reset", scale=(0.1, 0.1, 0.1), position = (.6, .3), color = color.clear, model = 'quad')
b2 = Button(text="Surrender", scale=(0.1, 0.1, 0.1), position = (.6, .2), color = color.clear, model = 'quad')
b3 = Button(text="Undo", scale=(0.1, 0.1, 0.1), position = (.6, .1), color = color.clear, model = 'quad')

def _reset_(b1 = b1):
    for y in range(h):
        for x in range(w):
            global flag
            global Omok_map
            board_buttons[y][x].color = color.clear
            board_buttons[y][x].text_color = color.clear
            board_buttons[y][x].collision = True
            flag = True

    Omok_map = np.zeros([map_size, map_size])

def _finish_(b2 = b2):
    global flag
    if flag == False:
        show_winner(1)
    else:
        show_winner(2)

def _Undo_(b3 = b3):
    global ux, uy, flag
    global Omok_map
    if flag == True:
        board_buttons[19 - ux][uy].color = color.clear
        board_buttons[19 - ux][uy].text_color = color.clear
        board_buttons[19 - ux][uy].collision = True
        Omok_map[ux][uy] = 0
        flag = False
    else:
        board_buttons[19 - ux][uy].color = color.clear
        board_buttons[19 - ux][uy].text_color = color.clear
        board_buttons[19 - ux][uy].collision = True
        Omok_map[ux][uy] = 0
        flag = True


b1.on_click = _reset_
b2.on_click = _finish_
b3.on_click = _Undo_

def game_start():
    for y in range(h):
        for x in range(w):
            global b
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
                count = 1
                global flag
                global ux, uy
                if flag == True:
                    b.text = "B"
                    b.text_color = color.white
                    b.color = color.black
                    b.collision = False 
                    flag = False
                    Omok_map[19 - int(b.position.y)][int(b.position.x)] = 1
                    ux = 19 - int(b.position.y)
                    uy = int(b.position.x)
                    if who_win(Omok_map) == 1:
                        show_winner(1)
                
                else:
                    b.text = "W"
                    b.text_color = color.black
                    b.color = color.white
                    b.collision = False 
                    flag = True
                    Omok_map[19 - int(b.position.y)][int(b.position.x)] = 2
                    ux = 19 - int(b.position.y)
                    uy = int(b.position.x)
                    if who_win(Omok_map) == 2:
                        show_winner(2)

            b.on_click = click

if __name__ == "__main__":
    game_start()
    app.run()