from tkinter import *
from time import sleep

tk = Tk()
tk.geometry("300x250")
tk.resizable(False, False)
tk.attributes('-topmost', True)
tk.title("Pong")

stop = False
play_again = True


def game():
    global gc, score1, score2
    score1 += 1
    var = IntVar()
    Label(gc, text="GAME OVER!", font=(None, 30), bg="black", fg="red").place(x=20, y=70)
    Button(gc, text="Play again", bg="black", fg="white", command=lambda: var.set(1)).place(x=110, y=160)
    if score1 > score2:
        Label(gc, text="Player 1 wins!", font=(None, 20), bg="black", fg="green").place(x=60, y=117)
    else:
        Label(gc, text="Player 2 wins!", font=(None, 20), bg="black", fg="green").place(x=60, y=117)
    
    tk.wait_variable(var)
    gc.destroy()
    gc = Canvas(tk, bg="black")
    gc.bind("<KeyPress>", keydown)
    gc.focus_set()
    gc.pack()


def keydown(e):
    global paddle1_x, paddle2_x, score1, stop, play_again
    if e.keysym=="a":
        paddle1_x -= 5
    if e.keysym=="s":
        paddle1_x += 5
    if e.keysym=="k":
        paddle2_x -= 5
    if e.keysym=="l":
        paddle2_x += 5
    if e.keysym=="Return":
        play_again = True
        stop = True


gc = Canvas(tk, bg="black")
gc.bind("<KeyPress>", keydown)
gc.focus_set()
gc.pack()

while play_again:
    
    stop = False
    
    score1 = 0
    score1_label = Label(gc, text="hi", bg="black", fg="white")
    score1_label.place(x=10, y=5)
    
    score2 = 0
    score2_label = Label(gc, text="hi", bg="black", fg="white")
    score2_label.place(x=240, y=5)
    
    ball_x = 150
    ball_y = 10
    xv = 1
    yv = 1
    ball_size = 10
    
    paddle1_x = 50
    paddle1_y = 235
    paddle2_x = 200
    paddle2_y = 235
    
    while not stop:
        ball_x += xv
        ball_y += yv
        
        if ball_x < 3 or ball_x + ball_size > 300:
            xv = xv * -1
        if ball_y < 3 or ball_y + ball_size > 250:
            yv = yv * -1
            if ball_y > 200:
                stop = True
        
        if paddle1_x < ball_x < paddle1_x + 50 and 227 < ball_y < 240:
            yv *= -1
            score1 += 1
        
        if paddle2_x < ball_x < paddle2_x + 50 and 227 < ball_y < 240:
            yv *= -1
            score2 += 1
        
        if score1 < 0:
            score1 = 0
        
        if score2 < 0:
            score2 = 0
        
        if paddle1_x + 50 > 150:
            paddle1_x = 100
        
        if paddle1_x < 0:
            paddle1_x = 0
        
        if paddle2_x < 150:
            paddle2_x = 150
        
        if paddle2_x + 50 > 300:
            paddle2_x = 250
        
        gc.delete("all")
        gc.create_line(150, 0, 150, 250, fill="white")
        gc.create_rectangle(paddle1_x, paddle1_y, paddle1_x + 50, paddle1_y + 10, fill="white")
        gc.create_rectangle(paddle2_x, paddle2_y, paddle2_x + 50, paddle2_y + 10, fill="white")
        gc.create_oval(ball_x, ball_y, ball_x + ball_size, ball_y + ball_size, fill="white")
        score1_label['text'] = "Score: " + str(score1)
        score2_label['text'] = "Score: " + str(score2)
        tk.update()
        sleep(0.01)
        if score1==10 or score2==10:
            stop = True
    game()
