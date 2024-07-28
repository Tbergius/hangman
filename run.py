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


if __name__ == "__main__":
    main()