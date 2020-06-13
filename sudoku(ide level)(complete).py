from random import randint
import copy

def Output():
    for j in range(0,9):
        for k in range(0,9):
            print(slist[j][k], end = ' ')
        print()

def matrix():
    return [[0 for _ in range(9)] for _ in range(9)]

def print_sudoku(s):
    for e in s:
        print(e, end="\n")

def trasponi(matrice):
    trasposta = matrix()
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            trasposta[j][i] = matrice[i][j]
    return trasposta
def riempi_sudoku():
    solution = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9, 1, 2, 3], [7, 8, 9, 1, 2, 3, 4, 5, 6],
                [2, 3, 4, 5, 6, 7, 8, 9, 1], [5, 6, 7, 8, 9, 1, 2, 3, 4], [8, 9, 1, 2, 3, 4, 5, 6, 7],
                [3, 4, 5, 6, 7, 8, 9, 1, 2], [6, 7, 8, 9, 1, 2, 3, 4, 5], [9, 1, 2, 3, 4, 5, 6, 7, 8]]

    for i in range(30):
        row1 = randint(0, 2)
        row2 = randint(0, 2)
        solution = switch_row(solution, row1, row2, 0, 2)
        solution = switch_column(solution, row1, row2, 0, 2)

    for i in range(30):
        row1 = randint(3, 5)
        row2 = randint(3, 5)
        solution = switch_row(solution, row1, row2, 3, 5)
        solution = switch_column(solution, row1, row2, 3, 5)

    for i in range(30):
        row1 = randint(6, 8)
        row2 = randint(6, 8)
        solution = switch_row(solution, row1, row2, 6, 8)
        solution = switch_column(solution, row1, row2, 6, 8)

    return solution


def switch_row(solution, row1, row2, i, j):
    while (row2 == row1):
        row2 = randint(i, j)
    tmp = solution[row1]
    solution[row1] = solution[row2]
    solution[row2] = tmp

    return solution


def switch_column(solution, row1, row2, i, j):
    while (row2 == row1):
        row2 = randint(i, j)
    solution = trasponi(solution)
    tmp = solution[row1]
    solution[row1] = solution[row2]
    solution[row2] = tmp

    return solution

sudoku = riempi_sudoku()


def switch_values(sudoku):
    conta = 0
    while(conta<5): #per garantire una maggiore diversità
        value1 = randint(1,9)
        value2 = randint(1,9)
        while(value2==value1):
            value2 = randint(1,9)

        for i in range(len(sudoku)):
            for j in range(len(sudoku)):
                if(sudoku[i][j]==value1):
                    sudoku[i][j]=value2
                elif(sudoku[i][j]==value2):
                    sudoku[i][j]=value1
        conta+=1
    return sudoku

def erase(sudoku, difn):
    for i in range(difn):
        row = randint(0,8)
        column = randint(0,8)
        sudoku[row][column] = 0
    return sudoku

def rowCheck():
    for j in range(0,9):
        rc = 0
        for c in range(1,10):
            if slist[j].count(c) > 1:
                rc = 1
        if rc == 1:
            print('로우 {} 오류'.format(j+1))

def colCheck():
    for k in range(0,9):
        cc = 0
        check = []
        for j in range(0,9):
            check.append(slist[j][k])
        for c in range(1,10):
            if check.count(c) > 1:
                cc = 1
        if cc == 1:
            print('칼럼 {} 오류'.format(k+1))

def boxCheck():
    num = 1
    for j in [0,3,6]:
        for k in [0,3,6]:
            bc = 0
            check = []
            for n in range(0,3):
                for m in range(0,3):
                    check.append(slist[j+n][k+m])
            for c in range(1,10):
                if check.count(c) > 1:
                    bc = 1
            if bc == 1:
                print('박스 {} 오류'.format(num))
            num += 1

def Victory():
    rc = cc = bc = 0
    for j in range(0, 9): #로우
        for c in range(1, 10):
            if slist[j].count(c) != 1:
                rc = 1
    for k in range(0, 9): #컬럼
        check = []
        for j in range(0, 9):
            check.append(slist[j][k])
        for c in range(1, 10):
            if check.count(c) != 1:
                cc = 1
    for j in [0, 3, 6]: #박스
        for k in [0, 3, 6]:
            check = []
            for n in range(0, 3):
                for m in range(0, 3):
                    check.append(slist[j + n][k + m])
            for c in range(1, 10):
                if check.count(c) != 1:
                    bc = 1
    if rc == bc == cc == 0:
        return 0
    else:
        return 1


q = input('난이도를 선택하세요(쉬움, 보통, 어려움): ')
if q == '쉬움':
    difn = 37
elif q == '보통':
    difn = 27
elif q == '어려움':
    difn = 17
slist = copy.deepcopy(sudoku)
erase(slist, difn)

init = copy.deepcopy(slist)
for i in range(9):
    for j in range(9):
        if init[i][j] != 0:
            init[i][j] = 1

while True:
    Output()
    if Victory() == 0:
        print('축하합니다! 스도쿠를 완성하셨습니다!')
        break
    rowCheck()
    colCheck()
    boxCheck()
    while True:
        x = int(input('행을 선택하세요: '))
        y = int(input('열을 선택하세요: '))
        n = int(input('({}, {})에 입력할 값을 선택하세요: '.format(x, y)))
        if x in range(1,10) and y in range(1,10) and n in range(1,10):
            break
        else:
            print('error')
    if init[x - 1][y - 1] == 0:
        slist[x - 1][y - 1] = n
    elif init[x - 1][y - 1] == 1:
        print('초기에 설정된 값은 변경할 수 없습니다.')