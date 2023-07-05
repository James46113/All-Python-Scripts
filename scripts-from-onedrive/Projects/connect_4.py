from time import sleep

eb = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
      [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
      [" ", " ", " ", " ", " ", " "]]

end_game = False
x_win = False
o_win = False


def clear():
    for outer in range(7):
        for inner in range(6):
            eb[outer][inner] = " "


def check_win():
    global end_game
    global eb
    global x_win
    global o_win
    
    # check board full
    if eb[0][5] != " ":
        if eb[1][5] != " ":
            if eb[2][5] != " ":
                if eb[3][5] != " ":
                    if eb[4][5] != " ":
                        if eb[5][5] != " ":
                            if eb[6][5] != " ":
                                end_game = True
    
    # check horizontal
    if not end_game:
        for outer in range(6):
            for inner in range(4):
                if eb[inner][outer] == "X":
                    if eb[inner + 1][outer] == "X":
                        if eb[inner + 2][outer] == "X":
                            if eb[inner + 3][outer] == "X":
                                x_win = True
                                end_game = True
                            
                elif eb[inner][outer] == "0":
                    if eb[inner + 1][outer] == "0":
                        if eb[inner + 2][outer] == "0":
                            if eb[inner + 3][outer] == "0":
                                if eb[inner + 3][outer] == "0":
                                    o_win = True
                                    end_game = True                                
    
    # check vertical
    if not end_game:
        for outer in range(7):
            for inner in range(3):
                if eb[outer][inner] == "X":
                    if eb[outer][inner + 1] == "X":
                        if eb[outer][inner + 2] == "X":
                            if eb[outer][inner + 3] == "X":
                                x_win = True
                                end_game = True
                            
                elif eb[outer][inner] == "0":
                    if eb[outer][inner + 1] == "0":
                        if eb[outer][inner + 2] == "0":
                            if eb[outer][inner + 3] == "0":
                                o_win = True
                                end_game = True
                            
    # check diagonal L to R
    if not end_game:
        for outer in range(4):
            for inner in range(3):
                if eb[outer][inner] == "X":
                    if eb[outer + 1][inner + 1] == "X":
                        if eb[outer + 2][inner + 2] == "X":
                            if eb[outer + 3][inner + 3] == "X":
                                x_win = True
                                end_game = True
                            
                elif eb[outer][inner] == "0":
                    if eb[outer + 1][inner + 1] == "0":
                        if eb[outer + 2][inner + 2] == "0":
                            if eb[outer + 3][inner + 3] == "0":
                                o_win = True
                                end_game = True
                            
    # check diagonal R to L
    if not end_game:
        for outer in range(6, 2, -1):
            for inner in range(3):
                if eb[outer][inner] == "X":
                    if eb[outer - 1][inner + 1] == "X":
                        if eb[outer - 2][inner + 2] == "X":
                            if eb[outer - 3][inner + 3] == "X":
                                end_game = True
                                x_win = True
                elif eb[outer][inner] == "0":
                    if eb[outer - 1][inner + 1] == "0":
                        if eb[outer - 2][inner + 2] == "0":
                            if eb[outer - 3][inner + 3] == "0":
                                end_game = True
                                o_win = True
                            

def draw_board():
    board = [
        ["|", eb[0][5], "|", eb[1][5], "|", eb[2][5], "|", eb[3][5], "|", eb[4][5], "|", eb[5][5], "|", eb[6][5], "|"],
        ["|", eb[0][4], "|", eb[1][4], "|", eb[2][4], "|", eb[3][4], "|", eb[4][4], "|", eb[5][4], "|", eb[6][4], "|"],
        ["|", eb[0][3], "|", eb[1][3], "|", eb[2][3], "|", eb[3][3], "|", eb[4][3], "|", eb[5][3], "|", eb[6][3], "|"],
        ["|", eb[0][2], "|", eb[1][2], "|", eb[2][2], "|", eb[3][2], "|", eb[4][2], "|", eb[5][2], "|", eb[6][2], "|"],
        ["|", eb[0][1], "|", eb[1][1], "|", eb[2][1], "|", eb[3][1], "|", eb[4][1], "|", eb[5][1], "|", eb[6][1], "|"],
        ["|", eb[0][0], "|", eb[1][0], "|", eb[2][0], "|", eb[3][0], "|", eb[4][0], "|", eb[5][0], "|", eb[6][0], "|"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["/", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "\\"]]
    
    for outer in range(len(board)):
        for inner in board[outer]:
            print(inner, end="")
        print()


score_x = 0
score_o = 0
times_played = 0
play_again = True
while play_again:
    if times_played != 0 and times_played % 2 == 1:
        turn = 2
    else:
        turn = 1
    end_game = False
    o_win = False
    x_win = False
    error = False
    play_again = False
    mid_clear = False
    last = []
    clear()
    
    print("Player one's turn\n")
    draw_board()
    play = "0"
    
    while not end_game:
        if error:
            print("Column full!")
            error = False
        column = int(input("Enter column\n>>>")) - 1
        
        if column >= 7:
            for x in range(7):
                for y in range(6):
                    eb[x][y] = play
            
            if play == "0":
                o_win = True
            else:
                x_win = True
        elif column == -1:
            mid_clear = True
            break
        elif column < -1:
            eb[last[0]][last[1]] = " "
        
        else:
            for x in range(len(eb[column])):
                if eb[column][x] == " ":
                    eb[column][x] = play
                    last = [column, x]
                    break
                elif x == 5:
                    error = True
        if not error:
            if turn == 1:
                turn = 2
            else:
                turn = 1
        
        if turn == 1:
            play = "0"
            print("\nPlayer one's turn\n")
        else:
            play = "X"
            print("\nPlayer two's turn\n")
        
        draw_board()
        check_win()
    if not mid_clear:
        print("GAME OVER!")
        sleep(1)
        if x_win:
            score_x += 1
            print("Player two wins!")
        else:
            score_o += 1
            print("Player one wins!")
        sleep(1)
        if times_played > 0:
            print("\nPlayer one score:", score_o, "\nPlayer two score:", score_x)
        sleep(1)
        if input("\nWould you like to play again?\n>>>").lower() != "no":
            play_again = True
        else:
            input("Thank you for playing")
    else:
        play_again = True
        print("RESTARTING...\n\n")
        sleep(1)
