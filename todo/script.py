#! /usr/bin/env python3
"""
Project: Ganitansh-GUI
Purpose: Provide interactive E-Education to abled and disabled
Programmer: HackOlympus
"""

import PySimpleGUI as gui
from colorama import *
import pyttsx3
from matplotlib import pyplot as plt

"""
Image Element
layout = [
            [sg.Image(r'C:\PySimpleGUI\Logos\PySimpleGUI_Logo_320.png')],
         ]
"""
"""
def mod_menu() :
    layout = [
        [gui.Button("Linear Equations")],
        [gui.Button("Coordinate Geometery")],
        [gui.Button("Visualise equations")],
        [gui.Button("Go Back")],
    ]

    window = gui.Window("Ganitansh-GUI",layout)

    event, values = window.read()
    while True  :
        if event in (gui.WIN_CLOSED,gui.WINDOW_CLOSE_ATTEMPTED_EVENT,"Exit"):
            window.close()
            break
        elif (event == "Linear Equations"):
            LinearEquations()
        elif (event == "Coordinate Geometery") :
            CoordinateGeometery()
        elif (event == "Visualise equations"):
            VisualiseEquations()
        elif (event == "Go Back"):
            ## goback function
"""

def speak(text):
    eng = pyttsx3.Engine()
    eng.say(text)
    eng.runAndWait()

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

gui.theme("Dark black")
# gui.theme_input_text_color("cyan")
# gui.theme_border_width("3")
# gui.theme_text_color("cyan")

USERNAME = ""

