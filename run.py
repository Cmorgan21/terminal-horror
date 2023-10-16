import time
import sys
import random
from os import system

from time import sleep
import gspread
from google.oauth2.service_account import Credentials

# Function to clear the terminal screen


def clear():
    """
    Clears the terminal.
    See https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
    """
    system("clear")

# Function to print text as if it's being typed like a typewriter


def t_print(message, delay=0.05):
    """
    Prints the passed string to the console, simulating a typewriter.
    """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# Define the scope and Google Sheets credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Try to open the 'terminal-horror' spreadsheet
try:
    SHEET = GSPREAD_CLIENT.open('terminal-horror')
except gspread.exceptions.SpreadsheetNotFound:
    print("The 'terminal-horror' spreadsheet was not found.")
    sys.exit(1)
except ConnectionError as error:
    print(f"An error occurred while opening the spreadsheet: {error}")
    sys.exit(1)

def pause_and_continue():
    """
    allows user to continnue the terminal when finished reading
    """
    print("\nPress 'c' to continue...")
    while True:
        user_input = input().strip().lower()
        if user_input == "c":
            break
        else:
            print("Invalid choice. Please enter c to continue")


# Function to introduce the game
def introduction():
    """
    Introduction for game with description of what the game is about
    """
    # Open the 'Game Tracker' worksheet
    user_info_worksheet = SHEET.worksheet('Game Tracker')
    terminal_title = """                   
  _______                  _             _   _    _                           
 |__   __|                (_)           | | | |  | |                          
    | | ___ _ __ _ __ ___  _ _ __   __ _| | | |__| | ___  _ __ _ __ ___  _ __ 
    | |/ _ | '__| '_ ` _ \| | '_ \ / _` | | |  __  |/ _ \| '__| '__/ _ \| '__|
    | |  __| |  | | | | | | | | | | (_| | | | |  | | (_) | |  | | | (_) | |   
    |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|_| |_|  |_|\___/|_|  |_|  \___/|_|                                                                         
    """

    print(terminal_title)
    print("By Callum Morgan")
    sleep(4)
    clear()
    t_print("Welcome to the Terminal Horror")
    t_print("Prepare to step into a world shrouded in darkness, where secrets lie within every creaking floorboard and shadowed corner.")
    sleep(1)
    print("")

    t_print("Before you stands Diablo, a seasoned paranormal investigator with an air of mystery and a haunted past.")
    t_print("He's sought the truth in countless haunted places, but none compare to the dread that lurks within the Terminal Horror Mansion.")
    sleep(1)
    print("")

    t_print("Whispers of the mansion's malevolent reputation have reached your ears.")
    t_print("Teenagers have gone missing, and no one has ventured near the place for decades.")
    t_print("The mansion, a chilling enigma, beckons you to uncover its secrets.")
    sleep(1)

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


# Function to generate a random ghost
def generate_ghost():
    """
    Generates Ghost at random using google sheets data and passing it as an argument
    """
    # Open the 'Ghosts' worksheet
    ghost_worksheet = SHEET.worksheet('Ghosts')
    game_tracker_worksheet = SHEET.worksheet('Game Tracker')

    # Get a list of ghost names
    ghost_names = ghost_worksheet.col_values(1)[1:]
    # Choose a random ghost name
    random_ghost = random.choice(ghost_names)
    # Generate clues for the chosen ghost
    generate_clues(random_ghost)
    # Update the 'Game Tracker' worksheet with the selected ghost
    game_tracker_worksheet.update_acell('B2', random_ghost)


# Function to generate clues for a specific ghost and update Google Sheets
def generate_clues(ghost):
    """
    Generates clues for the ghost and updates Google Sheets with descriptions of items in cells for the generated ghost.
    """
    # Open the 'Rooms' worksheet
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

    # Loop through the ghost_clues dictionary to find the clues for the specified ghost
    if ghost in ghost_clues:
        cell_data = ghost_clues[ghost]
        for data in cell_data:
            cell = room_worksheet.cell(data["row"], data["column"])
            cell.value = data["description"]
            cell_list.append(cell)

        # Update the worksheet to apply the changes
        room_worksheet.update_cells(cell_list)
    else:
        print(f"No clues defined for the ghost: {ghost}")


