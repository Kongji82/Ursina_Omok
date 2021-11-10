import numpy as np

map_size = 10
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
    print(num)
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


    if row == 5:
        game_over(i, j, num)

    if col == 5:
        game_over(i, j, num)

    if down_Diagonal == 5:
        game_over(i, j, num)

    if up_Diagonal == 5:
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




            
player_turn = map_size * map_size

for i in range(player_turn):

    if fin == 1:
        print("흑돌이 이겼습니다!")
        break
    elif fin == 2:
        print("백돌이 이겼습니다!")
        break
    else:
        if i % 2 == 0:
            x, y = map(int, input("흑돌 차례입니다 : ").split())
            Omok_map[x, y] = 1
            who_win()
            

        else: 
            x, y = map(int, input("백돌 차례입니다 : ").split())
            Omok_map[x, y] = 2
            who_win()
            

    print(Omok_map)
