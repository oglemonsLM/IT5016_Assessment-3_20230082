"""
Hangman implementation by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

#imports the random function to select words.
import random 

#imports the list of words from the "words" file.
from words import words 

#imports the ascii images from the "hangman_visual" file.
from hangman_visual import lives_visual_dict

#imports and allows the use of ascii letters later on.
import string

#creates the function for get_valid_word so that a word may be assigned to it.
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

#creates the main function for choosing the word and assigning attributes like lives and and counts for letters in the word.
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    #a loop that will keep going until either the player has won or lost the game.
    while len(word_letters) > 0 and lives > 0:
        #shows the user amount of lives left and letter used.
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        #shows the current word with guesed letters and tells the rest of the code to display the letters that haven't been guessed as a '-'.
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        #this statement will take players input and check it against used letters if it is not in the used letters it will check the word for that letter and decide if it needs to be added to either the word or the letters used list.
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            #takes away a life if a guess is wrong.
            else:
                lives = lives - 1 
                print('\nYour letter,', user_letter, 'is not in the word.')

        #this shows the player that if they guess a letter wrong they have to guess again.
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')
        
        #this is displayed to the user if the character they entered is not a letter or is not recognized by the code and to try again.
        else:
            print('\nThat is not a valid letter.')

    #the code gets to this point if there are either no lives remaining or the player has guessed the word.
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

#checking wether or not the file is running due to import.
if __name__ == '__main__':
    hangman()