# Starts the game with the users name and gives introduction of game
def start_game(name):
    """
    Starts the game and provides the player with information and objectives.
    """
    t_print(f"You must be {name}.")
    t_print("I'm Diablo, a paranormal investigator with a lifelong fascination for the unknown.")
    t_print("I've spent years studying the mysteries of the terminal horror mansion, but it's never been more sinister than now.")
    print("")
    t_print("The mansion has been abandoned for centuries, and the legends surrounding it have only grown darker.")
    t_print("What's worse... Since it gained notoriety, we've had a group of teenagers disappear after venturing inside.")
    print("")
    t_print("This is where you come in.")
    t_print("Your mission is to uncover the nature of the ghost")
    t_print("Use the descriptions of items within rooms to uncover the traits of the ghost. Only a few items reveal these traits")
    pause_and_continue()
    sleep(2)
    clear()
    t_print("I've provided you with a notebook, a tool I've used on countless investigations.")
    t_print("In this book, you'll find.")
    print("")
    t_print("Entities Traits. Check this first so you know what to look for.")
    print("")
    t_print("Ability to write and view your own notes")
    print("")
    t_print("Hints if you need help.")
    print("")
    t_print("Remember, when you're sure of the entity you're dealing with, make your guess in the notebook's 'Guess' section.")
    t_print("But you have only two chances, so choose wisely.")
    pause_and_continue()
    clear()
    sleep(2)

    # checks user input and executes statements depnding on input
    while True:
        user_ready = input(f"So {name} are you ready?(Y/N): ")
        if user_ready.upper() == "Y":
            haunted_house = """

                /_-_-| | |-_--|=| | | ||=|_|_|=||"|==|
                /-__--|_|_|_-_-| |_|_|=||______=||_| =|
                /_-__--_-__-___-|_=__=_.`---------'._=_|__
                /-----------------------\\===========/-----/
            ^^^\\^^^^^^^^^^^^^^^^^^^^^^[[|]]|[[|]]=====/
                |.' ..==::'"'::==.. '.[ /~~~~~\\ ]]]]]]]
                | .'=[[[|]]|[[|]]]=`._||==  =  || =\\ ]
                ||== =|/ _____ \\|== = ||=/^|^\\=||^\\ ||
                || == `||-----||' = ==|| | | |=|| |=||
                ||= == ||:^s^:|| = == ||=| | | || |=||
                || = = ||:___:||= == =|| |_|_| ||_|=||
                _||_ = =||o---.|| = ==_||_= == =||==_||_
                \\__/= = ||:   :||= == \\__/[][][][][]\\__/
                [||]= ==||:___:|| = = [||]\\//\\//\\[||]
                }  {---'"'-----'"'- --}  {//\\//\\//}  {
            """
            print(haunted_house)
            t_print("You walk towards to the building...")
            sleep(3)
            clear()
            generate_ghost()
            enter_house()
            break
        elif user_ready.upper() == "N":
            print("No problem. I will give you some time to think this through")
            continue
        elif user_ready.strip() == "":
            # Prevents user from inputting nothing
            print("Invalid choice. Please enter a response.")
            continue
        elif user_ready.isdigit():
            # Prevents user from inputting number
            print("Invalid input. Please enter 'Y' or 'N', not a number.")
            continue
        else:
            # If uer doesn't input any of the above it will execute this code
            print("Invalid input. Please enter 'Y' or 'N'.")
            continue


def enter_house():
    """
    Initiates the game by entering the haunted house.
    """
    room_worksheet = SHEET.worksheet('Rooms')
    hallway_description = room_worksheet.cell(5, 2).value
    # Gets cell value from room worksheet

    t_print("You entered the house...\n")
    t_print("You walk into the hallway\n")
    t_print(hallway_description + "\n")
    sleep(2)
    rooms()


