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

        b.on_mouse_enter = on_mouse_enter
        b.on_mouse_exit = on_mouse_exit

        def b_click(b=b):
            # black turn
            # b.text = '1'
            b.color = color.black
            b.collision = False

        def w_click(b=b):
            # white turn

            b.color = color.white
            b.collision = False

        turn = x + y
        
        if turn % 2 == 0:
            b.on_click = b_click
        else:
            b.on_click = w_click


app.run()