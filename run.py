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
    ghost_names = ghost_worksheet.col_values(1)[1:]
    random_ghost = random.choice(ghost_names)
    generate_clues(random_ghost)
    game_tracker_worksheet.update_acell('B2', random_ghost)


def generate_clues(ghost):
    """
    Generates clues for the ghost and updates Google Sheets with descriptions of items in cells for the generated ghost.
    """
    room_worksheet = SHEET.worksheet('Rooms')
    cell_list = []

    # Define a dictionary with ghost names as keys and a list of cell data as values
    ghost_clues = {
        "Banshee": [
            {"row": 2, "column": 6, "description": "The mirror is rusted with an old-fashioned like pattern. The cobwebs and dust hug the mirror. Visisble finger prints as if someone's trying to escape"},
            {"row": 4, "column": 4,
                "description": "The rusted microwave covered with nothing but old food. In the reflection a faint ball of light almost as if its an orb floats in the background"},
            {"row": 6, "column": 8, "description": "The small flickers of the old lamp reflect on the wall as a faint shadow darts across the wall"}
        ],
        "Demon": [
            {"row": 3, "column": 6, "description": "an old, weathered cot nestled in the corner. The wooden frame creaks as you approach it faint, ethereal writing etched into the timeworn wood. The letters appear to have been inscribed by an unseen hand"},
            {"row": 4, "column": 8, "description": "a solitary window, its glass frosted over with an icy veneer. As you draw near, an unmistakable coldness envelops you, seeping from the glass pane. The frost patterns etched upon the window"},
            {"row": 5, "column": 4,
                "description": "a series of broken and splintered wooden boards. These boards are not just broken; they bear the unmistakable mark of something unusual. Faint claw marks, almost translucent in appearance, are imprinted upon the shattered wood"}
        ],
        "Jinn": [
            {"row": 2, "column": 4, "description": "The curtains, once opulent and regal, now hang in tatters, their deep crimson color faded and frayed. But what truly captures your attention is the unusual phenomenon occurring around them—freezing temperatures that seem to emanate from the very fabric."},
            {"row": 3, "column": 8, "description": "A relic of a bygone era, emits a low, intermittent static that fills the room with a chilling sense of foreboding. As you approach the screen begins to flicker ferociously"},
            {"row": 6, "column": 4,
                "description": "The lampshade is tattered and frayed. What truly catches your eye, however, are the eerie and unexplainable white smudged hand print all over it"}
        ],
        "Shade": [
            {"row": 2, "column": 8,
                "description": "A beautiful yet eerie painting adorns one of the walls. The room exudes an unsettling ambiance, with the air growing noticeably colder. The light begins to flicker as if it's possesed"},
            {"row": 3, "column": 4,
                "description": "Shrouded in an inexplicable coldness, and the temperature drops to freezing levels. The chilling atmosphere seems to intensify around the rocking chair, leaving you with an eerie sensation that something spectral is lurking nearby..."},
            {"row": 5, "column": 8,
                "description": "You notice strange writing etched onto the clock's face, seemingly appearing out of nowhere. The cryptic messages and symbols suggest a haunting presence, and the ghostly aura in the hallway grows stronger"}
        ],
        "Wraith": [
            {"row": 3, "column": 8,
                "description": "The beaten up baby monitor with a shallow light eminating from it as you approach you hear something come from it...\n I.. I'm comin\n coming for YOU!"},
            {"row": 5, "column": 6,
                "description": "In the midst the dim light, you catch a glimpse of an elusive, shadowy tall figure darting across the corridor."},
            {"row": 6, "column": 6,
                "description": "As you approach the TV, you notice an unsettling presence, its lights flickering and beeping erratically. It's as though the spirits of the past are trying to communicate through this old, haunted television."}
        ],
    }