def rooms():
    """
    Displays a list of rooms for the player to investigate and provides options to access the notebook or quit the game.
    """
    clear()

    while True:
        print("Rooms to investigate:\n")
        room_worksheet = SHEET.worksheet('Rooms')
        room_names = room_worksheet.col_values(1)[1:]
        # Gathers room names in column except first row
        for room in room_names:
            print(f"{room} (Type '{room}')\n")
        print("")
        print("Access Notebook (Type 'N')\n")
        print("Quit Game (Type 'B')\n")

        print("Investigate a room, access your notebook or quit the game\n")
        user_room = input(
            "What action would you like to take?: ").strip().title()

        if user_room == "B":
            t_print("Exiting Game...")
            revert_original_sheet()
            clear()
            restart_game()
            break  # Exit the loop and end the program
        elif user_room == "N":
            clear()
            interact_with_notebook()
            continue
        elif user_room in room_names:
            room_index = room_names.index(user_room)
            room_item_descriptions = room_worksheet.row_values(
                2 + 1 * room_index)
            # Displayes the cell values of each row looped through
            investigate_room(user_room, room_item_descriptions)
        elif user_room == "":
            print("Invalid choice. Please enter a response.")
            continue
        else:
            clear()
            print("Invalid room name. Please try again.\n")
            continue


def investigate_room(room_name, room_item_descriptions):
    """
    Allows the player to investigate a room and its items.
    """
    clear()
    t_print(f"You have entered the {room_name}\n")
    # Get the room description from the room_item_descriptions list
    room_description = room_item_descriptions[1]
    # Get a list of items in the room (ignoring the first element, which is the room description)
    items = room_item_descriptions[2:]

    t_print(room_description + "\n")
    sleep(3)
    for i in range(0, len(items), 2):
        item_name = items[i]
    # Display the item name and the command to investigate it
        print(f"{item_name} (Type '{item_name}')\n")

    while True:
        # Prompt the player for their choice (item to investigate, notebook, or back)
        item_found = False 
        user_chosen_item = input("Type which item you would like to investigate or type 'B' to back out or type 'N' to access notebook: ")
        print("")
        for i in range(0, len(items), 2):
            item_name = items[i]
            # Check if the player's choice matches the name of an item
            if user_chosen_item.strip().title() == item_name:
                item_description = items[i + 1]
                t_print(item_description)
                print("")
                item_found = True
                break
        
        if user_chosen_item.strip().title().upper() == "N":
            interact_with_notebook()
            break
        elif user_chosen_item.strip().upper() == "B":
            clear()
            break
        elif user_chosen_item == "":
            print("Invalid choice. Please enter a response.")
            continue
        elif user_chosen_item.isdigit():
            print("Invalid input. Please enter a response not a number.")
            continue
        elif not item_found and user_chosen_item != "":
            print("Invalid choice. Please enter a valid item name or 'N' to access the notebook, or 'B' to go back.")



def end_game(ghost, user_guess):
    """
    Ends the game and informs the player of the result when they run out of guesses.
    """
    clear()
    sleep(2)
    t_print("Oh no...")
    t_print("Looks like you have run out of guesses!")
    t_print(
        f"The ghost you were dealing with was a {ghost}! Your final guess was a {user_guess}")
    restart_game()


def win_game(ghost):
    """
    Displays a victory message when the player correctly identifies the ghost.
    """
    win_text = """
   _____                            _         _       _   _                 
  / ____|                          | |       | |     | | (_)                
 | |     ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___ 
 | |    / _ \\| '_ \\ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \\| '_ \\/ __|
 | |___| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \\__ \'
  \\_____\\___/|_| |_|\\__, |_|  \\__,_|\\__|\\__,_|_|\\__,_|\\__|_|\\___/|_| |_|___/
                     __/ |                                                  
                    |___/                                                   

"""
    user_info_worksheet = SHEET.worksheet('Game Tracker')
    name = user_info_worksheet.col_values(1)[1]
    # Grabs value from Game Tracker worksheet and stores the cell information
    print(win_text)
    sleep(2)

    t_print(
        f"Congradulations {name} you're clearly what you're made up to be! Now you got the hard work done we can now exorcise this {ghost} accordingly")
    t_print("You Truly are the best ghost buster in town! :)")
    restart_game()


