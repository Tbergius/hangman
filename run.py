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
    Track the guesses from player. Add number of attempts (8 now, can change).
    Check the win conditions
    """
    words = load_words()
    word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = set()
    max_attempts = 8
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    display_word(word, guessed_letters)

    while len(incorrect_guesses) < max_attempts and not set(word).issubset(guessed_letters):
        guess = get_user_input(guessed_letters | incorrect_guesses)
        if guess in word:
            guessed_letters.add(guess)
        else:
            incorrect_guesses.add(guess)
        display_word(word, guessed_letters)
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Attempts remaining: {max_attempts - len(incorrect_guesses)}\n")

    if set(word).issubset(guessed_letters):
        print(f"Congrats! You guessed the word: {word}")
    else:
        print(f"Game over :( The word was: {word})")

    while True:
        guess = get_user_input(guessed_letters)
        guessed_letters.add(guess)
        display_word(word, guessed_letters)


if __name__ == "__main__":
    main()