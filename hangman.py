import random
from words import words
import string
from ahorcado_munieco import AHORCADO

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    wrong_letters = set()
    while len(word_letters) > 0:
        print('You have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letters = input('Guess a letter: ').upper()
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
            else:
                wrong_letters.add(user_letters)
                try:
                    print(AHORCADO[len(wrong_letters)])
                except Exception:
                    print('You already lost, sorry. Try again.')
                    break
        elif user_letters in used_letters:
            print('You have already used that character. Please try again.')
            
        else:
            print('Invalid character. Type again')
    if word_letters == 0:
        print(f'Congratulations! The word was {word}')
    else:
        print(f'The word was {word}')
            
hangman()