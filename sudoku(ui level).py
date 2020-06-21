from tkinter import *
import tkinter.messagebox
from tkinter import font as tkfont
from random import randint

def board():
    return [[0 for _ in range(9)] for _ in range(9)]


def change_row_col(before):
    after = board()
    for i in range(len(before)):
        for j in range(len(before)):
            after[j][i] = before[i][j]
    return after
def init_sudoku():
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
    k = solution[row1]
    solution[row1] = solution[row2]
    solution[row2] = k

    return solution


def switch_column(solution, row1, row2, i, j):
    while (row2 == row1):
        row2 = randint(i, j)
    solution = change_row_col(solution)
    k = solution[row1]
    solution[row1] = solution[row2]
    solution[row2] = k

    return solution

sudoku = init_sudoku()

def erase(sudoku):
    for i in range(60):
        row = randint(0,8)
        column = randint(0,8)
        sudoku[row][column] = 0
    return sudoku

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
switch_values(sudoku)
margin = 20
side = 50
Width = Height = margin * 2 + side * 9
slist_puzzle = erase(sudoku)
slist_init = []
slist_check = []
for i in range(1,10):
    slist_init.append([0]*9)
    slist_check.append([0]*9)
for i in range(9):
    for j in range(9):
        if slist_puzzle[i][j] == 0:
            slist_init[i][j] = 0
        else:
            slist_init[i][j] = 1

class SudokuUI(Frame):

    def __init__(self, parent):
        super(SudokuUI, self).__init__()
        self.row, self.col = -1, -1
        self.__initUI()

    def centerWindow(self):
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        self.master.geometry('%dx%d+%d+%d' % (Width, Height + 160, (sw - Width) / 2, (sh - Height - 160) / 2))

    def __initUI(self):
        self.pack(fill = 'both', side = 'top')
        self.canvas = Canvas(self, width = Width, height = Height)
        self.canvas.pack(fill = 'both', side = 'top')
        HowTo = Label(root, text = '''
스도쿠는 가로, 세로, 3x3 박스 안의 9개 칸에 1~9의 숫자를
중복되지 않게 채워 넣는 게임입니다.
네모칸들을 클릭한 후 키보드판의 숫자 키를 눌러 숫자를 입력할 수 있습니다.
1~9와 0을 입력할 수 있으며, 0은 공백으로 처리됩니다
처음에 이미 주어진 값(파란색 글씨)은 바꿀 수 없으며,
중복된 숫자는 빨간색 글씨로 표시됩니다.''')
        HowTo.place(x = 0, y = 490, width = Width, height = 110)
        #HowTo.pack(side = 'bottom')
        self.centerWindow()
        self.__draw_grid()
        self.__draw_puzzle()
        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)

    def __draw_grid(self):
        for i in range(10):
            color = "black" if i % 3 == 0 else "gray"

            x0 = margin + i * side
            y0 = margin
            x1 = margin + i * side
            y1 = Height - margin
            self.canvas.create_line(x0, y0, x1, y1, fill = color)

            x0 = margin
            y0 = margin + i * side
            x1 = Width - margin
            y1 = margin + i * side
            self.canvas.create_line(x0, y0, x1, y1, fill = color)

    def __draw_puzzle(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                font = tkfont.Font(root=self.canvas, size=24, weight = "bold")
                self.check_wrong(i, j)
                answer = slist_puzzle[i][j]
                if answer != 0:
                    x = margin + j * side + side / 2
                    y = margin + i * side + side / 2
                    original = slist_init[i][j]
                    if slist_check[i][j] == -1:
                        color = "red"
                    elif original == 0:
                        color = "black"
                    else:
                        color = "royal blue"
                    self.canvas.create_text(x, y, text = answer, tags = "numbers", fill = color, font = font)

    def __cell_clicked(self, event):
        x, y = event.x, event.y

        if margin < x < (Width - margin) and margin < y < (Height - margin):
            self.canvas.focus_set()
            row, col = (y - margin) // side, (x - margin) // side
            if (self.row, self.col) == (row, col):
                self.row, self.col = -1, -1
            elif slist_init[row][col] == 0:
                self.row, self.col = row, col
        else:
            self.row, self.col = -1, -1
        self.__draw_cursor()

    def __draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = margin + self.col * side
            y0 = margin + self.row * side
            x1 = margin + (self.col + 1) * side
            y1 = margin + (self.row + 1) * side
            self.canvas.create_rectangle(x0, y0, x1, y1, outline = "red", width = 3, tags = "cursor")

    def __key_pressed(self, event):
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890":
            slist_puzzle[self.row][self.col] = int(event.char)
            self.__draw_puzzle()
            self.__draw_cursor()
            if self.check_victory():
                root.after_cancel(solve)
                self.__draw_victory()

    def __draw_victory(self):
        self.vm = tkinter.messagebox.showinfo("","정답입니다!")
        for i in range(9):
            for j in range(9):
                slist_init[i][j] = 1
        self.__draw_puzzle()

    def check_wrong(self, x, y):
        for i in range(9):
            for j in range(9):
                slist_check[i][j] = 0
        rowCheck = []
        colCheck = []
        boxCheck = []
        if self.row >= 0 and self.col >= 0:
            for i in range(9):
                rowCheck.append(slist_puzzle[x][i])
                colCheck.append(slist_puzzle[i][y])
            for j in range(3):
                for k in range(3):
                    boxCheck.append(slist_puzzle[x//3*3+j][y//3*3+k])
        for i in range(1,10):
            if rowCheck.count(i) > 1:
                for j in range(9):
                    if rowCheck[j] == i:
                        slist_check[x][j] = -1
            if colCheck.count(i) > 1:
                for j in range(9):
                    if colCheck[j] == i:
                        slist_check[j][y] = -1
            if boxCheck.count(i) > 1:
                for j in range(9):
                    if boxCheck[j] == i:
                        slist_check[x//3*3+j//3][y//3*3+j%3] = -1

    def check_victory(self):
        for r in range(9):
            if not set(slist_puzzle[r]) == set(range(1,10)):
                return False
        for c in range(9):
            if not set(slist_puzzle[r][c] for r in range(9)) == set(range(1,10)):
                return False
        for r in range(3):
            for c in range(3):
                if not set(slist_puzzle[row][col] for row in range(r*3, (r+1)*3) for col in range(c*3, (c+1)*3)) == set(range(1,10)):
                    return False
        return True


s=0; m=0; h=0


def Run():
    global s, m, h
    w.delete('all')
    w.create_text([Width / 2, 10], text='타이머: %02d:%02d:%02d' % (h, m, s))
    if s == 60:
        m += 1;
        s = 0
    elif m == 60:
        h += 1;
        m = 0
    s += 1
    global solve
    solve = root.after(1000, Run)

if __name__ == '__main__':
    root = Tk()
    root.title("스도쿠")
    root.resizable(False, False)
    w = Canvas(root, width = Width, height=25)
    w.pack(side = 'bottom')
    SudokuUI(root)
    root.after(1, Run)
    root.mainloop()
