# # The secret word the user needs to guess
# secret = "airplane"

# # This function creates a list of underscores for each letter in the word
# def create_dashes(word):
#     dash_list = []  # Empty list to store underscores
#     for letter in word:
#         dash_list.append("_")  # Add one underscore for each letter
#     return dash_list  # Return the list, like ['_', '_', '_', ...]

# # Main game function
# def main():
#     tries = 5  # Total wrong guesses allowed
#     guessed = []  # This list stores the letters guessed by the user
#     display = create_dashes(secret)  # Create the hidden version of the word

#     # Run the game until all letters are guessed or no tries left
#     while "_" in display and tries > 0:
#         print("\nWord: ", " ".join(display))  # Show current progress (e.g. _ _ r _ _ _)
#         print("Tries left: ", tries)

#         guess = input("Enter a letter: ").lower()  # Take input and convert to lowercase

#         # Check if the letter was already guessed
#         if guess in guessed:
#             print("You already guessed that letter.")
#             continue  # Skip this round and ask again

#         guessed.append(guess)  # Add the letter to guessed list

#         # If the guessed letter is in the secret word
#         if guess in secret:
#             # Reveal the letter in the correct positions
#             for i in range(len(secret)):
#                 if secret[i] == guess:
#                     display[i] = guess
#         else:
#             print("Wrong guess.")
#             tries -= 1  # Reduce one try

#     # Game ends: check win or lose
#     if "_" not in display:
#         print("\nCongratulations! You guessed the word:", secret)
#     else:
#         print("\nGame over! The word was:", secret)

# # Start the game
# main()



secret_word = "Airplane"

# This function creates underscores for each letter in the secret word
def make_blanks(word):
    blanks = []
    for letter in word:
        blanks.append("_")
    return blanks

def play_game():
    tries_left = 5
    guessed_letters = []
    current_display = make_blanks(secret_word)

    while "_" in current_display and tries_left > 0:
        # Make the word string to show the user (like: _ _ _ _)
        word_to_show = ""
        for letter in current_display:
            word_to_show = word_to_show + letter + " "
        print("\nWord:", word_to_show)

        print("Tries left:", tries_left)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    current_display[i] = guess
        else:
            print("Wrong guess!")
            tries_left = tries_left - 1

    if "_" not in current_display:
        print("\nGood job! You guessed the word:", secret_word)
    else:
        print("\nSorry! You're out of tries. The word was:", secret_word)

# Start the game
play_game()
