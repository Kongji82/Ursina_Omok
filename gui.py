from ursina import *

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
            global flag
            if flag == True:
                b.text = "B"
                b.color = color.black
                b.collision = False
                flag = False
            else:
                b.text = "W"
                b.text_color = color.black
                b.color = color.white
                b.collision = False 
                flag = True
            # black turn

        # def w_click(b=b):
        #     # white turn
        #     b.text = "W"
        #     b.color = color.white
        #     b.collision = False

        b.on_click = click

app.run()