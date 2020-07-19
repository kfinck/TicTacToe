from tkinter import *

root =Tk()
root.title("Tic Tac Toe")

board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
    ]


def enemyclick():
        if board[1][1] == " ":
            board[1][1] = "O"
            #sides have 2 cases, corners have 3
        #wins
        elif board[0][2] == " " and((board[0][0] == "O" and board[0][1] == "O") or (board[0][0] == "O" and board[0][1] == "O") or (board[1][2] == "O" and board[2][2] == "O")):
            board[0][2] = "O"
        elif board[0][1] == " " and((board[0][0] == "O" and board[0][2] == "O") or (board[1][1] == "O" and board[2][1] == "O")):
            board[0][1] = "O"
            lose = True
        elif board[1][0] == " " and( (board[0][0] == "O" and board[2][0] == "O") or (board[1][1] == "O" and board[1][2] == "O")):
            board[1][0] = "O"
            lose = True
        elif board[1][2] == " " and((board[0][2] == "O" and board[2][2] == "O") or (board[1][0] == "O" and board[1][1] == "O")):
            board[1][2] = "O"
            lose = True
        elif board[2][0] == " " and( (board[0][0] == "O" and board[1][0] == "O") or (board[2][1] == "O" and board[2][2] == "O") or (board[1][1] == "O" and board[0][2] == "O")):
            board[2][0] = "O"
            lose = True
        elif board[2][1] == " " and((board[2][0] == "O" and board[2][2] == "O") or (board[1][1] == "O" and board[0][1] == "O")):
            board[2][1] = "O"
            lose = True
        elif board[2][2] == " " and( (board[2][0] == "O" and board[2][1] == "O") or (board[0][2] == "O" and board[1][2] == "O") or (board[0][0] == "O" and board[1][1] == "O")):
            board[2][2] = "O"
            lose = True
        #blocks
        elif board[0][2] == " " and((board[0][0] == "X" and board[0][1] == "X") or (board[0][0] == "X" and board[0][1] == "X") or (board[1][2] == "X" and board[2][2] == "X")):
            board[0][2] = "O"
        elif board[0][1] == " " and((board[0][0] == "X" and board[0][2] == "X") or (board[1][1] == "X" and board[2][1] == "X")):
            board[0][1] = "O"
        elif board[1][0] == " " and( (board[0][0] == "X" and board[2][0] == "X") or (board[1][1] == "X" and board[1][2] == "X")):
            board[1][0] = "O"
        elif board[1][2] == " " and((board[0][2] == "X" and board[2][2] == "X") or (board[1][0] == "X" and board[1][1] == "X")):
            board[1][2] = "O"
        elif board[2][0] == " " and( (board[0][0] == "X" and board[1][0] == "X") or (board[2][1] == "X" and board[2][2] == "X") or (board[1][1] == "X" and board[0][2] == "X")):
            board[2][0] = "O"
        elif board[2][1] == " " and((board[2][0] == "X" and board[2][2] == "X") or (board[1][1] == "X" and board[0][1] == "X")):
            board[2][1] = "O"
        elif board[2][2] == " " and( (board[2][0] == "X" and board[2][1] == "X") or (board[0][2] == "X" and board[1][2] == "X") or (board[0][0] == "X" and board[1][1] == "X")):
            board[2][2] = "O"
        else:
            if board[0][0] == " ":
                board[0][0] = "O"
            elif board[0][2] == " ":
                board[0][2] = "O"
            elif board[2][0] == " ":
                board[2][0] = "O"
            elif board[2][2] == " ":
                board[2][2] = "O"
            elif board[0][1] == " ":
                board[0][1] = "O"
            elif board[1][0] == " ":
                board[1][0] = "O"
            elif board[1][2] == " ":
                board[1][2] = "O"
            elif board[2][1] == " ":
                board[2][1] = "O"
        if board[0][0] == "O":
            button_tl['text'] = "O"
        if board[0][1] == "O":
            button_tm['text'] = "O"
        if board[0][2] == "O":
            button_tr['text'] = "O"
        if board[1][0] == "O":
            button_ml['text'] = "O"
        if board[1][1] == "O":
            button_mm['text'] = "O"
        if board[1][2] == "O":
            button_mr['text'] = "O"
        if board[2][0] == "O":
            button_bl['text'] = "O"
        if board[2][1] == "O":
            button_bm['text'] = "O"
        if board[2][2] == "O":
            button_br['text'] = "O"
        

def click(x,y,z):
    if board[x][y] == " ":
        board[x][y] = "X"
        if z == 1:
            button_tl['text'] = "X"
        elif z == 2:
            button_tm['text'] = "X"
        elif z == 3:
            button_tr['text'] = "X"
        elif z == 4:
            button_ml['text'] = "X"
        elif z == 5:
            button_mm['text'] = "X"
        elif z == 6:
            button_mr['text'] = "X"
        elif z == 7:
            button_bl['text'] = "X"
        elif z == 8:
            button_bm['text'] = "X"
        elif z == 9:
            button_br['text'] = "X"
        enemyclick()

def reset():
    for x in range(0,3):
        for y in range(0,3):
            board[x][y] = " "

    button_tl['text'] = " "
    button_tm['text'] = " "
    button_tr['text'] = " "
    button_ml['text'] = " "
    button_mm['text'] = " "
    button_mr['text'] = " "
    button_bl['text'] = " "
    button_bm['text'] = " "
    button_br['text'] = " "




button_tl = Button(root, text = " ", padx=30,pady=30,command = lambda: click(0,0,1))
button_tm = Button(root, text = " ", padx=30,pady=30,command = lambda: click(0,1,2))
button_tr = Button(root, text = " ", padx=30,pady=30,command = lambda: click(0,2,3))
button_ml = Button(root, text = " ", padx=30,pady=30,command = lambda: click(1,0,4))
button_mm = Button(root, text = " ", padx=30,pady=30,command = lambda: click(1,1,5))
button_mr = Button(root, text = " ", padx=30,pady=30,command = lambda: click(1,2,6))
button_bl = Button(root, text = " ", padx=30,pady=30,command = lambda: click(2,0,7))
button_bm = Button(root, text = " ", padx=30,pady=30,command = lambda: click(2,1,8))
button_br = Button(root, text = " ", padx=30,pady=30,command = lambda: click(2,2,9))
reset_button = Button(root, text = "Reset", padx=30,pady=30,command = reset)

button_tl.grid(row = 0,column = 0)
button_tm.grid(row = 0,column = 1)
button_tr.grid(row = 0,column = 2)
button_ml.grid(row = 1,column = 0)
button_mm.grid(row = 1,column = 1)
button_mr.grid(row = 1,column = 2)
button_bl.grid(row = 2,column = 0)
button_bm.grid(row = 2,column = 1)
button_br.grid(row = 2,column = 2)
reset_button.grid(row = 3, column = 1)




root.mainloop()
