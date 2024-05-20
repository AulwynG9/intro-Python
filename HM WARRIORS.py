import random

# Function to check if the word has been guessed
def check_word(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

# Function to display the hangman
def display_hangman(incorrect_guesses):
    hangman_display = [
        '''
         ------
         |    |
         |
         |
         |
         |
        ---
        ''',
        '''
         ------
         |    |
         |    O
         |
         |
         |
        ---
        ''',
        '''
         ------
         |    |
         |    O
         |    |
         |
         |
        ---
        ''',
        '''
         ------
         |    |
         |    O
         |   /|
         |
         |
        ---
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |
         |
        ---
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   /
         |
        ---
        ''',
        '''
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        ---
        '''
    ]
    print(hangman_display[incorrect_guesses])

# Function to play Hangman game
def play_hangman(word):
    guessed_letters = []
    incorrect_guesses = 0

    print("Let's play HM Warriors Hangman!")
    print("Try to guess the word. You can guess one letter at a time.")
    
    while incorrect_guesses < 6:
        display_hangman(incorrect_guesses)

        # Display the current word with blanks for unidentified letters
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in word:
            print("Good job! That letter is in the word.")
            guessed_letters.append(guess)
            if check_word(word, guessed_letters):
                display_hangman(incorrect_guesses)
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            print("Oops! That letter is not in the word.")
            guessed_letters.append(guess)
            incorrect_guesses += 1

    if incorrect_guesses == 6:
        display_hangman(6)
        print("Sorry, you've run out of guesses. The word was:", word)

# Main function
if __name__ == "__main__":
    word_list = ["hangman", "warriors", "battle", "story", "item", "shop"]
    word = random.choice(word_list)
    play_hangman(word)
 
