#오목알이 유효한지
def is_Vaild(x, y, num, Omok_map):
    return Omok_map[x][y] == num

#오목 규칙
def rule_chek(i, j, num, Omok_map):
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
    flag = False

    for dir in dirs:
        judge = 0
        for k in range(5):
            if is_Vaild(i+dir[0] * k, j+dir[1] * k, num, Omok_map):
                judge += 1
            else:
                break

        if judge == 5:
            flag = True
            break

    if flag:
        return num

#전체 2차원 배열을 탐색하여 5개 연속돌 찾기        
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