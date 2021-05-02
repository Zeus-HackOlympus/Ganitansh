#! /usr/bin/env python3
"""
Project: Ganitansh-GUI
Purpose: Provide interactive E-Education to abled and disabled
Programmer: HackOlympus
"""

import PySimpleGUI as gui
from colorama import *
import pyttsx3
import threading
from matplotlib import pyplot as plt
import math

# def DoubleDigitMultiplication():  TODO
# def MultiplicationOfa2DigitNumber(): TODO
# def SquareOfDoubleDigitEndingWith5(): TODO


"""
Image Element
layout = [
            [gui.Image(r'C:\PySimpleGUI\Logos\PySimpleGUI_Logo_320.png')],
         ]
"""
"""
def mod_menu() :
    layout = [
        [gui.Button("Linear EQUATIONs")],
        [gui.Button("Coordinate Geometery")],
        [gui.Button("Visualise EQUATIONs")],
        [gui.Button("Go Back")],
    ]

    window = gui.Window("Ganitansh-GUI",layout)

    event, values = window.read()
    while True  :
        if event in (gui.WIN_CLOSED,gui.WINDOW_CLOSE_ATTEMPTED_EVENT,"Exit"):
            window.close()
            break
        elif (event == "Linear EQUATIONs"):
            LinearEQUATIONs()
        elif (event == "Coordinate Geometery") :
            CoordinateGeometery()
        elif (event == "Visualise EQUATIONs"):
            VisualiseEQUATIONs()
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

# TODO: CHECK IF GLOBAL VARIABLES ARE IN CAPITAL OR NOT

gui.theme("Dark black")

USERNAME = ""

# TODO : COMPLETE ABOUT US

ABOUTUS = """ 
About Us 


We are a group of high school ....

{0} Prabhnoor Singh Sahni  :  prabhnoor28@outlook.com       

{0} Hirnika Oberoi : hirnikaoberoi7@gmail.com

{0} Vishal Juneja : vishal_juneja@outlook.com       

Our Teacher : 

{0} Ms. Sangeeta Panchal 

