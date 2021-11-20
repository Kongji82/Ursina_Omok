from ursina import *
from setting import *
import numpy as np

app = Ursina()

global flag
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

map_size = 20
Omok_map = np.zeros([map_size, map_size])

Entity(model=Grid(w+1, h+1), scale=w+1, color=color.black, x=w//2-0.5, y=h//2-0.5, z=0.1)   

def show_winner(won_player):
    Panel(z=1, scale=10, model='quad')
    t = Text(f'Player {won_player} won!', scale=3, origin=(0, 0), background=True)
    t.create_background(padding=(.5,.25), radius=Text.size/2)
    b1.text_color = color.clear


b1 = Button(text="undo", scale=(0.1, 0.1, 0.1), position = (.6, .3), color = color.clear, model = 'quad')

def _reset_(b1 = b1):
    print("_Undo_")
    for y in range(h):
        for x in range(w):
            board_buttons[y][x].color = color.clear
            board_buttons[y][x].text_color = color.clear
            board_buttons[y][x].collision = True

b1.on_click = _reset_

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
                if flag == True:
                    b.text = "B"
                    b.color = color.black
                    b.collision = False
                    flag = False
                    Omok_map[19 - int(b.position.y)][int(b.position.x)] = 1
                    if who_win(Omok_map) == 1:
                        show_winner(1)
                
                else:
                    b.text = "W"
                    b.text_color = color.black
                    b.color = color.white
                    b.collision = False 
                    flag = True
                    Omok_map[19 - int(b.position.y)][int(b.position.x)] = 2
                    if who_win(Omok_map) == 2:
                        show_winner(2)

            b.on_click = click


if __name__ == "__main__":
    game_start()
    app.run()