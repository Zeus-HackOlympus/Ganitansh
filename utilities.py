from math import *
from sympy import *
import pyintputplus as p
import time

def integral():
    l=[]
    while True:
        print("""Enter the equation.""")
        eq = p.inputStr()
        if eq.lower().replace(' ','').find("integral") == -1:
            print("Did you mean to find the integral of the question?")
            print("If yes then please input again with the word: \"integral\".")
            print()
            time.sleep(0.4)
            print("If not then please exit this function.")
        else:
            eq1 = eq.lower().replace('integral','')
            for i in eq1:
                if ord(i)>=97 and ord(i)<=122:
                    a = eq1.count(i)
                    l.append(a)
            x = Symbol(max(l))
            integrals = Integral(eq1,x)
            print(f"Your integral is : {integrals.doit()}")
            print()
            time.sleep(1)
            print("Do you wish to solve another integral? [Y/N]")
            eq11 = p.inputStr()
            if eq11.lower().replace(" ","") == "y":
                print()
                pass
            else:
                print()
                break


def calc():
    pass

def conv():
    while True:
        print("""What do you want to convert?""")
        print("""1 --> Mass [mg->kg, kg->mg]
        2 --> Length [cm->m, mm->m, m->cm, cm-mm]
        3 --> Time [seconds->hours, hours->seconds, minutes->seconds, hours->minutes]
        4 --> Volume [Cubic Metres -> Litres, Litres -> Cubic Metres, Litres -> Milli Litres, Milli Litres -> Cubic Centimetres, Cubic Centimetres -> Cubic Metres]
        5 --> Exit.
        """)
        c1 = p.inputNum()
        if c1 == 1:
            while True:
                print("""Choose one of the following options""")
                print("""1 --> Milligrams -> Kilograms
                2 --> Kilograms -> Milligrams
                3 --> Exit
                """)
                c11 = p.inputNum()
                if c11 == 1:
                    pass
                if c11 == 2:
                    pass
                if c11 == 3:
                    break
        if c1 == 2:
            pass
        if c1 == 3:
            pass
        if c1 == 4:
            pass
        if c1 == 5:
            break



def main():
    while True:
        print("Please select any one of the following options: ")
        print("""1 --> Calculator     (Addition, Subtraction, Division, Multiplication)

        2 --> Conversion of units     (Mass, Length, Time, Volume)

        3 --> Integral Solver         (any function [NOTE:Please follow the provided instructions while inputting your equation])

        4 --> Exit utilities.
        """)
        c = p.inputNum()
        if c==1: calc()
        if c == 2: conv()
        if c == 3: integral()
        if c == 4: break
        print()
        time.sleep(0.5)


if __name__ == '__main__':
    main()
