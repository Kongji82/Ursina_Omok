def is_num(x, y, num, Omok_map):
    if Omok_map[x][y] != num:
        return False
    else:
        return True

def game_over(num):
    print(num)
    return num

def rule_chek(i, j, num, Omok_map):
    row = 0 
    col = 0 
    down_Diagonal = 0 
    up_Diagonal = 0

    for k in range(5):
        if is_num(i, j + k, num, Omok_map) == False:
            break
        else:
            row = row + 1

    for k in range(5):
        if is_num(i + k, j, num, Omok_map) == False:
            break
        else:
            col = col + 1

    for k in range(5):
        if is_num(i + k, j + k, num, Omok_map) == False:
            break
        else:
            down_Diagonal = down_Diagonal + 1

    for k in range(5):
        if is_num(i - k, j + k, num, Omok_map) == False:
            break
        else:
            up_Diagonal = up_Diagonal + 1
    
    if row == 5 or col == 5 or down_Diagonal == 5 or up_Diagonal == 5:
        winner = game_over(num)
        return winner
        
def who_win(Omok_map):
    for i in range(20):
        for j in range(20):
            if Omok_map[i][j] == 1:
                winner = rule_chek(i, j, 1, Omok_map)
                if winner == 1:
                    return 1
                    
            elif Omok_map[i][j] == 2:
                winner = rule_chek(i, j, 2, Omok_map)
                if winner == 2:
                    return 2