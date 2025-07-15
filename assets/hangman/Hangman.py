import random
from Words_for_hangman import word_list

# Function to get a random word from the word list
def get_word():
    word = random.choice(word_list)
    return word.upper()

# Function to display the hangman based on remaining tries
def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           |
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |  
           |
        """,
        """
           -----
           |   |
           |   O
           |  
           |  
           |
        """,
        """
           -----
           |   |
           |  
           |  
           |  
           |
        """,
        """
           -----
           |  
           |  
           |  
           |  
           |
        """,
    ]
    return stages[max(0, min(tries, len(stages) - 1))]

# Main function for playing the game
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    total_attempts = 6
    tries = total_attempts

    print("Welcome to Hangman!!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    # Loop until the word is guessed or tries run out
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()

        # Check if the guess is a single letter
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is correct!")
                guessed_letters.append(guess)
                # Update the word completion
                word_as_list = list(word_completion)
                indexes = [i for i, letter in enumerate(word) if letter == guess]
                for index in indexes:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        # Check if the guess is a whole word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed that word", guess)
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid guess.")

        # Show the current state of the hangman and word completion
        print(display_hangman(tries))
        print(word_completion)
        print(f"Total attempts: {total_attempts}, Remaining attempts: {tries}\n")

    # Messages for winning or losing
    if guessed:
        print("Congratulations, you've guessed the word! You Win!!")
    else:
        print("Sorry, you are out of tries. The correct word is", word + ". Good luck next time!")

# Main function to control the game flow
def main():
    word = get_word()  # Get a random word
    play(word)  # Start the game
    # Loop to allow replaying the game
    while input("Play again? (Yes/No)").upper() == "YES":
        word = get_word()  # Get a new word
        play(word)  # Start a new game

# Entry point of the program
if __name__ == "__main__":
    main()  # Run the main function