""".format(emoji.point_right)

def progressBar():
    layout = [[gui.Text('A custom progress meter')],
              [gui.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')],
              [gui.Cancel()],
              [gui.Button("click here and start progress bar",key = "click here")]
              ]
    window = gui.Window('Custom Progress Meter', layout)
    progress_bar = window['progressbar']
    while True :
        event, values = window.read()
        if event == "click here":
            for i in range(1000):
                if event == 'Cancel' or event == gui.WIN_CLOSED:
                    break
                progress_bar.UpdateBar(i + 1)
        elif event in (gui.WIN_CLOSED,gui.WIN_CLOSE_ATTEMPTED_EVENT,"Exit") :
            break
    window.close()

def starting_window():

    Menu = [

        ["Go To", ["Introduction", "Main Menu", ["Basic Level", "Moderate Level", "Advanced Level"]]],
        ["Utilities", ["Calculator"]],
        ["About Us", ["About ..."]]
    ]

    layout = [
        [gui.Menu(Menu)],
        [gui.Text(ascii_art.main_welcome)],
        [gui.Text("", key="error")],
        [gui.Text("Hello, Please Introduce yourself to us: ", size=(40, 0), font=("SanFrancisco",20))],
        [gui.Text("Enter your name :", size=(20, 0), font=("SanFrancisco", 16))],
        [gui.InputText(font="SanFrancisco-Bold", text_color="cyan", focus=True)],
        [gui.Text("",key="ERROR ABOUT NAME",size=(24,1))],
        [gui.Button("Next"), gui.Exit()]
    ]
    window = gui.Window("Ganitansh-GUI", layout, enable_close_attempted_event=True,
                        finalize=True,
                        size=(1000, 500))
    return window



def MainMenu():
    layout = [
        [gui.Text("\t   Main Menu", font="SanFrancisco-Bold  20", justification="centre")],
        [gui.Button("\t\t\tBasic Level (VEDIC MATHS)\t\t\t",key="Basic Level (VEDIC MATHS)",
                    size=(70,2),font=("Helvetica"))],
        [gui.Button("\t\t\tModerate Level(6TH -8TH STANDARD)\t\t\t",key="Moderate Level(6TH -8TH STANDARD)",
                    size=(70,2),font=("Helvetica"))],
        [gui.Button("\t\t\tAdvance Level(9TH TO 12TH STANDARD)\t\t\t",key="Advance Level(9TH TO 12TH STANDARD)",
                    size=(70,2),font=("Helvetica"))],
        [gui.Button("\t\t\tEveryday Mathematics\t\t\t",key="Everyday Mathematics",
                    size=(70,2),font=("Helvetica"))],
        [gui.Exit()]
    ]

    window = gui.Window("Ganitansh-GUI", layout,
                              enable_close_attempted_event=True, size=(500, 500),
                              modal=True,finalize=True)
    # window1,window2 = window,None

    # while True :
    #     window, event, value = gui.read_all_windows()
    #     if event in (gui.WIN_CLOSED,"Exit") :
    #         if window == window1 :
    #             break
    #         elif window == window2 :
    #             window2 = None
    return window




def basiclevelVedicMaths():
    layout = [
        [gui.Text("\t\tBasic Math Menu",font="SanFrancisco-Bold 12",text_color="cyan",justification="center")],
        [gui.Button("Double Digit Multiplication",font="SanFrancisco-Bold 12")],
        [gui.Button("Multiplication of a two-digit number by 11",font="SanFrancisco-Bold 12")],
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




def calculator_window():
    BArgs = {"size": (8, 2), "font": ("Franklin Gothic Book", 10, "bold"), "pad": (0, 0), "border_width": 0}
    menu = [
        ["Modes", ["Simple", "Advanced", "Graphing"]],
        ["AboutUs", ["About..."]],
        ["Help", ["Guide Fo.."]]
    ]

    # 404040
    layout = [
        [gui.Menu(menu)],
        [gui.Text("Ganitansh Calculator", font=("dejavu", "14", "bold"), text_color="lime", justification="center",
                  background_color="grey")],
        [gui.Text("0", font=("digital-7", 30, "bold"), background_color="white", size=(32, 3),
                  justification="right", text_color="Red", key="SCREEN", relief="sunken")],
        [gui.Button("1", **BArgs), gui.Button("2", **BArgs), gui.Button("3", **BArgs),
         gui.Button("\u00F7", **BArgs), gui.Button("Undo", **BArgs),
         gui.Button("Clear", button_color="#bd1616", **BArgs)],
        [gui.Button("4", **BArgs), gui.Button("5", **BArgs), gui.Button("6", **BArgs), gui.Button("x", **BArgs),
         gui.Button("(", **BArgs), gui.Button(")", **BArgs)],
        [gui.Button("7", **BArgs), gui.Button("8", **BArgs), gui.Button("9", **BArgs), gui.Button("-", **BArgs),
         gui.Button(button_text="x" + "\u00B2", **BArgs), gui.Button("\u221A", **BArgs, key="\u221A" + "(")],
        [gui.Button("0", **BArgs), gui.Button(".", **BArgs), gui.Button("%", **BArgs), gui.Button("+", **BArgs),
         gui.Button("Enter", size=(19, 2), font=("Franklin Gothic Book", 10, "bold"), pad=(0, 0),
                    button_color="#0066FF")],
    ]

    SCREEN = ""
    EQUATION = []

    window = gui.Window("Ganitansh-Calculator", layout, background_color="grey",
                        return_keyboard_events=True,finalize=True)  # 23252e
    return  window


def mod_menu():
    layout = [
        [gui.Button("{} Linear Equations".format(emoji.point_right))],
        [gui.Button("{} Coordinate Geometery".format(emoji.point_right))],
        [gui.Button("{} Go Back".format(emoji.point_right))]
    ]

    def menu():
        frame = [
            # [gui.Text("Calculator Help Menu")],
            [gui.Button("Simple Mode Help")],
            [gui.Button("Advanced Mode Help")],
            [gui.Button("Graphing Mode")]
        ]
        layout = [
            gui.Frame("Calculator Help Menu", layout=frame)
        ]

        window = gui.Window("Ganitansh-GUI", layout)
        while True:
            event, values = window.read()
            print(event, values)

    menu()
    window = gui.Window("Ganitansh Moderate Menu", layout)

    while True:
        events, values = window.read()
        if events in ("Exit", gui.WIN_CLOSE_ATTEMPTED_EVENT, gui.WIN_CLOSED):
            break
    window.close()


"""
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
"""


def Starting() :
    key_scheme = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                  "(", ")", "-", "+", "."]
    keyboard = ["1:10", "2:11", "3:12",
                "4:13", "5:14", "6:15",
                "7:16", "8:17", "9:18",
                "0:19", "parenleft:18",
                "parenright:19", "minus:20", "plus:21",
                "period:60", "percent:14", "asciicircum:15"]
    SCREEN = ""
    EQUATION = []

    # window1 = main window
    # window2 and window3 = supplementary window

    window1 = starting_window()
    window2 = None
    window3 = None
    while True :
        window, event, values = gui.read_all_windows()
        print(event,values)
        if event == gui.WIN_CLOSED or event == "Exit" :
            if window == window2 :
                window2 = None
            elif window == window3 :
                window3 = None
            elif window == window1 :
                break
        elif event == "About ..." :
            gui.popup("About Us",ABOUTUS)
        elif event == "Next" and values[1] != "" and not window3  :
            global USERNAME
            USERNAME += values[1]
            print("USERNAME = {}".format(USERNAME))
            window3 = MainMenu()
        elif event == "Next" and values[1] == "" :
            window1['ERROR ABOUT NAME'].update("Please introduce yourself")

        elif event == "Calculator" and not window2 :
            window2 = calculator_window()

        # TODO : ADD MULTI WINDOW FUNCTIONALITY FOR SCIENTIFIC AND GRAPHING CALC
        # elif event == "Advanced":enter your na
        #     AdvancedCalculator()
        # elif event == "Graphing":
        #     GraphingCalc()

        # CALCULATOR EVENTS OF STARTING
        elif (event in keyboard) and (event != "asciicircum:15"):
            if (event in keyboard) and (event == "percent:14"):
                SCREEN += "%"
                EQUATION.append("{}/100".format(EQUATION[len(EQUATION) - 1]))
                window['SCREEN'].update(SCREEN)
                print("equation = ", EQUATION)
                print("event = ", event)
            else:
                if event in keyboard:
                    event = key_scheme[keyboard.index(event)]
                    SCREEN += event
                    EQUATION.append(event)
                    window['SCREEN'].update(SCREEN)
                    print("equation = ", EQUATION)
                    print("event = ", event)
        elif (event in key_scheme):
            SCREEN += event
            EQUATION.append(event)
            window['SCREEN'].update(SCREEN)
            print("equation = ", EQUATION)
            print("event = ", event)

        elif event in ("\u00F7", "slash:61"):
            SCREEN += "\u00F7"
            EQUATION.append("/")
            window['SCREEN'].update(SCREEN)
            print("equation = ", EQUATION)
            print("event = ", event)

            # square
        elif event in ("x" + "\u00B2", "asciicircum:15"):
            SCREEN += "\u00B2"
            EQUATION.append("**2")
            window['SCREEN'].update(SCREEN)
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event in ("x", "KP_Multiply:63", "asterisk:17"):
            SCREEN += "x"
            EQUATION.append("*")
            window['SCREEN'].update(SCREEN)
            print("equation = ", EQUATION)
            print("event = ", event)
            # square root
        elif event == "\u221A" + "(":
            SCREEN += event
            EQUATION.append("math.sqrt(")
            window['SCREEN'].update(SCREEN)
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_End:87":
            SCREEN += "1"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("1")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Delete:91":
            SCREEN += "."
            window['SCREEN'].update(SCREEN)
            EQUATION.append(".")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Left:83":
            SCREEN += "4"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("4")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Home:79":
            SCREEN += "7"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("7")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Up:80":
            SCREEN += "8"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("8")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Prior:81":
            SCREEN += "9"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("9")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Begin:84":
            SCREEN += "5"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("5")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Right:85":
            SCREEN += "6"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("6")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Next:89":
            SCREEN += "3"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("3")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Down:88":
            SCREEN += "2"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("2")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "Clear":
            window['SCREEN'].update("0")
            SCREEN = ""
            EQUATION = []
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Add:86":
            print(event)
            SCREEN += "+"
            EQUATION.append("+")
            window['SCREEN'].update(SCREEN)
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Add:86":
            SCREEN += "+"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("+")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Subtract:82":
            SCREEN += "-"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("-")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Multiply:63":
            SCREEN += "*"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("*")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Divide:106":
            SCREEN += "\u00F7"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("/")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event in ("Undo", "BackSpace:22"):
            try:
                SCREEN = SCREEN[0:len(SCREEN) - 1]
                EQUATION.pop()
                print(EQUATION)
                window['SCREEN'].update(SCREEN)
                print("equation = ", EQUATION)
                print("event = ", event)
            except:
                pass
        elif event in ("Enter", "Return:36", "KP_Enter:104", "equal:21"):
            try:
                result = eval("".join(EQUATION))
                print("result = ", result)
                EQUATION = [str(result)]
                SCREEN = str(float(result))
                window['SCREEN'].update(SCREEN.format(".10f"))
                print("equation = ", EQUATION)
                print("event = ", event)
            except ZeroDivisionError:
                window['SCREEN'].update("Error")
            except SyntaxError:
                pass

    window.close

def main():
    init()
    Starting()

if __name__ == '__main__':
  main()




