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
