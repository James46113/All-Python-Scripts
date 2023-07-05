from random import choice


def win():
    global player_score
    print("You win!")
    player_score += 1


def lose():
    global computer_score
    print("Computer wins!")
    computer_score += 1


def draw():
    print("Draw!")


player_score = 0
computer_score = 0

while player_score < 10 and computer_score < 10:
    user_input = input("Rock, paper or scissors: ")
