from random import choice, randint
from tkinter import font
from tkinter import *
from time import sleep

tk = Tk()
tk.geometry("300x250+600+250")
tk.resizable(False, False)
tk.attributes('-topmost', True)
tk.title("Pong")
tk.bind('<Escape>', lambda e: tk.destroy())

stop = False
play_again = True

appHighlightFont = font.Font(family='digital-7', size=30, weight='bold')
font.families()

end_pause = IntVar()
bg_c = "black"
fg_c = "white"


def game():
    global gc, score1, score2, score1_label, score2_label
    var = IntVar()
    go = Label(gc, text="GAME OVER!", font=("digital-7", 30), bg=bg_c, fg=fg_c)
    go.place(x=23, y=70)

    again = Button(gc, text="Play again", bg=bg_c, fg=fg_c, command=lambda: var.set(1))
    again.place(x=113, y=160)
    if score1 > score2:
        win = Label(gc, text="Player 1 wins!", font=(None, 20), bg=bg_c, fg=fg_c)
        win.place(x=63, y=117)
    else:
        win = Label(gc, text="Player 2 wins!", font=(None, 20), bg=bg_c, fg=fg_c)
        win.place(x=63, y=117)
    
    tk.wait_variable(var)
    go.destroy()
    again.destroy()
    win.destroy()
    score1_label.destroy()
    score2_label.destroy()
    

def key_press(e):
    global paddle1_y, paddle2_y, score1, stop, play_again, ball_x, end_pause, gc
    if e.keysym == "q" and ball_x < 150:
        paddle1_y -= 15
    if e.keysym == "a" and ball_x < 150:
        paddle1_y += 15
    if e.keysym == "p" and ball_x > 150:
        paddle2_y -= 15
    if e.keysym == "l" and ball_x > 150:
        paddle2_y += 15
    if e.keysym == "Return":
        x = Button(gc, text="►", bg=bg_c, fg=fg_c, font=(None, 30), command=lambda: end_pause.set(1))  # ▶
        x.place(x=115, y=85)
        tk.wait_variable(end_pause)
        x.destroy()


gc = Canvas(tk, bg=bg_c)
gc.bind("<KeyPress>", key_press)
gc.focus_set()
gc.pack()

ball_speed = [-2, 2]

while play_again:
    stop = False
    
    score1 = 0
    score1_label = Label(gc, text="hi", font=("digital-7", 30), bg=bg_c, fg=fg_c)
    score1_label.place(x=100, y=5)
    score1_label['font'] = appHighlightFont
    
    score2 = 0
    score2_label = Label(gc, text="hi", font=("digital-7", 30), bg=bg_c, fg=fg_c)
    score2_label.place(x=170, y=5)
    score2_label['font'] = appHighlightFont
    
    ball_x = 150
    ball_y = 10
    xv = 2
    yv = 2.5
    ball_size = 10
    
    paddle1_x = 5
    paddle1_y = 100
    paddle2_x = 285
    paddle2_y = 100
    
    while not stop:
        ball_x += xv
        ball_y += yv
        
        if ball_x < -10 or ball_x + ball_size > 310:
            
            if ball_x > 100:
                score1 += 1
            else:
                score2 += 1
            if score1 == 10 or score2 == 10:
                stop = True
            else:
                sleep(0.5)
                paddle1_y = 100
                paddle2_y = 100
                xv = choice(ball_speed)
                yv = choice(ball_speed)
                if xv == 2:
                    ball_x = randint(20, 150)
                    ball_y = randint(50, 200)
                else:
                    ball_x = randint(150, 250)
                    ball_y = randint(50, 200)
        
        if ball_y < 3 or ball_y + ball_size > 250:
            yv = yv * -1
        
        if paddle1_y < ball_y < paddle1_y + 50 and 0 < ball_x < 15:
            xv *= -1
        
        if paddle2_y < ball_y < paddle2_y + 50 and 275 < ball_x < 290:
            xv *= -1
        
        if paddle1_y <= 0:
            paddle1_y = 0
        
        if paddle1_y + 50 > 250:
            paddle1_y = 200
        
        if paddle2_y <= 0:
            paddle2_y = 0
        
        if paddle2_y + 50 > 250:
            paddle2_y = 200
        
        gc.delete("all")
        gc.create_line(150, 0, 150, 250, dash=(6, 4), fill=fg_c)
        gc.create_rectangle(paddle1_x, paddle1_y, paddle1_x + 10, paddle1_y + 50, fill=fg_c)
        gc.create_rectangle(paddle2_x, paddle2_y, paddle2_x + 10, paddle2_y + 50, fill=fg_c)
        gc.create_oval(ball_x, ball_y, ball_x + ball_size, ball_y + ball_size, fill=fg_c)
        score1_label['text'] = str(score1)
        score2_label['text'] = str(score2)
        tk.update()
        sleep(0.01)
        if score1 == 10 or score2 == 10:
            stop = True
    game()
