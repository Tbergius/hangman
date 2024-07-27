import random

def load_words():
    """
    Loads a list of words for the Hangman game.
    """
    return ["python", "hangman", "challenge", "programming", "developer"]


def main():
    """
    Main function to start the Hangman game.
    """
    words = load_words()
    print("Welcome to Hangman!")


if __name__ == "__main__":
    main()