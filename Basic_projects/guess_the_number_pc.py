import random

# user input
# def guess_pc(x):
#     randomNum = random.randint(1,x)
#     guess = 0
#     score = 5
#     while guess != randomNum and score != 0:
#         guess = int(input("Enter the number: "))
#         if guess < randomNum:
#             print('Sorry too low, try again! ')
#             score -=1
#         elif guess > randomNum:
#             print("Sorry two high, try again! ")
#             score -=1
#     if(score > 0):
#         print(f'Yay, you win! your score is {score}')
#     else:
#         print(f'You loose! your number is {randomNum}')
    
# guess_pc(100)

# pc guess

# def guess_user(x):
#     randomNum = 0 
#     score = 5
#     while x != randomNum and score > 0:
#         if randomNum > x:
#             print(f'Too high, Try again pc')
#             randomNum = random.randint(x,randomNum)
#             score -=1
#         elif randomNum < x:
#             print(f'Too low,Try again!')
#             randomNum = random.randint(randomNum,x)
#             score -=1
#     if score > 0:
#         print(f'Computer You win, your score {score}')
#     else:
#         print(f'Computer you loose, your score {score}')
# y = int(input("Enter the number too guess: "))
# guess_user(y)

# the program is correct in it's own way but it is not much 
# user interactive

# so we generate a feedback based system so end user can give
# lower and higher estimation  rather than system

def guess_user(x):
    low = 1
    high = x
    feedback = ''
    while feedback !='c':
        if low != high:
            randomNum = random.randint(low,high)
        else:
            randomNum = low # either high since low=high
        feedback = input(f'Is the {randomNum} correct(c),low(l) or high(h)!').lower()
        if feedback == 'h':
            high = randomNum-1
        elif feedback == 'l':
            low = randomNum+1
    print(f'You guessed the number right')
y = int(input("Enter the number too guess: "))
guess_user(y)
