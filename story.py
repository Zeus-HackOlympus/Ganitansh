import pyintputplus as p

# direcion system
north = ['gonorth','N','n','north']
south = ['gosouth','S','s','south']
east = ['goeast','E','e','east']
west = ['gowest','W','w','west']

# global variables for health bar
maxHealth = 100    # Max Health
healthDashes = 20  # Max Displayed dashes

def healthbar(health):
    dashConvert = int(maxHealth/healthDashes)
    currentDashes = int(health/dashConvert)
    remainingHealth = healthDashes - currentDashes

    healthDisplay = '█' * currentDashes
    remainingDisplay = ' ' * remainingHealth
    percent = str(int((health/maxHealth)*100)) + "%"

    print("|" + healthDisplay + remainingDisplay + "|")
    print("         " + percent)

def background():           #Hirnika
    print('''
In the reign of the mughal emperor Jalalludin Mohammad Akhbar kwown as "Akhbar", the Rajput kings of Rajasthan were not surrendering their power to the Mughals.
After many invasions and beneficial proposals by Akhbar, many Rajput kings surrendered to him. He also sent many offers to Rana Pratap but he denied and was adamant.
On 18th June of 1576, a battle took place in Haldighati between Maharana Pratap of Mewar and Akhbar's led by Maan Singh of Amber.
It was a fierce battle. Unfortunately,Rana Pratap lost the battle though he managed to escape.
To hide he has to reach Koriyalli(a safe place towards south western Aravalli Hills )  but his way goes through jungles.
Now, help Rana Pratap to go through the jungle to reach Koriyalli hilly town from Haldighati (south of Mewar) safely.
Keep in mind some Mughal soldiers may follow you.
''')


def possibility():
    print("""
This is a text based game that will require the use of both imagination and Mathematics.
In order to move through the game you can only enter action commands that should include 'a verb' and 'a noun'.
Such as: Go east, go west, go south, go north, take <object>, attack <object>, open <object>, etc
""")
    print("Your Current Health is\n"+healthbar(100))
    print("This will decrease by 20. If you give wrong answer.")


def error():
    print("{} is not defined. {}".format(user_input, possibility()))




def main():
    oof = 0
    while oof != 1:
        inventory = []
        print("""The day dawned crisp and clear, in the Jungle you find yourself in the canopy of a dense forest. """)
        while True:
            print("""
            Towards your north you see a path covered with leaves, towards your west you see a wooden hut, towards your south you see a similar path as the path towards north and towards east there is a cliff.
            What do you do?""")
            user_input = p.inputStr()
            if user_input.replace(' ', '').lower() in east:
                print("You went over the cliff, you're now dead.")
                healthbar(0)
                print("""If you want to start again enter \"revive\" .
                Otherwise press enter anything.""")
                inu = input()
                if inu.replace(' ', '').lower() == "revive":
                    main()
                else:
                    oof += 1
            if user_input.replace(' ', '').lower() in west:
                break
            if user_input.replace(' ', '').lower() in south:
                pass
            if user_input.replace(' ', '').lower() in north:
                pass
            else: error()
        while True:
            print("""You reach the front of the house.
            In front of you stands a wooden door. What do you do?""")
            user_input = p.inputStr()
            if user_input.replace(' ', '').lower() == "opendoor":
                break
            if "go" in user_input.replace(' ', '').lower():
                main()
            else:
                error()
        print("""The door creaks open. The room inside is filled with darkness, with light seeping in through the opened door.
        You see a wooden table in front you. On the table lies a lantern, a bow and arrow and a slice a bread.
        On the floor you see a rugged carpet and a huge box lying in the corner of the room.
        """)
        while True:
            print("""What do you do?""")
            user_input = p.inputStr()
            if user_input.replace(' ', '').lower() == "openbox":
                print("""You try to open the box but its locked. The lock can only be opened with a two digit combination. First digit is 1.
                Beneath the box you find a yellow weathered paper which has something written on it. It reads,
                \"The Mughals you fought were led by Raja Maan Singh who commanded an army of about 80,000 Mughal troops against 20,000 Mewar soldiers.\"
                If all Mewari soldiers fought equal number of Mughal soldiers then how many Mughal soldiers fought one Mewar soldier?
                (find the answer to get the 2nd digit and enter both the digits to open the box)
                Your options are-
                a) 1
                b) 4
                c) 2
                """)
                user_input1 = p.inputNum()
                if user_input1 == 14:
                    inventory.append("Sword")
                    inventory.append("Medicines")
                    print('''
                    The box opens and you find a magnificent sword lying inside. The box also contains medicines.
                    You take the sword and put it around your waist.
                    History fact-
                    Akhbar's queen (one of Begum-e-Khaas) Jodha Bai was the paternal aunt of Raja Maan Singh of Amber. Akhbar took his responsibilty and trained him to be an excellent fighter
                    ''')
                else:
                    inc()

            if user_input.replace(' ', '').lower() == "takelantern":
                print("""you have taken the lantern""")
                inventory.append("Lantern")
            if user_input.replace(' ',''),lower() == "takebowandarrow":
                print("You have taken the Bow and Arrow.")
                inventory.append("Bow and Arrow")
            if "take" and ("bread" or "slice") in user_input.replace(' ', '').lower():
                print("You have taken the Slice of Bread")
                inventory.append("Slice of Bread")
            if "pick" and "carpet" in user_input.replace(' ', '').lower():
                print("You pick the carpet to discover a trap door.")
                trpd()

            if user_input.replace(' ',''),lower() in (west or north or east):
                print("You can't go that way.")
            if user_input.replace(' ',''),lower() in south:
                print("The wooden door behind you is closed.")
            if user_input.replace(' ',''),lower() == "opendoor":
                print("""You open the door and see a Mughal soldier who sees you at the same time and raises his bow to shoot you with an arrow.
                What do you do?
                """)
                

            else: error()


def trpd():
    print("What do you do?")








def inc():
    print("""The combination is incorrect. An arrow is fired from outside the house and pierces your leg. You turn around and see a Mughal soldier.
    You immediately close the door and fall to the ground.  """)

    print('''
    You suddenly find a secret underground tunnel under the carpet .
    The rim of the tunnel cover says ,'On an average a person can move inside this tunnel with the speed of 0.5m/s ,the tunnel is in the shape  of semicircle , the radius of tunnel is 7m.
    Find the time taken by you to reach the other end of the tunnel as the code to unlock the cover at the other end.''
    (Take pi=22/7 , answer in seconds)
    Your options are -
    a)44
    b)11
    c)22
    ''')






if __name__ == '__main__':
    background()


    possibility()
    main()
