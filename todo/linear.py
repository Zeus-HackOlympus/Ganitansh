#! /usr/bin/env python3 

def linear():
    print(Fore.RED + 'These questions will test your basic knowledge of Linear Equations')
    print(Fore.RED + 'A linear equation of the form ax + by + c will be given')
    eng.say('These questions will test your basic knowledge of Linear Equations. A linear equation of the form ax + by + c will be given')
    eng.runAndWait()
    print(Style.DIM + 'You have to find the value of x only')
    eng.say('You have to find the value of x only')
    eng.runAndWait()
    time.sleep(2)
    scr2 = 0
    while True:
        for i in range(4):
            num1 = floor(random.uniform(-10, 10))
            num2 = floor(random.uniform(-10, 10))
            con = floor(random.uniform(-10, 10))
            var = floor(random.uniform(-10, 10))
            sym.init_printing()
            x,y = sym.symbols('x,y')
            a = sym.Eq(num1*x + num2*y + con,0)
            b = sym.Eq((num1+var)*x + num2*var*y + (con/var),0)
            d = {}
            d = sym.solve([a,b],(x,y))
            print( Style.DIM + 'equation 1 is', num1,x, '+', num2,y, '+', con, '=', '0')
            speak("Equation 1 is {} x plus {} y plus {} equal to zero".format(num1,num2,con)) 
            print( Back.BLACK + 'equation 2 is', (num1+var),x, '+', (num2*var)+y, '+', con/var, '=', '0')
            print( Fore.CYAN + 'Enter the value of x')
            #display(Math(r'nudef cg():
    print( Back.BLACK + 'These questions will test your basic knowledge of Coordinate Geometry more specifically the section formula')
    print( Back.BLACK + 'The coordinates of the two end points and the ratio with which the line is internally divided will be given')
    print( Back.BLACK + 'You have to find the coordinates of the point which divides the line internally in the given ratio')
    scr3 = 0
    while True:
        for i2 in range(4):
            x1 = floor(random.uniform(-10, 10))
            x2 = floor(random.uniform(-10, 10))
            y1 = floor(random.uniform(-10, 10))
            y2 = floor(random.uniform(-10, 10))
            m = floor(random.uniform(-10, 10))
            n = floor(random.uniform(-10, 10))
            lmb = lambda x1,x2,m,n : (x1*n + x2*m)/m+n
            lmb1 = lambda y1,y2,m,n : (y1*n + y2*m)/m+n
            print(Fore.CYAN + 'coordinates of point1 are', '(',x1,',',y1,')')
            print( Fore.CYAN + 'coordinates of point2 are', '(',x2,',',y2,')')
            print( Back.BLACK +'The line is internally divided in a ratio of m:n where m = {} and n = {}'.format(m,n))
            x3 = int(input('Enter the x coordinate of point '))
            y3 = int(input('Enter the y coordinate of point '))
            kaw = floor(lmb(x1,x2,m,n))
            koo = floor(lmb1(y1,y2,m,n))
            t= Timer(120, time_up) #x is amount of allowed time in seconds then execute the provided function
            t.start() #start the timer
            if x3 == kaw and y3 == koo:
                t.cancel()
                scr3 += 1
                print( Fore.GREEN + 'Good Job! Your answer is correct')
                eng.say('Good Job! Your answer is correct')
                eng.runAndWait()
            else :
                t.cancel()
                print( Style.DIM + 'Your answer is incorrect')
                eng.say('Your answer is incorrect')
                eng.runAndWait()
                print( Fore.YELLOW + 'The correct answer is, x coordinate = {} and y coordinate = {}'.format(kaw, koo))
                eng.say('The correct answer is, x coordinate = {} and y coordinate = {}'.format(kaw, koo))
                eng.runAndWait()
            print()
            time.sleep(5)
        break
    print('You got {} questions right out of 4'.format(scr3))
    perc3 = int((scr3)/4)*100
    if perc3 >= 75:
        print("Which means you scored" + Fore.CYAN + {} + "percentage".format(perc3))
        print(Fore.GREEN + "WOW !! Nice Score")
    else:
        print("You have scored {} percentage".format(perc3))
        print("We know that you can score better."+ Fore.RED +"You should try again")
#m1 x + num2 y + con = 0'))

#           num1,x, '+', num2,y, '+', con, '=', '0')
            speak("equation 2 is {} x plus {} {} y plus {} equal to zero".format(num1+var,num2*var,con/var))
            inp = int(input())
            k = floor(d[x])
            #t= Timer(120, time_up) #x is amount of allowed time in seconds then execute the provided function
            #t.start() #start the timer
            if inp == k:
                #t.cancel()
                scr2 += 1
                eng.say('Enter the value of x and wait for 2 minutes')
                eng.runAndWait()
                print( Fore.GREEN +'Good Job! Your answer is correct')
            elif inp == "":
                print(Fore.MAGENTA+"The correct answer is {}".format(k))
                eng.say("The correct answer is {}".format(k))
                eng.runAndWait()
            else :
                #t.cancel()
                print( Fore.RED + 'Your answer is incorrect')
                eng.say('Your answer is incorrect')
                eng.runAndWait()
                print( Back.BLACK + 'The correct answer is', k)
                eng.say('The correct answer is' + str(floor(d[x])))
                eng.runAndWait()
                eng.say(floor(d[x]))
                eng.runAndWait()
            print()
            time.sleep(2)
        break
    print('You got {} questions right out of 4'.format(scr2))
    perc2 = int((scr2)/4)*100
    if perc2 >= 75:
        print("Which means you scored" + Fore.CYAN + {} + "percentage".format(perc2))
        print(Fore.GREEN + "WOW !! Nice Score")
    else:
        print("You have scored {} percentage".format(perc2))
        print("We know that you can score better."+ Fore.RED +"You should try again")

        
linear()