def progressBar():
    layout = [[sg.Text('A custom progress meter')],
              [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')],
              [sg.Cancel()]]
    window = sg.Window('Custom Progress Meter', layout)
    progress_bar = window['progressbar']
    for i in range(1000):
        event, values = window.read(timeout=10)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        progress_bar.UpdateBar(i + 1)
    window.close()

def Starting():
    LAYOUTOFSTARTING = [
        [gui.Text(ascii_art.main_welcome)],
        [gui.Text("",key="error")],
        [gui.Text("Hello, Please Introduce yourself to us: ", size=(40, 1), font="SanFrancisco 20")],
        [gui.Text("Enter your name :", size=(20, 1), font="SanFrancisco 16")],
        [gui.InputText(font="SanFrancisco-Bold", text_color="cyan", focus=True)],
        [gui.Button("Next"), gui.Exit()]
    ]
    WINDOWOFSTARTING = gui.Window("Ganitansh-GUI", LAYOUTOFSTARTING, enable_close_attempted_event=True, finalize=True,size=(1000,500))

    while True:
        eventOfWinOfStarting, valuesOfWinOfStarting = WINDOWOFSTARTING.read()
        print(eventOfWinOfStarting, valuesOfWinOfStarting)
        # if valuesOfWinOfStarting[0] == None :
        # error please enter name
        global USERNAME
        if valuesOfWinOfStarting[0] != "":
            USERNAME += valuesOfWinOfStarting[0]
        else:
            WINDOWOFSTARTING['error'].update("Please enter name")
        print("Username is {}".format(USERNAME))
        if  eventOfWinOfStarting in (gui.WIN_CLOSED, 'Exit'):
            break
        elif (eventOfWinOfStarting == "Next") and (USERNAME != None):
            WINDOWOFSTARTING.close()
            MainMenu()
        WINDOWOFSTARTING.close()


def MainMenu():
    LAYOUTOFMENU = [

        [gui.Text("Main Menu", font="SanFrancisco-Bold  20", justification="centre")],
        [gui.Button("\t\t\tBasic Level (VEDIC MATHS)\t\t\t",key="Basic Level (VEDIC MATHS)")],
        [gui.Button("\t\t\tModerate Level(6TH -8TH STANDARD)\t\t\t",key="Moderate Level(6TH -8TH STANDARD")],
        [gui.Button("\t\t\tAdvance Level(9TH TO 12TH STANDARD)\t\t\t",key="Advance Level(9TH TO 12TH STANDARD)")],
        [gui.Button("\t\t\tEveryday Mathematics\t\t\t",key="Everyday Mathematics")],
        [gui.Exit()]

    ]

    WINDOWOFMENU = gui.Window("Ganitansh-GUI", LAYOUTOFMENU, enable_close_attempted_event=True, size=(500, 500),
                              modal=True)

    while True:
        eventOfWinOfMenu, valuesofWinOfMenu = WINDOWOFMENU.read()
        print(eventOfWinOfMenu,valuesofWinOfMenu)
        if (eventOfWinOfMenu == gui.WINDOW_CLOSE_ATTEMPTED_EVENT or eventOfWinOfMenu == "Exit" or eventOfWinOfMenu == gui.WIN_CLOSED) :
            break

        elif (eventOfWinOfMenu == "Basic Level (VEDIC MATHS)") :
            WINDOWOFMENU.close()
            basiclevelVedicMaths()
            break
        elif (eventOfWinOfMenu == "Moderate Level(6TH -8TH STANDARD)"):
            WINDOWOFMENU.close()
            ModerateLevel()
            break
        elif (eventOfWinOfMenu == "Advance Level(9TH TO 12TH STANDARD)"):
            WINDOWOFMENU.close()
            AdvancedMenu()
            break
        elif (eventOfWinOfMenu == "Everyday Mathematics"):
            WINDOWOFMENU.close()
            EverydayMath()
            break
    WINDOWOFMENU.close()
def basiclevelVedicMaths():
    layout = [
        [gui.Text("These questions will help you build your speed in calculation",font="SanFrancisco-Bold 12",text_color="cyan")],
        [gui.Button("Double Digit Multiplication",font="SanFrancisco-Bold 12")],
        [gui.Button("Multiplication of a two-digit number by 11...",font="SanFrancisco-Bold 12")],
        [gui.Button("Finding square of double digit numbers ending with 5",font="SanFrancisco-Bold 12")],
        [gui.Button("Go Back",font="SanFrancisco-Bold 12")]

    ]

    window = gui.Window("Ganitansh-GUI",layout)
    while True:
        event, values = window.read()
        if event in (gui.WIN_CLOSED,gui.WINDOW_CLOSE_ATTEMPTED_EVENT,"Exit"):
            window.close()
            break
        elif (event == "Double Digit Multiplication") :
            DoubleDigitMultiplication()
        elif (event == "Multiplication of a two-digit number by 11..."):
            MultiplicationOfa2DigitNumber()
        elif (event == "Finding square of double digit numbers ending with 5"):
            SquareOfDoubleDigitEndingWith5()
        elif (event == "Go Back"):
            MainMenu()


def calculator():

    BArgs = {"size":(8,2),"font":("Franklin Gothic Book",10,"bold"),"pad":(0,0),"border_width":0}
    menu = [
        ["Modes",["Simple","Advanced","Graphing"]],
        ["AboutUs"]
    ]
    layout = [
        [gui.Menu(menu)],
        [gui.Text("Ganitansh Calculator",font=("dejavu","14","bold"),text_color="#0000FF",justification="center",background_color="grey")],
        [gui.Text("0",font=("Digit-7",20),background_color="#404040",size=(34,2),justification="right",text_color="Red",key="screen",relief="sunken")],
        [gui.Button("1",**BArgs),gui.Button("2",**BArgs),gui.Button("3",**BArgs),gui.Button("\u00F7",**BArgs),gui.Button("Undo",**BArgs),gui.Button("Clear",button_color="#bd1616",**BArgs)],
        [gui.Button("4",**BArgs),gui.Button("5",**BArgs),gui.Button("6",**BArgs),gui.Button("x",**BArgs),gui.Button("(",**BArgs),gui.Button(")",**BArgs)],
        [gui.Button("7",**BArgs),gui.Button("8",**BArgs),gui.Button("9",**BArgs),gui.Button("-",**BArgs),gui.Button(button_text="x"+ "\u00B2",key="square",**BArgs),gui.Button("\u221A",**BArgs)],
        [gui.Button("0",**BArgs),gui.Button(".",**BArgs),gui.Button("%",**BArgs),gui.Button("+",**BArgs),gui.Button("Enter",size=(19,2),font=("Franklin Gothic Book",10,"bold"),pad=(0,0))],
    ]

    window = gui.Window("Ganitansh-Calculator",layout,background_color="grey",return_keyboard_events=True) #23252e
    while True:
        event, values = window.read()
        print(event,values)
        if event in (gui.WIN_CLOSED,gui.WINDOW_CLOSE_ATTEMPTED_EVENT,"Exit"):
            break


    window.close()
# def DoubleDigitMultiplication():


# def MultiplicationOfa2DigitNumber():

# def SquareOfDoubleDigitEndingWith5():

def mod_menu():
    print(Fore.GREEN + BOLD + '''
1 {0} Linear Equations
2 {0} Coordinate Geometry (section formula)
3 {0} Visualise Equations
4 {0} Go Back'''.format(emoji.point_right) + color.END)






def GraphingCalc():
    layout = [
        [gui.Text("Plot Equations",justification="center",text_color="Red")]
    ]
    window = gui.Window("Ganitansh-GUI",layout)
    event, values = window.read()

def main():
    calculator()
    init()
    # Starting()

if __name__ == '__main__':
    main()




