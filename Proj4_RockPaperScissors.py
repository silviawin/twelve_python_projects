import random


# r > s, s > p, p > r

def play():
    user = input("Please Choose:'r' for rock, 'p' for paper and 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    print(computer)

    if user == computer:
        return "It\'s a tie."
    if is_win(user, computer):
        return "You won!"
    return "You lost"


# return true if the player wins

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True

print(play())