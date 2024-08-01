# Command line based Python game - Hangman

## Introduction
Thank you for viewing my third project from the Full Stack Developer course. This time I will take you along Hangman, a command line based game created with Python.
This README will give you some more insights on my journey.
- You can find the live link here: [https://tbergius-hangman-219834a76c84.herokuapp.com/](https://tbergius-hangman-219834a76c84.herokuapp.com/)
## 1. Purpose of the project
For this project I wanted to create a game, and I picked a word guessing game as it came close to something else I am learning: a new language. Not coding, but the Bulgarian language. As I am far from speaking it, I made it English only. 
## 2. User stories:
### New players:
- As a new player, I want to understand the game's purpose and rules quickly.
- As a new player, I want to navigate the game easily.
- As a new player, I want to feel a sense of achievement while playing.
### Returning players:
- As a returning player, I want to easily follow the game information.
- As a returning player, I want to interact with the game without issues.
- As a returning player, I want to guess (new) words with fewer guesses.

## 3. Features
- **Welcome Message:** Introduces the game and explains the rules.
- **Word Display:** Shows the word with guessed letters and underscores for missing ones.
- **Player's Guess:** Prompts the player to guess a letter and checks the input.
- **Feedback:** Provides feedback on guessed letters and remaining attempts.
- **Game Over Messages:** Displays a message when the player wins or loses.

## 4. Future Features

- Add graphics or ASCII art for visual enhancement.
- Introduce a multiplayer option to play against another player.
- Include game statistics and leaderboards for player progression and achievements.

## 5. Blueprint

A detailed plan was created to guide the game's development. Adjustments were made to improve user experience and address any issues. Every step was tested to ensure it was working before moving on to the next stage. The blueprint was refined during development.

- ![Flow Chart](https://github.com/Tbergius/hangman/blob/main/assets/hangman_bp.png)

## 6. Technology
- [**GitHub**](https://github.com/) - For version control and code repository
- [**Gitpod**](https://gitpod.io/) - For writing the code
- [**Code Institude template**](https://github.com/Code-Institute-Org/python-essentials-template)- To start with the base of writing the code and have the basic programs and files
- [**Python**](https://en.wikipedia.org/wiki/Python_(programming_language)) - The programming language of this project
- [**Heroku**](https://www.heroku.com/) - To deploy the working program
- [**Code Institude PEP8 validator**](https://pep8ci.herokuapp.com/) - To check python code and deployability on Heroku
- [**ExtendsClass Python syntax check**](https://extendsclass.com/python-tester.html) - To check the Python code syntax (Python 3), and find Python errors

## 8. Testing
Testing was done throughout coding of the project. Wrong replies were given, such as numbers, multiple letters, words, gibberish. 
Examples of testing during coding:
- Line 31, the leading " was at the wrong spot, it should have been after the opening (. This was fixed
![Error comma image](https://github.com/Tbergius/hangman/blob/main/assets/wrong_place_comma.png)

- Writing by hand, instead of copying, can result in code not working. Such a using display_word instead of display_words
![Typo image](https://github.com/Tbergius/hangman/blob/main/assets/typo_words.png)

### 8.1 Test cases


### 8.2 Code Validation
The code was checked via the online PEP8 checker from Code Institude. During the test a heap of inconsitansies such as no double line breaks, and user text that extends the broder of the terminal was found, and adjusted.
Also ran it through ExtendsClass Python syntax checker for syntax errors, this came back all good.

- PEP8 Python Validator Results
![PEP8 Python Validator results](https://github.com/Tbergius/hangman/blob/main/assets/ci_pep.png)

- ExtendsClass Python syntax checker
![ExtendsClass Python syntax checker results](https://github.com/Tbergius/hangman/blob/main/assets/extendsclass.png)


### 9. Deployment
For the coding in Gitpod, and hosting on Heroku
### To load the project in Gitpod, please follow these steps:

- Login or Sign Up to Gitpod
- Click on New Workspace
- Enter the repository url created from a template, or your own url if you worked on it before in a different environment. This URL will be the Github repository URL
- Wait for it to load, and select it from the drop-down menu
- Click on continue
- Wait until the workspace loads
- Happy coding!

### Hosting on Heroku:
- Login or Sign Up to Heroku
- Link the repository from your Github project
- Add the buildpacks Python and Node.js in that order
- In the config var settings: set the KEY to PORT, and the Value to 8000
- Manually deploy the Main branch, launch the application

## 10. Credits
