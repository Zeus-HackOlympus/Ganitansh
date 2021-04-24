#! /usr/bin/env python3
import PySimpleGUI as gui
from colorama import *
from matplotlib import pyplot as plt
class emoji:
    point_right = '\U0001F449'
    correct = '\u2705'
    wrong = '\u274C'
    frowning = "☹️  "

class color:
    # Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    BOLD = '\033[1m'
    END = '\033[0m'
    Theory = Fore.MAGENTA + Back.BLACK
    Theory2 = Fore.CYAN
    Ques = Fore.YELLOW + "Q. " + Fore.RED + BOLD + Back.BLACK
    Ans = Fore.WHITE
    Imp = Fore.YELLOW + BOLD  + Back.BLACK
    Menu = Fore.GREEN+ Back.BLACK

class ascii_art:
    main_end_game = """

       ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████       ▄██████▄   ▄█    █▄     ▄████████    ▄████████
      ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███
      ███    █▀    ███    ███ ███   ███   ███   ███    █▀       ███    ███ ███    ███   ███    █▀    ███    ███
     ▄███          ███    ███ ███   ███   ███  ▄███▄▄▄          ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀
    ▀▀███ ████▄  ▀███████████ ███   ███   ███ ▀▀███▀▀▀          ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
      ███    ███   ███    ███ ███   ███   ███   ███    █▄       ███    ███ ███    ███   ███    █▄  ▀███████████
      ███    ███   ███    ███ ███   ███   ███   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███
      ████████▀    ███    █▀   ▀█   ███   █▀    ██████████       ▀██████▀   ▀██████▀    ██████████   ███    ███
                                                                                                     ███    ███
"""
    main_welcome = """

    ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗
    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝
    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
     ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
"""

# Tip : global variables always capital

gui.theme("Dark")
gui.theme_input_text_color("cyan")
gui.theme_border_width("3")

USERNAME = ""

def Starting():
    LAYOUTOFSTARTING = [
        [gui.Text("Hello, Please Introduce yourself to us: ", size=(40, 1), font="SanFrancisco 20")],
        [gui.Text("Enter your name :", size=(20, 1), font="SanFrancisco 16"),
         gui.InputText(font="SanFrancisco-Bold", text_color="cyan", focus=True)],
        [gui.Button("Next"), gui.Exit()]
    ]
    WINDOWOFSTARTING = gui.Window("Ganitansh-GUI", LAYOUTOFSTARTING, enable_close_attempted_event=True, finalize=True)

    while True:
        eventOfWinOfStarting, valuesOfWinOfStarting = WINDOWOFSTARTING.read()
        print(eventOfWinOfStarting, valuesOfWinOfStarting)
        # if valuesOfWinOfStarting[0] == None :
        # error please enter name
        if (eventOfWinOfStarting == gui.WIN_CLOSED or eventOfWinOfStarting == 'Exit' or eventOfWinOfStarting == gui.WINDOW_CLOSE_ATTEMPTED_EVENT) and (gui.popup_yes_no("Do you really want to close ? ") == "Yes") :
            break
        elif (eventOfWinOfStarting == "Next"):
            MainMenu()

def MainMenu():
    LAYOUTOFMENU = [

        [gui.Text("Main Menu", font="SanFrancisco-Bold  20", justification="center")],
        [gui.Button("Basic Level (VEDIC MATHS)", key="Enter")],
        [gui.Button("Moderate Level(6TH -8TH STANDARD)")],
        [gui.Button("Advance Level(9TH TO 12TH STANDARD)")],
        [gui.Button("Everyday Mathematics")],
        [gui.Exit()]

    ]

    WINDOWOFMENU = gui.Window("Ganitansh-GUI", LAYOUTOFMENU, enable_close_attempted_event=True, size=(500, 500),
                              modal=True)

    while True:
        eventOfWinOfMenu, valuesofWinOfMenu = WINDOWOFMENU.read()
        print(eventOfWinOfMenu,valuesofWinOfMenu)
        if (eventOfWinOfMenu == gui.WINDOW_CLOSE_ATTEMPTED_EVENT or eventOfWinOfMenu == "Exit" or eventOfWinOfMenu == gui.WIN_CLOSED) and (gui.popup_yes_no("Do you really want to close ?") == "Yes"):
            break
            WINDOWOFMENU.close()
        elif (eventOfWinOfMenu == "Basic Level (VEDIC MATHS)") :
            break
            WINDOWOFMENU.close()
            basiclevelVedicMaths()
        elif (eventOfWinOfMenu == "Moderate Level(6TH -8TH STANDARD)"):
            break
            WINDOWOFMENU.close()
            ModerateLevel()
        elif (eventOfWinOfMenu == "Advance Level(9TH TO 12TH STANDARD)"):
            break
            WINDOWOFMENU.close()
            AdvancedMenu()
        elif (eventOfWinOfMenu == "Everyday Mathematics"):
            break
            WINDOWOFMENU.close()
            EverydayMath()


def main():
    eventLoopStarting()

if __name__ == '__main__':
    main()