def write_notes(notes_worksheet):
    """
    Allows the player to write notes in their notebook.
    """
    clear()
    note = input("Write a note: ")
    notes_worksheet.append_rows([[note]])
    # Sends the data and stores it on the next row of the notebook worksheet
    t_print(f"You wrote: '{note}'")


def view_notes(notes_worksheet):
    """
    Retrieves and displays all notes from the player's notebook.
    """
    clear()
    # Retrieve and display all notes from the Excel sheet
    notes = notes_worksheet.col_values(1)[1:]  # Skip the header
    if notes:
        t_print("Your notes:")
        for index, note in enumerate(notes, start=1):
            t_print(f"{index}. {note}")
    else:
        t_print("You haven't written any notes yet.")


def handle_guess(guess_left):
    """
    Handles the player's guess for the ghost and returns the user's choice.
    """
    clear()
    t_print(f"Take your guess! You have {guess_left} guesses left!")
    print("1. Banshee (Type 'Banshee')")
    print("2. Jinn (Type 'Jinn')")
    print("3. Wraith (Type 'Wraith')")
    print("4. Shade (Type 'Shade')")
    print("5. Demon (Type 'Demon')")
    user_guess = input(
        "Which ghost would you like to go for: ").strip().title()
    t_print(f"You guessed: {user_guess}")
    return user_guess


def interact_with_notebook():
    """
    Allows the player to interact with their notebook, write notes, view notes, check ghost traits, make guesses, or access hints.
    """
    guess_left = 2  # Initialize guess_left here
    clear()
    t_print("You take out your notebook")

    while True:
        notes_worksheet = SHEET.worksheet('Notebook')
        game_tracker_worksheet = SHEET.worksheet('Game Tracker')
        game_tracker_row = game_tracker_worksheet.row_values(2)
        ghost = game_tracker_row[1]

        print("1. Write notes (Type 'Write')")
        print("2. View notes (Type 'View')")
        print("3. View ghost traits (Type 'Traits')")
        print("4. Take a guess of what the entiity could be (Type 'Guess')")
        print("5. To get hints for what to look for (Type 'Hints')")
        print("6. Escape from this action (Type 'B')")
        
        choice = input("What would you like to do?: ").strip().capitalize()
        
        if choice == "Write":
            write_notes(notes_worksheet)
            pause_and_continue()

            clear()
            continue
        elif choice == "View":
            view_notes(notes_worksheet)
            pause_and_continue()
            clear()
            continue
        elif choice == "B":
            clear()
            t_print("You put your notebook away.")
            break
        elif choice == "Hints":
            clear()
            print("Hints from Diablo:\n")
            print(
                "Here are more in-depth descriptions to give you an idea of the traits the ghosts have:\n")
            print("1. Freezing Temperatures:")
            print("   - This isn't your typical cold room or chilly setting; it's a more sinister, bone-chilling cold.")
            print(
                "   - You'll feel an intense cold that cuts to the bone, making you shiver and see your breath.")
            print("   - Objects may frost over, and windows may become icy.")
            print("\n2. Ghost Writing:")
            print(
                "   - This trait involves anything that appears to have been written or inscribed.")
            print(
                "   - Look for mysterious writings or symbols on walls, objects, or even in your own notebook.")
            print("   - These messages might seem to be written by an unseen hand.")
            print("\n3. Ghost Orb:")
            print("   - Ghost orbs are floating white orbs of light that can be seen in reflections, mirrors, or photographs.")
            print(
                "   - These orbs are not physical objects but rather manifestations of ghostly energy.")
            print("   - They often move in an unusual and non-linear pattern.")
            print("\n4. Shadows:")
            print("   - Shadow activity can manifest as dark, shadowy figures or silhouettes moving in the corners of your vision.")
            print("   - Sudden and unexplained movements or disturbances in the shadows may be a sign of this trait.")
            print("\n5. Spirit Box:")
            print("   - This trait involves communication with the other side.")
            print("   - You may hear unexplained voices, whispers, or responses to your questions through a spirit box or radio.")
            print("   - The voices you hear may have an otherworldly quality.")
            print("\n6. EMF Levels:")
            print("   - High levels of electromagnetic interference (EMF) are often associated with ghostly activity.")
            print("   - Electronic devices like TVs or lights may behave erratically, flicker, or malfunction when a ghost is nearby.")
            print("\n7. Fingerprints:")
            print(
                "   - These could be in many forms, fingerprints, handmarks... claw marks?")
            print("")
            pause_and_continue()
            clear()
            continue

        elif choice == "Traits":
            clear()
            ghost_worksheet = SHEET.worksheet('Ghosts')
            ghost_names = ghost_worksheet.col_values(
                1)[1:]  # Skip the header row
            # Get descriptions from column B, skip the header row
            ghost_descriptions = ghost_worksheet.col_values(2)[1:]
            for ghost_name, ghost_description in zip(ghost_names, ghost_descriptions):
                print(ghost_name)
                print(ghost_description)
                print(f"Traits of {ghost_name}:")
                # Adjust for 0-based index and header row
                row_number = ghost_names.index(ghost_name) + 2
                # Get traits from columns C, D, E
                traits = ghost_worksheet.row_values(row_number)[2:5]
                for index, trait in enumerate(traits, start=1):
                    print(f"{index}. {trait}")
            pause_and_continue()
            clear()
            
            print("")
        elif choice == "Guess":
            user_guess = handle_guess(guess_left)

            if user_guess != ghost:
                clear()
                t_print("Sorry, this isn't the ghost we're looking for")
                guess_left -= 1
                t_print(f"You have {guess_left} guesses left")

                if guess_left == 0:
                    end_game(ghost, user_guess)
                    break
            elif user_guess == ghost:
                clear()
                win_game(ghost)
                break
        else:
            clear()
            t_print(
                "Invalid input. Please choose one of the available options (Write, View, B, Hints, Traits, Guess).")


