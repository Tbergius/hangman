# Command line based Python game - Hangman

## Introduction
Thank you for viewing my third project from the Full Stack Developer course. This time I will take you along Hangman, a command line based game created with Python.
This README will give you some more insights on my journey.
You can find the live link here: 
## Hangman Idea
For this project I wanted to create a game, and I picked a word guessing game as it came close to something else I am learning: a new language. Not coding, but the Bulgarian language. As I am far from speaking it, I made it English only. 

## Hangman Game Development
To create a fun and engaging Hangman game, I divided the project into several stages: Discovery, Planning, Development, Testing, and Deployment. Each stage helped ensure the game was user-friendly and enjoyable.
### Discovery Phase
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
### Planning
- Plan the basic logic of the Hangman game.
- Outline the structure of the Python code needed for the game.
- Create a rough blueprint for the logic.
### Development Phase
A detailed plan was created to guide the game's development. Adjustments were made to improve user experience and address any issues. Every step was tested to be sure it was working, before resuming with the next stage. During working on this, the blueprint was adjusted and refined as well. The code was written in Gitpod on the base of the Code Institude template.
### Testing
In addition to the above, every game step was tested once deployed. Wrong replies were given, such as numbers, multiple letters, words, gibberish. 
The code was checked via the online PEP8 checker from Code Institude. During the test a heap of inconsitansies such as no double line breaks, and user text that extends the broder of the terminal was found, and adjusted.
Also ran it through ExtendsClass Python syntax checker for syntax errors, this came back all good.
### Deployment
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
Github