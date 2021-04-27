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
import math

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

# Tip : global variables always capital

gui.theme("Dark black")
# gui.theme_input_text_color("cyan")
# gui.theme_border_width("3")
# gui.theme_text_color("cyan")

USERNAME = ""

def progressBar():
    layout = [[gui.Text('A custom progress meter')],
              [gui.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')],
              [gui.Cancel()]]
    window = gui.Window('Custom Progress Meter', layout)
    progress_bar = window['progressbar']
    for i in range(1000):
        event, values = window.read(timeout=10)
        if event == 'Cancel' or event == gui.WIN_CLOSED:
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

        [gui.Text("\t   Main Menu", font="SanFrancisco-Bold  20", justification="centre")],
        [gui.Button("\t\t\tBasic Level (VEDIC MATHS)\t\t\t",key="Basic Level (VEDIC MATHS)",size=(70,2),font=("Helvetica"))],
        [gui.Button("\t\t\tModerate Level(6TH -8TH STANDARD)\t\t\t",key="Moderate Level(6TH -8TH STANDARD",size=(70,2),font=("Helvetica"))],
        [gui.Button("\t\t\tAdvance Level(9TH TO 12TH STANDARD)\t\t\t",key="Advance Level(9TH TO 12TH STANDARD)",size=(70,2),font=("Helvetica"))],
        [gui.Button("\t\t\tEveryday Mathematics\t\t\t",key="Everyday Mathematics",size=(70,2),font=("Helvetica"))],
        [gui.Exit()]

    ]

    WINDOWOFMENU = gui.Window("Ganitansh-GUI", LAYOUTOFMENU,
                              enable_close_attempted_event=True, size=(500, 500),
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


def calculator():
    def check(a: list):
        l = a.copy()
        symbols = "! % * ( ) - + / . **(1/2)".split()
        for i in range(len(a)):
            try:
                if a[i] in symbols and a[i + 1] in symbols:
                    pass
                elif (a[i] in symbols) and (type(eval(a[i + 1]))) in (int, float):
                    if a[i] == ")":
                        l.insert(i + 1, "*")
                elif type(eval(a[i])) in (int, float) and (a[i + 1] in symbols):
                    if a[i + 1] == "(":
                        l.insert(i + 1, "*")
            except IndexError:
                break
        return l

    def sqrt(a: list):
        test = a.copy()
        symbols = "! % * ( ) - + / .".split()
        for i in range(len(a)):
            if a[i] == "**(1/2)" and a[i + 1] not in symbols:
                if type(eval(a[i + 1])) in (int, float):
                    test.insert(i, a[i + 1])
                    test.pop(i + 2)
            elif a[i] == "**(1/2)":
                if a[i + 1] == "(":
                    while a[i + 1] != ")":
                        test.insert(i, a[i + 1])
                        test.pop(i + 2)
                        i += 1
                if a[i + 1] == ")":
                    test.insert(i, a[i + 1])
                    test.pop(i + 2)
        return test

    BArgs = {"size":(8,2),"font":("Franklin Gothic Book",10,"bold"),"pad":(0,0),"border_width":0}
    menu = [
        ["Modes",["Simple","Advanced","Graphing"]],
        ["AboutUs"]
    ]

    key_scheme = ["1","2","3","4","5","6","7","8","9","0",
                  "(",")","-","+","."]
    keyboard = ["1:10","2:11","3:12",
                "4:13","5:14","6:15",
                "7:16","8:17","9:18",
                "0:19","parenleft:18",
                "parenright:19","minus:20","plus:21",
                "period:60","percent:14","asciicircum:15"]

    layout = [
        [gui.Menu(menu)],
        [gui.Text("Ganitansh Calculator",font=("dejavu","14","bold"),text_color="lime",justification="center",background_color="grey")],
        [gui.Text("0",font=("digital-7",30),background_color="#404040",size=(32,3),justification="right",text_color="Red",key="SCREEN",relief="sunken")],
        [gui.Button("1",**BArgs),gui.Button("2",**BArgs),gui.Button("3",**BArgs),gui.Button("\u00F7",**BArgs),gui.Button("Undo",**BArgs),gui.Button("Clear",button_color="#bd1616",**BArgs)],
        [gui.Button("4",**BArgs),gui.Button("5",**BArgs),gui.Button("6",**BArgs),gui.Button("x",**BArgs),gui.Button("(",**BArgs),gui.Button(")",**BArgs)],
        [gui.Button("7",**BArgs),gui.Button("8",**BArgs),gui.Button("9",**BArgs),gui.Button("-",**BArgs),gui.Button(button_text="x"+ "\u00B2",**BArgs),gui.Button("\u221A",**BArgs)],
        [gui.Button("0",**BArgs),gui.Button(".",**BArgs),gui.Button("%",**BArgs),gui.Button("+",**BArgs),gui.Button("Enter",size=(19,2),font=("Franklin Gothic Book",10,"bold"),pad=(0,0),button_color="#0066FF")],
    ]

    SCREEN = ""
    EQUATION = []

    window = gui.Window("Ganitansh-Calculator",layout,background_color="grey",return_keyboard_events=True) #23252e

    while True:
        event, values = window.read()
        print(event,values)
        if event in (gui.WIN_CLOSED,gui.WINDOW_CLOSE_ATTEMPTED_EVENT,"Exit"):
            print("event = ",event)
            break
        elif event == "Advanced" :
            AdvancedCalculator()
        elif event == "Graphing" :
            GraphingCalc()
        elif (event in keyboard) and (event != "asciicircum:15"):
            if (event in keyboard) and (event == "percent:14"):
                SCREEN += "%"
                EQUATION.append("{}/100".format(EQUATION[len(EQUATION) - 1]))
                window['SCREEN'].update(SCREEN)
                print("equation = ",EQUATION)
                print("event = ", event)
            else:
                if event in keyboard :
                    event = key_scheme[keyboard.index(event)]
                    SCREEN += event
                    EQUATION.append(event)
                    window['SCREEN'].update(SCREEN)
                    print("equation = ", EQUATION)
                    print("event = ", event)
        elif (event in key_scheme) :
            SCREEN += event
            EQUATION.append(event)
            window['SCREEN'].update(SCREEN)
            print("equation = ",EQUATION)
            print("event = ",event)

        elif event in ("\u00F7", "slash:61"):
            SCREEN += "\u00F7"
            EQUATION.append("/")
            window['SCREEN'].update(SCREEN)
            print("equation = ", EQUATION)
            print("event = ", event)


        # square
        elif event in ("X"+"\u00B2","asciicircum:15") :
            SCREEN += "\u00B2"
            EQUATION.append("**2")
            window['SCREEN'].update(SCREEN)
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event in ("x","KP_Multiply:63","asterisk:17") :
            SCREEN += "x"
            EQUATION.append("*")
            window['SCREEN'].update(SCREEN)
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "\u221A" :
            SCREEN += event
            EQUATION.append("**(1/2)")
            window['SCREEN'].update(SCREEN)
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_End:87" :
            SCREEN += "1"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("1")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Delete:91" :
            SCREEN += "."
            window['SCREEN'].update(SCREEN)
            EQUATION.append(".")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Left:83" :
            SCREEN += "4"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("4")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Home:79" :
            SCREEN += "7"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("7")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Up:80" :
            SCREEN += "8"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("8")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Prior:81" :
            SCREEN += "9"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("9")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Begin:84" :
            SCREEN += "5"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("5")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Right:85" :
            SCREEN += "6"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("6")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Next:89" :
            SCREEN += "3"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("3")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Down:88" :
            SCREEN += "2"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("2")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "Clear" :
            window['SCREEN'].update("0")
            SCREEN = ""
            EQUATION = []
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Add:86" :
            print(event)
            SCREEN += "+"
            EQUATION.append("+")
            window['SCREEN'].update(SCREEN)
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Add:86" :
            SCREEN += "+"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("+")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Subtract:82" :
            SCREEN += "-"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("-")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Multiply:63" :
            SCREEN += "*"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("*")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event == "KP_Divide:106" :
            SCREEN += "\u00F7"
            window['SCREEN'].update(SCREEN)
            EQUATION.append("/")
            print("equation = ", EQUATION)
            print("event = ", event)
        elif event in ("Undo","BackSpace:22") :
            try:
                SCREEN = SCREEN[0:len(SCREEN)-1]
                EQUATION.pop()
                print(EQUATION)
                window['SCREEN'].update(SCREEN)
                print("equation = ",EQUATION)
                print("event = ", event)
            except:
                pass
        elif event in ("Enter","Return:36","KP_Enter:104","equal:21") :
            try :
                EQUATION = check(EQUATION)
                print("after check = ", EQUATION)
                EQUATION = sqrt(EQUATION)
                print("after sqrt = ",EQUATION)
                result = eval("".join(EQUATION))
                print("result = ",result)
                EQUATION = [str(result)]
                SCREEN = str(float(result))
                window['SCREEN'].update(SCREEN.format(".10f"))
                print("equation = ",EQUATION)
                print("event = ", event)
            except ZeroDivisionError :
                window['SCREEN'].update("Error")
            except SyntaxError :
                pass

    window.close()
# def DoubleDigitMultiplication():


# def MultiplicationOfa2DigitNumber():

# def SquareOfDoubleDigitEndingWith5():

def mod_menu():
    print(Fore.GREEN + BOLD + '''
1 {0} Linear equations
2 {0} Coordinate Geometry (section formula)
3 {0} Visualise equations
4 {0} Go Back'''.format(emoji.point_right) + color.END)






def GraphingCalc():
    layout = [
        [gui.Text("Plot equations",justification="center",text_color="Red")]
    ]
    window = gui.Window("Ganitansh-GUI",layout)
    event, values = window.read()

def main():
    calculator()
    init()
    #Starting()

if __name__ == '__main__':
    main()