def revert_original_sheet():
    """
    Reverts the original worksheet data back to a backup in case the player ends the game.
    """
    original_worksheet = SHEET.worksheet("Rooms")
    backup_worksheet = SHEET.worksheet("Rooms Copy")
    note_worksheet = SHEET.worksheet("Notebook")
    game_tracker_worksheet = SHEET.worksheet("Game Tracker")

    # Get the data from the backup worksheet
    note_values = note_worksheet.get_all_values()
    note_worksheet.clear()
    if note_values:
        first_row = note_values[0]  # Store the first row
        note_worksheet.insert_rows([first_row])

    game_values = game_tracker_worksheet.get_all_values()
    game_tracker_worksheet.clear()
    if game_values:
        first_row = game_values[0]  # Store the first row
        game_tracker_worksheet.insert_rows([first_row])

    backup_data = backup_worksheet.get_all_values()

    original_worksheet.clear()

    original_worksheet.insert_rows(backup_data)


def restart_game():
    revert_original_sheet()
    while True:
        t_print("Thank you for playing Terminal Horror!")
        play_again = input("Play again? (Y/N): ").strip().upper()

        if play_again == "Y":
            clear()
            introduction()
            break  # Exit the loop to avoid repeating the question
        elif play_again == "N":
            t_print("No Problem. Goodbye!")
            raise GameExitException("User decided to exit the game.")
            # This will raise a custom exception
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")

class GameExitException(Exception):
    pass


def main():
    """
    The main function that initiates and controls the game's flow.
    """
    try:
        introduction()
    except ConnectionRefusedError as e:
        # error handling is introduction couldn't be executed
        print(f"An unexpected error occurred: {e}")
    except GameExitException:
        # Handle the custom exit exception
        print("Exiting the game...")
    except Exception as e:
        # Handle other exceptions
        print(f"An unexpected error occurred: {e}")


main()
