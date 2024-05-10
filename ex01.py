# A variable containing the opening page
HANGMAN_ASCII_ART = "Welcome to the game Hangman\n" + """
  _    _    
 | |  | |   
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
"""


# constant variable- How many (failed) guessing attempts are allowed to a player in the game
MAX_TRIES = 6
print("the max tries that you have is: ", MAX_TRIES)

# The hanging column
HANGMAN_PHOTOS = {
    0: """
    x-------x
    """,
    1: """
    x-------x
    |
    |
    |
    |
    |
    """,
    2: """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    3: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    4: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
}


# A function you implemented at the end of the unit on lists.
# A Boolean function that accepts a character and a list of letters that the user has guessed previously.
# The function checks two things: the correctness of the input and whether it is legal to guess this letter
# (that is, the player has not guessed this letter before) and returns true or false accordingly.
def check_valid_input(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    if (len(letter_guessed) == 1 and letter_guessed.isalpha() and
            letter_guessed not in old_letters_guessed):
        return True
    else:
        return False


# The function uses the check_valid_input function to know if the character is correct
# and has not been guessed before or the character is not correct and/or is already in the list of guesses.
# If the character is incorrect or the character has already been guessed before,
# the function prints the character X (as a capital letter),
# below it the list of letters that have already been guessed and returns false.
# If the character is correct, and it was not guessed before -
# the function adds the character to the list of guesses and returns true.
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        print(' -> '.join(sorted(old_letters_guessed)))
        return False


# A function that returns a string consisting of letters and underscores.
# The string shows the letters from the old_letters_guessed list that are in the
# secret_word string in their appropriate position,
# and the rest of the letters in the string (which the player has not yet guessed) as underlines.
def show_hidden_word(secret_word, old_letters_guessed):
    gamer_progress = []
    for letter in secret_word:
        if letter in old_letters_guessed:
            gamer_progress.append(letter)
        else:
            gamer_progress.append('_')
    return ' '.join(gamer_progress)


# A Boolean function that returns true if all the letters that make up the secret word
# are included in the list of letters that the user guessed.
# Otherwise, the function returns false.
def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


# A function that prints the snapshot of the hanging man using the dictionary defined above.
def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


# The function accepts as parameters: a string representing a path to a text file containing words
# separated by spaces, and an integer representing a position of a certain word in the file.
# The function returns a tuple consisting of two elements in the following order:
# (1) the number of different words in the file
# (2) a word in the position received as an argument to the function (index).
def choose_word(file_path, index):
    count_different_words = set()
    words_in_file = []
    with open(file_path, "r") as file_to_read:
        for line in file_to_read:
            words_to_count = line.split()
            words_in_file.extend(words_to_count)
            count_different_words.update(words_to_count)
            len1 = len(count_different_words)
        if index > len(words_to_count):
            index = (index - 1) % len(words_to_count) + 1
        secret_word = words_in_file[index-1]
        return len1, secret_word


def main():
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    print(HANGMAN_ASCII_ART)
    print("Let’s start!")
    print_hangman(0)
    total_words, secret_word = choose_word(file_path, index)

    old_letters_guessed = []
    num_of_tries = 0
    print(show_hidden_word(secret_word, old_letters_guessed))

    while num_of_tries < MAX_TRIES:
        # the user guess of the letter
        letter_guessed = input("Guess a letter: ")

        # Check for valid input and update letters guessed
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):

            # Check if the guessed letter is in the secret word
            if letter_guessed in secret_word:
                print(show_hidden_word(secret_word, old_letters_guessed))
                pass
            else:
                # if the guess was wrong
                print(":(")
                num_of_tries += 1
                print_hangman(num_of_tries)

        # check if the user won the game
        if check_win(secret_word, old_letters_guessed):
            print("WIN")
            break
        # check if the user lost the game
        elif num_of_tries == MAX_TRIES:
            print("LOSE! The word was:", secret_word)
            break


if __name__ == "__main__":
    main()
