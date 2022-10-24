# Задача 3. Создайте программу для игры в ""Крестики-нолики""

from tkinter import *
from tkinter import messagebox
import tkinter.font as font

window = Tk()
window.title('Игра крестики-нолики')

def chose_winner(mylist):
    win_cond = [[0,1,2], [3,4,5], [6,7,8],[0,3,6],\
                       [1,4,7], [2,5,8],[6,4,2], [0,4,8]]
    for pos in win_cond:
        if mylist[pos[0]] == mylist[pos[1]] == mylist[pos[2]]\
         and mylist[pos[0]] in ('X0'):
            if mylist[pos[0]] == 'X':
                messagebox.showinfo('Победили крестики!') 
                window.destroy()
            if mylist[pos[0]] == '0':
                messagebox.showinfo('Победили нолики!') 
                window.destroy()
    if ' ' not in mylist:
        messagebox.showinfo('Это ничья!') 
        window.destroy()

def push(board, cell):
    global turn
    if turn % 2 == 0:
        board[cell] = 'X'
        button[cell].config(text='X', state = 'disabled')
        turn += 1
    else:
        board[cell] = '0'
        button[cell].config(text='0', state = 'disabled')
        turn += 1
    if turn > 3:
        chose_winner(board)


mylist = [" "] * 9
turn = 0

myFont = font.Font(size = 60)
button = [Button( width = 3, height = 1, font = myFont, \
                 command = lambda x = i: push(mylist,x)) for i in range (9)]

row = 1; col = 0
for i in range(9):
    button[i].grid(row = row, column = col, sticky=W+E)
    col += 1
    if col == 3:
        row += 1; col = 0

window.mainloop()