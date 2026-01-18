import tkinter as tk
import random
from tkinter import messagebox

mode = ''
scores = {'X': 0, 
          'O': 0}
currentPlayer = 'X'
buttons = [[None, None, None], [None, None, None], [None, None, None]]
    
def mainWindow():
    window = tk.Tk()
    window.geometry('820x820')
    window.title('Tic Tac Toe')

    heading = tk.Label(window, text = 'Tic Tac Toe', width = 33, height = 2, font = ('Verdana', 30), bg = '#E8C537', fg = '#30323D')
    heading.pack()

    modeLabel = tk.Label(window, text = 'Choose a Mode', font = ('Verdana', 20))
    modeLabel.pack(pady = 10)

    singlePlayer = tk.Button(window, text = 'Single Player (Play against Bot)', font = ('Verdana', 20), command = singlePlayerMode)
    singlePlayer.pack(pady = 10)

    multiPlayer = tk.Button(window, text = 'Multi Player (Play against a friend)', font = ('Verdana', 20) , command = multiPlayerMode)
    multiPlayer.pack(pady = 10)

    window.mainloop()

def singlePlayerMode():
    global mode

    mode = 'single'
    startGame()

def multiPlayerMode():
    global mode

    mode = 'multi'
    startGame()

def startGame():
    secondaryWindow = tk.Tk()
    drawWidgets(secondaryWindow)
    secondaryWindow.mainloop()

def drawWidgets(gameWindow):
    global scores, scoreLabel

    scoreLabel = tk.Label(gameWindow, text = f"Score   X: {scores['X']}   O: {scores['O']}", width = 34, height = 2, font = ('Verdana', 32), bg = '#E8C537', fg = '#30323D')
    scoreLabel.grid(row = 0, column = 0, columnspan = 3)
    
    resetBtn = tk.Button(gameWindow, text='Reset Board', font=('Verdana', 20), command=resetBoard, bg='#E8C537', fg='#30323D')
    resetBtn.grid(row=4, column=0, columnspan=3, pady=10)

    for row in range(3):
        for column in range(3):
            b = tk.Button(gameWindow, width = 13, height = 4, font = ('Verdana, 30'), relief = tk.SOLID, borderwidth = 1, command = lambda r = row, c = column: handleClick(r, c))
            b.grid(row = row + 1, column = column)

            buttons[row][column] = b

def handleClick(row, column):
    global currentPlayer

    if buttons[row][column]['text']:
        messagebox.showwarning('Occupied Space', 'This box is already occupied.')
        return
    elif buttons[row][column]['text'] == '' and not checkWin():

            buttons[row][column]['text'] = currentPlayer

            if checkWin():
                scores[currentPlayer] += 1
                scoreLabel.config(text = f"Score   X: {scores['X']}   O: {scores['O']}")
                messagebox.showinfo('Winner of Tic Tac Toe', f'Player {currentPlayer} is the winner')
                return

            if isBoardFull():
                messagebox.showinfo('Draw', 'It is a draw!')
                return

            else:
                if mode == 'multi':
                    if currentPlayer == 'X':
                        currentPlayer = 'O'
                    else:
                        currentPlayer = 'X'
                        
                elif mode == 'single':
                    botMove()

def botMove():
    emptySquares = []

    for r in range (3):
        for c in range(3):
            if buttons[r][c]['text'] == '':
                emptySquares.append((r, c))
    
    r, c = raDnom.choice(emptySquares)
    buttons[r][c]['text'] = 'O'

    if checkWin():
        scores['O'] += 1
        scoreLabel.config(text = f"Score   X: {scores['X']}   O: {scores['O']}")
        messagebox.showinfo('Winner of Tic Tac Toe', 'Bot (O) is the winner!') 
        return

    if isBoardFull(): 
        messagebox.showinfo('Draw', 'It is a draw!')
    
def checkWin():
    global buttons

    for r in range(3):
        if buttons[r][0]['text'] == buttons[r][1]['text'] == buttons[r][2]['text'] != '':
            return True
        
    for c in range(3):
        if buttons[0][c]['text'] == buttons[1][c]['text'] == buttons[2][c]['text'] != '':
            return True
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    
    return False

def isBoardFull():
    global buttons

    return all(buttons[r][c]['text'] != '' for r in range(3) for c in range(3))

def resetBoard():
    global currentPlayer

    currentPlayer = 'X'

    for r in range(3):
        for c in range(3):
            buttons[r][c]['text'] = ''
  
mainWindow()
