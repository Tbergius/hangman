# Command line based Python game - Hangman

## Introduction
Thank you for viewing my third project from the Full Stack Developer course. This time I will take you along Hangman, a command line based game created with Python.
This README will give you some more insights on my journey.
- You can find the live link here: 
## Hangman Idea
For this project I wanted to create a game, and I picked a word guessing game as it came close to something else I am learning: a new language. Not coding, but the Bulgarian language. As I am far from speaking it, I made it English only. 

## Hangman Game Development
To create a fun and engaging Hangman game, I divided the project into several stages: 
1. Discovery
2. Planning
3. Development
4. Testing
5. Deployment
Each stage helped ensure the game was user-friendly and enjoyable.
### 1. Discovery Phase
### My Goals:
- Make the game easy to use and understand.
- Ensure instructions and messages are clear.
- Create a positive experience for players.
- Keep game feedback relevant and helpful.
- Design a logical game flow that is accessible and simple.
### User Objectives:
### New players:
- Understand the game's purpose and rules quickly.
- Navigate the game easily.
- Feel a sense of achievement while playing.
### Returning players:
- Easily follow the game information.
- Interact with the game without issues.
- Guess (new) words faster. 
### 2. Planning
- Plan the basic logic of the Hangman game.
- Outline the structure of the Python code needed for the game.
- Create a rough blueprint for the logic:
- ![Flow Chart](https://github.com/Tbergius/hangman/blob/main/assets/hangman_bp.png)
### 3. Development Phase
A detailed plan was created to guide the game's development. Adjustments were made to improve user experience and address any issues. Every step was tested to be sure it was working, before resuming with the next stage. During working on this, the blueprint was adjusted and refined as well. The code was written in Gitpod on the base of the Code Institude template.
### 4. Testing
In addition to the above testing while coding, every game step was tested once deployed. Wrong replies were given, such as numbers, multiple letters, words, gibberish. 
The code was checked via the online PEP8 checker from Code Institude. During the test a heap of inconsitansies such as no double line breaks, and user text that extends the broder of the terminal was found, and adjusted.
Also ran it through ExtendsClass Python syntax checker for syntax errors, this came back all good.

Examples of testing during coding:
- Line 31, the leading " was at the wrong spot, it should have been after the opening (. This was fixed
![Error comma image](https://github.com/Tbergius/hangman/blob/main/assets/wrong_place_comma.png)

- Writing by hand, instead of copying, can result in code not working. Such a using display_word instead of display_words
![Typo image](https://github.com/Tbergius/hangman/blob/main/assets/typo_words.png)

- PEP8 Python Validator Results
![PEP8 Python Validator results](https://github.com/Tbergius/hangman/blob/main/assets/ci_pep.png)

2. ExtendsClass Python syntax checker
![ExtendsClass Python syntax checker results](https://github.com/Tbergius/hangman/blob/main/assets/extendsclass.png)


### 5. Deployment
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

## Credits
### Tools used:
[**GitHub**](https://github.com/) - for pushing the code
[**Gitpod**](https://gitpod.io/) - for writing the code
[**Code Institude template**](https://github.com/Code-Institute-Org/python-essentials-template)- To start with the base of writing the code and have the basic programs and files
[**Python**](https://en.wikipedia.org/wiki/Python_(programming_language)) - the language of this project
[**Heroku**](https://www.heroku.com/) - to deploy the working program
[**Code Institude PEP8 validator**](https://pep8ci.herokuapp.com/) - check python code and deployability on Heroku
[**ExtendsClass Python syntax check**](https://extendsclass.com/python-tester.html) - check the Python code syntax (Python 3), and find Python errors