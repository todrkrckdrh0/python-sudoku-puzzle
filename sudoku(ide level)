from random import *

def Output():
    for j in range(0,9):
        for k in range(0,9):
            print(slist[j][k], end = ' ')
        print()

slist = []
for i in range(1,10):
    slist.append([0]*9)

init = []
for i in range(1,10):
    init.append([0]*9)


def initrowCheck():
    rc = 0
    for j in range(0,9):
        for c in range(1,10):
            if slist[j].count(c) > 1:
                rc = 1
    if rc == 1:
        return 1
    else:
        return 0

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

def initcolCheck():
    cc = 0
    for k in range(0,9):
        check = []
        for j in range(0,9):
            check.append(slist[j][k])
        for c in range(1,10):
            if check.count(c) > 1:
                cc = 1
    if cc == 1:
        return 1
    else:
        return 0

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

def initboxCheck():
    bc = 0
    for j in [0,3,6]:
        for k in [0,3,6]:
            check = []
            for n in range(0,3):
                for m in range(0,3):
                    check.append(slist[j+n][k+m])
            for c in range(1,10):
                if check.count(c) > 1:
                    bc = 1
    if bc == 1:
        return 1
    else:
        return 0

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
while difn > 0:
    ix = randint(0,8)
    iy = randint(0,8)
    if init[ix][iy] == 0:
        slist[ix][iy] = randint(1,9)
        if initboxCheck() == 0 and initcolCheck() == 0 and initrowCheck() == 0:
            init[ix][iy] = 1
            difn -= 1
        else:
            slist[ix][iy] = 0

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
