import string
from words import choose_word
from images import IMAGES

# End of helper code
# -----------------------------------
def ifValid(user_input):
    if len(user_input) != 1:
        return False

    if not user_input.isalpha():
        return False

    # True , we are doing return when
    # the lenght of user input is 1 and that character
    return True
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: it is the string which is guessed by user
    letters_guessed: It is a list, In which the letter is there which is not guess by user
    returns: It will return True if all letters which is guess by user are in secret_word,
      otherwise false
    '''
    if secret_word == get_guessed_word(secret_word, letters_guessed):
        return True

    return False

# to test this function you can call get_guessed_word("kindness", [k, n, d])
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: it is the string which is guessed by user
    letters_guessed: It is a list, In which the letter is there which is guess by user
    returns: we have to return a string which is guess by user and left it will leave underscore
    eg If secret_word = "kindness", letters_guessed = [k,n, s]
    then we'll do "k_n_n_ss"
    '''

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: It is a list, In which the letter is there which is not guess by user
    returns: string, we have to print all those letters which is not guess by user
    eg If letters_guessed = ['e', 'a'] then we have to return remaining characters
    that is`bcdfghijklmnopqrstuvwxyz' like this
    '''
    import string
    letters_left = string.ascii_lowercase
    for i in letters_guessed:
        letters_left = letters_left.replace(i, "")

    return letters_left

    # hint function
def get_hint(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek character jo abhi tak guess nahi hua hai
    '''
    import random
    letters_not_guessed = []
    for i in secret_word:
        if i not in letters_guessed:
            if i not in letters_not_guessed:
                letters_not_guessed.append(i)

    return random.choice(letters_not_guessed)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Hangman game will start this:
    * In the starting of , this game there is already metioned that how many words are in secret word
    * in every round , this will ask user to guess one letter
    * after every guess , just give the feedback to user how may letters exist or not
    *after every guess , just show that words which is guess by user and how may remaining letters are left also
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

    letters_guessed = []
    Total_lives = remaining_lives = 8
    images_selection = [0,1,2,3,4,5,6,7]
    level = input("enter the level in which you want to play""\n""a for easy""\n""b for medium""\n""c for hard""\n""enter your option: ")
    if level == "b":
        Total_lives = remaining_lives = 6
        images_selection = [1,2,3,4,5,6,7]

    elif level == "c":
        Total_lives = remaining_lives = 4
        images_selection = [1,3,5,7] 
    else:
        if level != "a":
            print("your choice is invalid""\n""game is starting in easy level")

    while (remaining_lives > 0):
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: " + available_letters)

        guess = input("Please guess a letter: ")
        letter = guess.lower()
        # for hint
        if letter == "hint":
            print("your hint for this secret word is  " + get_hint(secret_word,letters_guessed))

        else:
            if (not ifValid(letter)) and letter != "hint":
                print("invalid input")
                continue

        if letter in secret_word:
            letters_guessed.append(letter)
            
            print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print("")

            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ")
                print("")
                break

        else:
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            letters_guessed.append(letter)
            print(IMAGES[images_selection[Total_lives - remaining_lives]])
            print("")
            remaining_lives = remaining_lives - 1
            print("remaining_lives :", str(remaining_lives))
    else:
        print("sorry you ran out of guesses the word was "  +  str(secret_word))        

    
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)