import random
import string
from words import words

def get_words(words_list):
    word = random.choice(words_list)
    
    while '-' in word or ' ' in word:
        word = random.choice(words_list)
    
    return word.upper()

def hangman():
    word = get_words(words)
    word_letters = set(word) # converts string to set index with unique values
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    # creating point system
    lives = 7
    while len(word_letters) > 0:

        print('You have', lives, ' lives left and you have used these letters:',' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',' '.join(word_list))

        # ALL THE LOGIC FOR INITAL GAME 
        user_letter = input("Guess a letter: ")
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -=1
                print("\nYou letter", user_letter, ' is not in word')
        
        elif user_letter in used_letters:
            print("\n You have already used the letter.Guess another one.")
        
        else:
            print("\nThat is not a valid letter")
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print("\nYou WIN! your word is : ",word)
hangman()