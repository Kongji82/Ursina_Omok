map = [list(map(int, input().split())) for _ in range(10)]

cnt = 0 
row = 0 
col = 0
ur = 0 
dr = 0



def check(x, y, num):
    if map[x][y] != num:
        return False
    else:
        return True
    


def finish(i, j, num):
    print(num)



def search12(i, j, num, row, col, ur, dr):

    for k in range(5):
        if check(i, j + k, num) == False:
            break
        else:
            row = row + 1

    for k in range(5):
        if check(i + k, j, num) == False:
            break
        else:
            col = col + 1

    for k in range(5):
        if check(i + k, j + k, num) == False:
            break
        else:
            dr = dr + 1

    for k in range(5):
        if check(i - k, j + k, num) == False:
            break
        else:
            ur = ur + 1


    if row == 5:
        finish(i, j, num)

    if col == 5:
        finish(i, j, num)

    if ur == 5:
        finish(i, j, num)

    if dr == 5:
        finish(i, j, num)

    row = 0 
    col = 0 
    ur = 0 
    dr = 0


for i in range(10):
    for j in range(10):
        if map[i][j] == 1:
            search12(i, j, 1, row, col ,ur, dr)
        elif map[i][j] == 2:
            search12(i, j, 2, row, col ,ur ,dr)

            

