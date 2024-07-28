import random

def load_words():
    """
    Loads a list of words for the Hangman game.
    """
    return ["python", "hangman", "challenge", "programming", "developer"]

def display_word(word, guessed_letters):
    """
    Show the current state of the word with guessed letters and underscores for missing letters.
    Args:
        word (str): The word to guess.
        guessed_letters (set): The set of letters that have been guessed.
    """
    display = [letter if letter in guessed_letters else '_' for letter in word]
    print (' '.join(display))

def get_user_input(guessed_letters):
    """
    Promts player to guess a letter, validating for letter.
    Args:
        guessed_letters (set): The set of letters that have been guessed.
    Returns:
        str: A valid guessed letter.
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
            return guess
        print("Invalid input. Please enter a single letter that you did not guess before.")

def main():
    """
    Main function to start the Hangman game.
    Select a random word.
    Display the word state.
    """
    words = load_words()
    word = random.choice(words)
    guessed_letters = set()
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    display_word(word,guessed_letters)

    while True:
        guess = get_user_input(guessed_letters)
        guessed_letters.add(guess)
        display_word(word, guessed_letters)


if __name__ == "__main__":
    main()