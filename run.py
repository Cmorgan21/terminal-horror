import time
import sys
import random
from os import system

from time import sleep
from google.oauth2.service_account import Credentials
import gspread


def clear():
    """
    Clears the terminal.
    See https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
    system("clear")


def t_print(message, delay=0.05):
    """
    Prints the passed string to the console, simulating a typewriter.
    """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

try:
    SHEET = GSPREAD_CLIENT.open('terminal-horror')
except gspread.exceptions.SpreadsheetNotFound:
    print("The 'terminal-horror' spreadsheet was not found.")
    sys.exit(1)
except ConnectionError as error:
    print(f"An error occurred while opening the spreadsheet: {error}")
    sys.exit(1)


def introduction():
    """
    Introduction for game with description of what the game is about
    """
    user_info_worksheet = SHEET.worksheet('Game Tracker')
    terminal_title = """
      _______                  _             _   _    _                           
     |__   __|                (_)           | | | |  | |                          
        | | ___ _ __ _ __ ___  _ _ __   __ _| | | |__| | ___  _ __ _ __ ___  _ __ 
        | |/ _ \\ '__| '_ ` _ \\| | '_ \\ / _` | | |  __  |/ _ \\| '__| '__/ _ \\| '__|
        | |  __/ |  | | | | | | | | | | (_| | | | |  | | (_) | |  | | | (_) | |   
        |_|\\___|_|  |_| |_| |_|_|_| |_|\\__,_|_| |_|  |_|\\___/|_|  |_|  \\___/|_|                                                                           
    """

    print(terminal_title)
    t_print("Welcome to the Terminal Horror")
    t_print("Prepare to step into a world shrouded in darkness, where secrets lie within every creaking floorboard and shadowed corner.")
    sleep(2)

    t_print("Before you stands Diablo, a seasoned paranormal investigator with an air of mystery and a haunted past.")
    t_print("He's sought the truth in countless haunted places, but none compare to the dread that lurks within the Terminal Horror Mansion.")
    sleep(3)

    t_print("Whispers of the mansion's malevolent reputation have reached your ears.")
    t_print(
        "Teenagers have gone missing, and no one has ventured near the place for decades.")
    t_print("The mansion, a chilling enigma, beckons you to uncover its secrets.")
    sleep(3)

    while True:
        answer = input(
            "Will you take on this paranormal phenomenon adventure?(Y/N): ").strip().upper()
        print("")

        if answer == "N":
            t_print("Ah, it seems you aren't what we're looking for...")
            t_print("Fear not. Not everyone is cut out for such an ominous task.")
            t_print(
                "But remember, the Terminal Horror Mansion's secrets will remain hidden...")
            sleep(2)
            break

        elif answer == "Y":
            t_print("Brave soul, you've accepted the challenge.")
            t_print(
                "Prepare yourself to confront the supernatural and uncover the truth.")
            while True:
                name = input("What is your name: ").strip()
                if not name:
                    print(
                        "I'm sorry, but we need to know your name for the investigation.")
                    continue
                elif name.isdigit():
                    print("Your name cannot be a number. Please enter a valid name.")
                    continue
                else:
                    try:
                        user_info_worksheet.update_acell('A2', name)
                        clear()
                        start_game(name)
                        break
                    except ConnectionError as e:
                        print(
                            f"An error occurred while updating user info: {e}")
                        break
        elif answer == "":
            print(
                "Empty input. Please enter 'Y' to start the adventure or 'N' to decline.")
            print("")
        else:
            if any(char.isdigit() for char in answer):
                print(
                    "Invalid choice. Please enter 'Y' to start the adventure or 'N' to decline.")
            else:
                print(
                    "Invalid choice. Please enter 'Y' to start the adventure or 'N' to decline.")
            print("")


def generate_ghost():
    """
    Generates Ghost at random using google sheets data and passing it as an argument
    """
    ghost_worksheet = SHEET.worksheet('Ghosts')
    game_tracker_worksheet = SHEET.worksheet('Game Tracker')
