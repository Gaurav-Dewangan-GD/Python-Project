import random


# rock paper condition to win

# r > s, s > p, p > r

def iswin(user,computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer =='p') \
        or (user == 'p' and computer == 'r'):
        return True

def play():
    user = input("What's your choice ? rock (r) | scissor(s) | paper(p): ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a Tie'
    
    if iswin(user,computer):
        return 'You win'
    
    return 'You lose'
