import random

def load_words():
    """
    Loads a list of words for the Hangman game.
    """
    return ["python", "hangman", "challenge", "programming", "developer"]


def main():
    """
    Main function to start the Hangman game.
    Select a random word.
    """
    words = load_words()
    word = random.choice(words)
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")


if __name__ == "__main__":
    main()