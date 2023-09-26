import gspread
from google.oauth2.service_account import Credentials
import time
import sys

def slow_type(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('terminal-horror')

def introduction():
    """
    Introduction for game with description of what the game is about
    """
    print("Welcome to the Terminal Horror")
    haunted_house = """
                                    .     .
                                    !!!!!!!
                            .       [[[|]]]    .
                            !!!!!!!!|--_--|!!!!!
                            [[[[[[[[\_(X)_/]]]]]
                    .-.     /-_--__-/_--_-\-_--\\
                    |=|    /-_---__/__-__-_\__-_\\
                . . |=| ._/-__-__\===========/-__\_
                !!!!!!!!!\========[ /]]|[[\ ]=====/
                /-_--_-_-_[[[[[[[[[||==  == ||]]]]]]
                /-_--_--_--_|=  === ||=/^|^\ ||== =|
                /-_-/^|^\-_--| /^|^\=|| | | | ||^\= |
            /_-_-| | |-_--|=| | | ||=|_|_|=||"|==|
            /-__--|_|_|_-_-| |_|_|=||______=||_| =|
            /_-__--_-__-___-|_=__=_.`---------'._=_|__
            /-----------------------\===========/-----/
        ^^^\^^^^^^^^^^^^^^^^^^^^^^[[|]]|[[|]]=====/
            |.' ..==::'"'::==.. '.[ /~~~~~\ ]]]]]]]
            | .'=[[[|]]|[[|]]]=`._||==  =  || =\ ]
            ||== =|/ _____ \|== = ||=/^|^\=||^\ ||
            || == `||-----||' = ==|| | | |=|| |=||
            ||= == ||:^s^:|| = == ||=| | | || |=||
            || = = ||:___:||= == =|| |_|_| ||_|=||
            _||_ = =||o---.|| = ==_||_= == =||==_||_
            \__/= = ||:   :||= == \__/[][][][][]\__/
            [||]= ==||:___:|| = = [||]\\//\\//\\[||]
            }  {---'"'-----'"'- --}  {//\\//\\//}  {
            __[==]__________________[==]\\//\\//\\[==]_
        |`|~~~~|================|~~~~|~~~~~~~~|~~~~||
        jgs|^| ^  |================|^   | ^ ^^ ^ |  ^ ||
        \|//\\/^|/==============\|/^\\\^/^.\^///\\//|///
        \\///\\\//===============\\//\\///\\\\////\\\/////
        """
    slow_type("In this text-based adventure game. You will be tasked with the responsibility of finding the ghost\n")
    slow_type("The question is - which ghost could it be? It's your job to uncover the nature of the ghost that is lurking within the shadows\n")
    slow_type("BE AWARE... The deeper you tread into the abyss of the mystery the ghost may get angrier tread carefully\n")
    slow_type("Do you have what it takes? Or will you become another ghostly resident of the Terminal Horror Mansion...")


introduction()