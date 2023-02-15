# Battleship Game

## Python Portfolio Project 3

![Image of game title](assets/readme-images/title-screenshot.png)

![Image of gameplay](assets/readme-images/gameplay-screenshot.png)

## Introduction
This battleship game was developed for Portfolio Project 3 as part of the Code Institute Diploma in 
Full-Stack Software Development. This project focuses on Python Essentials. It is designed to be played
within the Code Institute mock terminal hosted on Heroku - [Link to game](https://portfolio-project-3-battleship.herokuapp.com/)

The aim of the game is to sink all of your opponents ships before they sink yours. In this case
the user plays agains the computer. It is based on the classic battleship board game, rules for
this can be found [here](https://www.cs.nmsu.edu/~bdu/TA/487/brules.htm)

Using a command-line interface, the user can select rows and columns to guess where the computer's
ships are positioned. Each time the user makes a guess the board is updated and the user is informed
of whether they scored a hit or a miss. This continues until either the user or the computer sinks
all of their opponents ships and therefore win the game.

## User Experience & Game Goals
- The aim as a developer was:
  - To build an easy to play game that was enjoyable
  - To allow the user to select their own difficulty

- As a user I want to:
  - Understand the rules of the game
  - Consistent feedback on input and right/wrong guesses
  - Enjoy the game
  - Increase or decrease the difficulty if I want to play again

## Design

### Game Logic
![Flowchart for design of game](assets/readme-images/flowchart-screenshot.png)

The first step in the design of this game was to create a flowchart in [Lucidchart.com](https://www.lucidchart.com/pages/)
to plan the structure and logic of the game. As can be seen in the chart the game runs through 
initial stages of verifying user name, difficulty and start choice before looping on the guess
stage until a win is detected.

### Code Structure

An Object-Oriented approach was used in the development of this game so 4 classes were created;
board, ship, validation & admin. These were used to handle specific areas of the game:
- Board
  - Creates a board in the style of a grid which can be altered as ships added & guesses made
  - Contains methods to print out the board and to clear the board if needed
- Ship
  - Creates locations for 1-3 ships depending on game difficulty
  - Contains methods to test for free locations, position ships and mark them on the board
- Validation
  - Contains methods to test if input is valid and raise a ValueError if it is not
- Admin
  - Creates an instance of the game containing the conditions and elements needed to play
  - Contains methods to complete running of game:
    - Verifies correct amount of spaces taken up by ships
    - Sets game conditions based on difficulty choice
    - Takes user guess and generates computer guess
    - Checks guesses to see if they are a hit or miss and marks board appropriately
    - Displays current game status; boards, scores etc.
    - Checks if either player has won
    - Using time library, simulates loading to improve rhythm of game

### Aesthetic Design
The approach to the look of the game was to keep it minimal and simple, using pops 
of color to highlight specific points. The thinking behind this was to keep the grid
and co-ordinates clear by not trying to over complicate it's design. The color was
added using the [rich](https://github.com/Textualize/rich) library and the title design
was created using an [ASCII text generator](https://fsymbols.com/generators/smallcaps/).

## Features
### Validation
All of the user input is tested using the Validation class for suitability, see below images
for examples of invalid input

![Name Verification](assets/readme-images/name-verification-screenshot.png)

![Difficulty Verification](assets/readme-images/difficulty-verification-screenshot.png)

![Start Verification](assets/readme-images/start-verification-screenshot.png)

![Guess Verification](assets/readme-images/guess-verification-screenshot.png)

### Boards
The game functions using 3 boards; a guess board, a board containing user's ships and a board
containing computers ships. Only the guess board and the board containing the user's ships are
displayed and these are both updated after each turn. The board containing the computer's ships is
only used for checking user's guesses.

The boards are navigated using indexing as x & y co-ordinates. So board1[0][0] is designed to
be the value at board1 if x & y co-ordinates are (0, 0).

Once a guess is generated, the board is checked at these co-ordinates and then marked 'X' if a
hit or 'o' is a miss.

![Board screenshot](assets/readme-images/board-screenshot.png)

### Scores
Each player's score is incremented every time they hit a ship. Once they reach the target score 
they win the game.

![Scores](assets/readme-images/scores-screenshot.png)

## Technologies Used
- Languages:
  - [Python](https://www.python.org/)

- Packages:
  - [Random](https://docs.python.org/3/library/random.html?highlight=random#module-random): Used to generate ship positions
  - [Time](https://docs.python.org/3/library/time.html?highlight=time#module-time): Used to display content gradually by using sleep() function
  - [Rich](https://github.com/Textualize/rich): Used to add colour to highlight text
  - [Flake8](https://flake8.pycqa.org/en/latest/): Used as style guide enforcement. Built into Gitpod workspace
  - [Pylint](https://pypi.org/project/pylint/): Used as static code checker. Built into Gitpod workspace

- Websites/Programs/Frameworks:
  - [Gitpod](https://www.gitpod.io/): Used for version control and to develop/commit changes to project
  - [Github](https://github.com/): Used to store the project's code after push from Gitpod
  - [VSCode](https://code.visualstudio.com/): Used to experiment with classes and develop functions before adding to Gitpod
  - [Heroku](https://dashboard.heroku.com): Used for deployment of game
  - [Lucidchart.com](https://www.lucidchart.com/pages/): Used to build game flowchart
  - [ASCII text generator](https://fsymbols.com/generators/smallcaps/): Used to generate game startup logo

## Testing
### Input Validation
Input validation is carried out using the Validation class at every point where the user is asked to 
input data. If the input is not valid a ValueError is raised and input is asked for again. This prevents
the game crashing due to incorrect input. Inputs that are validated are explained further in [Features](#features) section.



## Deployment

## Forking/Cloning Project

## Credits