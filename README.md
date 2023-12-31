# Terminal Horror

Terminal Horror is a Python Terminal Horror Adventure game. This game is all about discovering what nature the entity is based upon it's traits. You enter the terminal horror mansion where this entity lays

**Author:** Callum Morgan

**Game Link:** [Play Terminal Horror](https://terminal-horror-8b6bbf24f4d4.herokuapp.com)

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
   - [Introduction](#introduction)
   - [Game Introduction](#game-introduction)
   - [Haunted House ASCII](#haunted-house-ascii)
   - [Entering the House](#entering-the-house)
   - [Generated Ghost](#generated-ghost)
   - [Room Options](#room-options)
   - [Notebook](#notebook)
     - [Hints](#hints)
     - [Ghost Traits](#ghost-traits)
     - [Guessing the Ghost](#guessing-the-ghost)
     - [Writing Notes](#writing-notes)
     - [Viewing Notes](#viewing-notes)
   - [Item Options](#item-options)
   - [Winning the Game](#winning-the-game)
   - [Losing the Game](#losing-the-game)
   - [Restart the Game](#restart-the-game)
3. [Design](#design)
   - [The Strategy Plane](#the-strategy-plane)
   - [The Scope Plane](#the-scope-plane)
   - [Timing and Scalability](#timing-and-scalability)
   - [The Structure Plane](#the-structure-plane)
   - [The Surface Plane](#the-surface-plane)
4. [Testing and Validation](#testing-and-validation)
   - [Pylint](#pylint)
   - [Error Handling](#error-handling)
5. [Spreadsheet](#spreadsheet)
   - [Ghosts](#ghosts)
   - [Rooms](#rooms)
   - [Rooms Copy](#rooms-copy)
   - [Notebook](#notebook)
   - [Game Tracker](#game-tracker)
6. [Bugs and Fixes](#bugs-and-fixes)
7. [Deployment](#deployment)
8. [Technologies](#technologies)
   - [Python](#python)
     - [Libraries](#libraries)
9. [Future Implementations](#future-implementations)
10. [Tools and Technologies](#tools-and-technologies)
11. [Credits](#credits)

## Features

### Introduction

- The start of the programme gives you a brief introduction of what the game is and what your objective it.
- It also gives you an introduction to a character you will be meeting within the game
- The user will be asked if they are ready to play the game. If the user inputs a number, incorrect character or nothing. They will be redirected to the question with an explination of what they need to do

![Game Introduction](./documentation/screenshots/Introduction-game-name.png)

![Game Introduction 2](./documentation/screenshots/game-introduction-2.png)

- When sucessful the user will then be promted for their name

![Name Prompt](./documentation/screenshots/introduction-name-prompt.png)

### Game Introduction

- The user will be given an introduction and a rundown to the story of what is going on and what their objective is.

- A backstory will be given to support user experience. This is all done with a type writing affect to create ambience

- The user will be prompted again if they are ready to take on the challenge - giving the user opportunity to engage with the game

![In game introduction](./documentation/screenshots/in-game-introduction.png)

![In game introduction 2](./documentation/screenshots/in-game-introduction-2.png)

### Haunted House ASCII

![Haunted House ASCII](./documentation/screenshots/house-ASCII.png)

- The user will be displayed with a visual house created from ASCII to help with the user experince

### Entering the House

- Entering the house you are given a visual description of where you are as the user

- You are given the option where you would like to explore

### Generated Ghost

- When the user decides to take on the challenge. A ghost from a spreadsheet called "Ghosts" is generated from random

- When the ghost is generated this updates specific descriptions based on which ghost it is to indicate descriptions towards their traits.

### Room Options

- When the user enters the house they are displayed with 5 different rooms they can enter. All these rooms have different items and descriptions

- The user will be given a prompt on how to acess these rooms

![Rooms Display](./documentation/screenshots/room-options.png)

### NoteBook

User is supplied with a notenook which has a variety of uses throughout the game

![Notebook](./documentation/screenshots/notebook.png)

- #### Hints

  - The user can access hints to support them within the game. Specifically what to look for in terms of decriptions when they are checking the ghosts traits

  - This will give the user a better idea of what they are actual

![Hints](./documentation/screenshots/hints.png)

- #### Ghost Traits

  - The ghost traits section gives a brief description of the entities that it could possibly be.

  - It also gives 3 differnt traits that all of them carry. This is how the user will begin to decide which one it could be. By narrowing them down

![Traits](./documentation/screenshots/traits.png)

- #### Guessing the Ghost

  - Guessing the ghost section displays the list of ghosts that there are to to guess from. It will also explain that you only have two guesses.

![Guessing ghost option](./documentation/screenshots/guess-ghost.png)

- When a user has made their guess. It will give the user feedback if it is right or wrong. If it is wrong the next time they go to guess. It will warn them they only have the one guess

![Wrong guess](./documentation/screenshots/wrong-guess.png)

![Right Guess](./documentation/screenshots/congradulations-text.png)

- #### Writing Notes

- This allows the user to write notes of their own while they are playing the game to support them

- Once they have writted their notes this will be stored in an excel sheet ready to be previewed

- #### Viewing Notes
  - When a user views their notes they have made within the gaming session these notes will be fetched and displayed within the terminal from the sheets

### Item Options

- When the user has chose a room to investigate they will be displayed with three items within each room.

- The user will be given instructions of what to type to access the descriptions of the items.

![item options](./documentation/screenshots/room-item-option.png)

![item descriptions](./documentation/screenshots/item-descriptions.png)

### Winning the game

- When the user wins the game they will be prompted with a congradualtions and a small section of text

- They will also be asked if they would like to play the game again or not and are given the option

![Congradulations ASCII](./documentation/screenshots/congradulations.png)

![Congradulations text](./documentation/screenshots/congradulations-text.png)

### Losing the games

- If the user loses the game thet will be displayed with a Losing text and better luck next time! They will also be told what the actual nature of the ghost was.

- The user will be asked if they would like to play again or not too!

![Losing the game](./documentation/screenshots/lose-game.png)

### Restart the game

- The user will be given the option to play the game again or exit the game completely after winning or losing the game. This will save the user from having to exit the website entirely

![option to play again](./documentation/screenshots/lose-game.png)

## Design

### The Strategy Plane

- #### Purpose of the game

  - The purpose of the game is for the user to play a fun, adventure and mystery packed horror game

- #### Target Audience

  - The target audience of the terminal horror game is for user's that enjoy problem solving, tense and mystery games or adventures.

- #### Strategy of Game

  - The strategy of the game is to challenge the user and their problem solving skills to crack which entity they are dealing with. Allow the user to think and read between the lines as they uncover the mystery within the horror house. Meanwhile dealing with an earrie ambiance as they play.

  ### The Scope Plane

- #### Project Aim

  - Create a game that is fun and interactive for users that play

  - A game that creates an unsettling spooky feeling as you play

  - Gives the user a vivid image of the game that they are playing through descriptions

  - Gives the user a challenge to use their problem solving skills

  - Gives user clear feeback and clear instructions whatever they decide to do within the game

- #### Features

  - When the users initiates the game - they will be given an introduction to the game told what they have to do and what to expect. The user is given the option to play the game or not

  - After the user decides to join the game - they will be introducted to an in-game personaility 'Diablo'. Who will paint the user a story and an environment to better help the user visualise the game they are playing.

  - Rooms are available to investigate when they have started the adventure. They are given 5 rooms to investigate from which all include their own individual items which have their individual descriptions

  - When the ghost has been generated - Some of the items descriptions will be modified within the googlesheets. These are different for each ghost and these hints indicate towards the traits of that individual ghost

  - The notebook is another feature which is displayed when the rooms are displayed. The notebook is also displayed whe the user is investigating a room. This allows the user to write notes and view them. Other features are as follows:

    - A feature included withint the notebook is ghost traits. This allows the user to see all the traits of each ghost that it could potentially be. This allows them to refer back to it and narrow down which ghost it could be depending on the clues they have picked up

    - Another feature that is in the notebook is Guessing the Ghost. This allows the user to take their guess of which ghost they think it is. They are informed they only have two guesses

    - Hints is another feature that is included within the notebook. This can support a user in breaking down the descriptions of the items that they are looking at. Such as reading between the lines and understanding what the traits mean.

- #### Timing and Scalability

  - This code was disected into short sprints due to limited time.

  | Sprint 1             | Description                                                                                                                                                          |
  | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Create Logic Diagram | Creating a logic diagram allowed me to break down the code into smaller sections and made the final objective much more comprehendable                               |
  | Create Mind Map      | Creating a mind map gave me a better idea on all the contents that I wanted to incorperate within the project and assess what could be used within the the timeframe |

  | Sprint 2                    | Description                                                                                                       |
  | --------------------------- | ----------------------------------------------------------------------------------------------------------------- |
  | Initiate Python Application | Initaite the Python Terminal Files and ensure everything is all files are there using the Code Institute Template |
  | Create all functions needed | Implement all functions within the run.py that was broke down using a logic diagram in sprint 1                   |

  | Sprint 3                             | Description                                                                                                                                        |
  | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Initial Commit and Link Spreadsheets | Link the spreadsheets and create all worksheets needed for game. Also commit my first commit to github ready for version control                   |
  | Create content for spreadsheets      | Complete content for spreadsheets to efficiently extract and update data within the python programme and navigate to creating a smooth application |

  | Sprint 4                         | Description                                                                                                                                                                                                         |
  | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Complete Code and Error handling | Finish all code and ensure a smooth application with no erros from pylint. Ensuring all error handling form user inputs and extracting and updating data from spreadsheets is handled clear, consise and gracefully |
  | Complete Readme.md               | Do readme.md of completed project and provide visual exmaples of code and game                                                                                                                                      |

### The Structure Plane

- Termianl Horror is a termianl based horror adventure game. Allowing users to use their problem solving skills to figure out the entity's nature.

- The user navigates through the house by typing the room they want to enter, inspecting the items they want to check.

- The user can backout of each section with a clear concise instruction of pressing 'B'

- The user can also take out their notebook at any point of the game too using the instruction of 'N'

### The Surface Plane

- The Surface plane is a text-based terminal game

- This also includes ASCII Designs to make the terminal game more appealing and to break up the text more

- I have also implemented a type-writer like effect to allow users to follow along with the content, this helps with not allowing the user to feel so overwhelmed with text all in one print

- I have also implemented spaces between certain sections of text such as rooms. This is to improve readbility

- Following along this. Through each stage of the terminal clearing function. I have implemented a continue prompt so users get the time to read the content without feeling overwhelmed or rushed.

## Testing and Validation

### Pylint

- I used pylint to ensure my python code was running at maximum efficeincy and any errors and bad handling could be sorted straight away, such as lines being too long and docstrings.

- The only error returned was a few lines being too long, but couldnt be changed due to descriptions. Couldn't chnage this as it would cluster up code

### Error Handling

- I have tested all inputs to ensure all errors get handled gracefully such as. Numbers, Whitespaces, Incorrect characters and too mant characters and nothing being inputted.

- All are provided with clear instructions that the user can't input these and are instructed again what they can input

- Number Error Handling
  ![Number Error Handling](./documentation/screenshots/number-error-handler.png)

- No Input Error Handlings
  ![No input Error Handling](./documentation/screenshots/no-input-error-handler.png)

- Wrong text Error Handling
  ![Wrong text Error Handling](./documentation/screenshots/wrong-input-error-handler.png)

## SpreadSheet

### Ghosts

- The ghosts worksheet was used to display all ghost names and refernce all their ghost traits for eachother

![Ghost worksheet](./documentation/screenshots/ghost-worksheet.png)

### Rooms

- The rooms worksheet was used to displa all rooms, room descriptions, items and item descriptions for the game.

![Rooms worksheet](./documentation/screenshots/rooms-worksheet.png)

### Rooms Copy

- The rooms copy worksheet allows me to reset the original rooms sheet back to normal after the user has played the game. This is due to some of the descriptions changing depending on the ghost

![Rooms Copy worksheet](./documentation/screenshots/rooms-copy.png)

### Notebook

- This worksheet allows all a users notes to be stored in a single column and will display them when the user decides to view them

![Notebook worksheet](./documentation/screenshots/notes-worksheet.png)

### Game Tracker

- The game tracker sheet keeps track of the constants of the game - such as the users name and the entity that was generated - which can later be used for checking if the user guessed the correct entity

![Game Tracker worksheet](./documentation/screenshots/game-tracker-worksheet.png)

## Bugs and Fixes

- One bug that I had while creating this project was User inputs not matching Rooms. When I would enter an input it wouldn't match with the if statemnet to enter the room. This was rectified by printing the users input to see what would come out and use the .strip and .title methods to match the Room names.

- Another bug that I had issues with was viewing the notes and error handling. When the user goes to view notes and they aven't created any. I created a try and exception error handler that would print a message to inform users "You haven't created any notes", but this wouldn't work and would suggest "data is out of range". This was due to there being no data within the spreadsheet.

## Deployment

This website has been deployed using Heroku.

Instructions to deploy using Heroku:

1 - While in Heroku, navigate to dashboard and then click on the new button in the top right corner choosing: create new app.

2 - Input a name for your app (this name will need to be unique) and choose the correct region for where you are located. Click create app.

3 - Your app has been created, now click on the settings tab.

4 - Click reveal config vars to add any keys the application will need. For this project I added the api credentials for my spreadsheet to a key of CREDS and a value of 8000 to a key of PORT.

5 - Click add buildpack to install any interdependecies needed. For this project I installed 'python' and 'nodejs'.

6 - Click on deploy tab. Select deploy method, in this case Git Hub. Confirm connection to git hub by searching for the correct repository and then connecting to it.

7 - To manually deploy project click 'Deploy Branch'. Once built a message will appear saying: Your app was successfully deployed. Click the view button to view the deployed page making a note of it's url.

## Languages and Libraries

### Python

- #### Libraries:

  - time
  - sys
  - random
  - system from OS

  - sleep from time
  - Credentials from google.oauth2.service_account
  - gspread

## Future Implementatios

- One feature I would love to add is a ghost hunting feature. When the user is playing the ghost randomly hunts them and they have to quickly type hide. If they don't they lose. This would happen on random occasions

- Another feature would be a sanity bar. After so much time the users sanity goes down. This would put pressure on the user and create a more tense game. Once it is too low the user loses

## Tools and Technologies

- VSCode: Used for writing and pushing the code to git hub

- Git: Used for version control

- Git hub: Used to store the repository for this project

- Heroku: Used to deploy the website

- Text to ASCII Art Generator: Used to generate the text art

- Excalidraw: Used for creating mind maps and logic diagrams

![Mind map](./documentation/screenshots/rooms-and-ghosts-mindmap.png)

![Mind map 2](./documentation/screenshots/sanity-bar-and-clues-mindmap.png)

- draw.io: Logic Diagram

![Simple Logic Graph](./documentation/screenshots/Simple-logic-graph.png)

## Credits

- I used this website to create my ASCII Designs whcih create a more visual appreance for the terminal game.
  [ASCII Designs Website](https://patorjk.com/software/taag/#p=display&f=Big&t=Terminal%20Horror)

- The use of sleep() and clear() function for the tunnel was taken from the inspiration of [detective-game-p3 project](https://github.com/GeorginaCarlisle/detective-game-p3) Go check it out

- Code Institute has taught me all foundation knowledgde of Python with the Python Essentials Module
