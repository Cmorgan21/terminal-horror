# Terminal Horror

Terminal Horror is a Python Terminal Horror Adventure game. This game is all about discovering what nature the entity is based upon it's traits. You enter the terminal horror mansion where this entity lays

**Author:** Callum Morgan

**Game Link:** [Play Terminal Horror]()

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Design](#design)
4. [Development](#development)
5. [Testing and Validation](#testing-and-validation)
6. [Bugs and Fixes](#bugs-and-fixes)
7. [Deployment](#deployment)
8. [Local Setup](#local-setup)
9. [Technologies](#technologies)
10. [Credits](#credits)
11. [Acknowledgments](#acknowledgments)

## Features

### Introduction

- The start of the programme gives you a brief introduction of what the game is and what your objective it.
- It also gives you an introduction to a character you will be meeting within the game
- The user will be asked if they are ready to play the game. If the user inputs a number, incorrect character or nothing. They will be redirected to the question with an explination of what they need to do

- When sucessful the user will then be promted for their name

- ![Introduction]()

### Game Introduction

- The user will be given an introduction and a rundown to the story of what is going on and what their objective is.

- A backstory will be given to support user experience. This is all done with a type writing affect to create ambience

- The user will be prompted again if they are ready to take on the challenge - giving the user opportunity to engage with the game

### Haunted House ASCII

-[Haunted House ASCII]()

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

- ![Rooms Display]()

### NoteBook

User is supplied with a notenook which has a variety of uses throughout the game

- #### Hints

  - The user can access hints to support them within the game. Specifically what to look for in terms of decriptions when they are checking the ghosts traits

  - This will give the user a better idea of what they are actual

- #### Ghost Traits

  - The ghost traits section gives a brief description of the entities that it could possibly be.

  - It also gives 3 differnt traits that all of them carry. This is how the user will begin to decide which one it could be. By narrowing them down

- #### Guessing the Ghost

  - Guessing the ghost section displays the list of ghosts that there are to to guess from. It will also explain that you only have two guesses.

  - When a user has made their guess. It will give the user feedback if it is right or wrong. If it is wrong the next time they go to guess. It will warn them they only have the one guess

  - #### Writing Notes

  - This allows the user to write notes of their own while they are playing the game to support them

  - Once they have writted their notes this will be stored in an excel sheet ready to be previewed

- #### Viewing Notes
  - When a user views their notes they have made within the gaming session these notes will be fetched and displayed within the terminal from the sheets

### Item Options

- When the user has chose a room to investigate they will be displayed with three items within each room.

- The user will be given instructions of what to type to access the descriptions of the items.

### Winning the game

- When the user wins the game they will be prompted with a congradualtions and a small section of text

- They will also be asked if they would like to play the game again or not and are given the option

### Losing the games

- If the user loses the game thet will be displayed with a Losing text and better luck next time! They will also be told what the actual nature of the ghost was.

- The user will be asked if they would like to play again or not too!

### Restart the game

- The user will be given the option to play the game again or exit the game completely after winning or losing the game. This will save the user from having to exit the website entirely

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
