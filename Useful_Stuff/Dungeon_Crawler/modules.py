import os

def nameque():
    global name
    name = input('What is your travellers name?: ')

def charcre():
    #A shittily named function to create the player's character if the character doesn't exist
    # global name
    # name = input('What is your travellers name?: ')
    try:
        with open (name+'/'+name) as charfile:
            print(charfile.readlines())
    except FileNotFoundError:
        butt = input('Would you like to create the character ' + name + ' now? YES/NO: ') 
        if butt=='YES':
            os.mkdir(name)
            charfile = open(name+'/'+name, 'w+')
            eldersup = open(name+'/eldersup', 'w+')
            eldersup.write('0')
            arrival = open(name+'/arrival', 'w+')
            arrival.write('0')
            villagestatus = open(name+'/villagestatus', 'w+')
            villagestatus.write('1')
            print('')
            while True:
                corey = input('Would you like this character to be Hardcore? You would lose your save upon death. YES/NO: ')
                if corey == 'YES':
                    charfile.write(name+' \n0\nAlive\nHardcore')
                    charfile.close()
                    break
                elif corey == 'NO':
                    print('Okay, no Hardcore for you')
                    charfile.write(name+' \n0\nAlive\nNormalcore')
                    charfile.close()
                    break
                else:
                    print('')
                    print('Input invalid. Please try again')
                    print('')

#def death():
    #A module called upon when the character dies
    #print('filler lmao')

def village():
    villagestatus = open(name+'/villagestatus', 'r')
    stats = villagestatus.read()

    if villagestatus == '1':
        village1()
    elif villagestatus == '2':
        village2()
    else:
        print('Either I fucked up my code, or you fucked with the game files') 
        exit()

def intro():
    global name    
    #A function that runs the intro sequence. Should only be run once so its not very useful.
    print('')
    print('Your name is '+ name +' and you are travelling through this forgotten kingdom with no weapon or magic')
    print('You see a village')
    print('In the village is an elder man and a well that decends into deep catacombs, likely containing great treasure and hidden beasts')     

def village1():
    #The starting village hub. As the game progresses, different functions will take over such as "village2()"
    relder = input('Do you speak with the ELDER, or decend into the RUINS?: ')
    if relder==('RUINS'):
        arrival = open(name+'/arrival', 'r')
        contents = arrival.read()
        arrival.close()
        if contents == '0':
            arrival = open(name+'/arrival', 'w+')
            arrival.write('1')
            arrival.close()
        elif contents == '1':
            pass
        elif contents == '2':
            pass
        else:
            print('Either you fucked with character files, or I fucked up my code')
            exit()
        print('You climb into the damp, musty stone well. The ladder creaks and you fear it will give under your weight.')
        print('Your feet touch moist ground, and you open your eyes.')
        print('You can barely see, except for the door glowing, blocking the path in front of you.')
        print('There is a fancy keyhole in the door.')
        print('')
        stoopid = input('Do you try to FORCE the ancient glowing artifact holding immesurable magic, or ASCEND to perhaps find the ornate key.')
        print('')
        if stoopid == 'FORCE':
            print('Nice one dumbass, a surge of magic flows through your body, you collapse and die.')
            #charfile = open(name+'/'+name, 'w+')
            #charfile.write(name+' \n0\nAlive')
            #charfile.close()
            exit()
        elif stoopid == 'ASCEND':
            print('You climb back up the well, the ladder threatening to shatter upon every step until finally, you reach the village again')
            village1()
    elif relder==('ELDER'):
        arrival = open(name+'/arrival', 'r')
        contents = arrival.read()
        arrival.close()
        if arrival == '1':
            print('The elder begins speaking, \n \"Ohoho! What an eagerness for exploration! When you arrived in my itty bitty town, you simply walked right past me and into those old crypts\"')
            print('\"Those ruins were locked away centuries ago, before my time, but you... you seem to have a desire for adventure that I can\'t turn down.\"')
            pass
        elif arrival == '0':
            print('The elder begins speaking, \n \"Hello kind sir, if you are seeking to enter that ancient crypt, you will need a key and perhaps a weapon\"')
            pass
        stupidchoice = input('Will you ACCEPT the sword and key, or REFUSE and venture into the dungeon unassisted? ')
        while True:
            if stupidchoice == 'ACCEPT': 
                eldersup = open(name+'/eldersup', 'w+')
                eldersup.write('2')
                print('The handle of the handcrafted blade is warm in your hand, and ancient weapon, infused with secrets untold')
                print('The elder thanks you for taking the items off his hands')
                villagestatus = open(name+'/villagestatus', 'w+')
                villagestatus.write('2')
                village2()

            elif stupidchoice == 'REFUSE':
                print('Seriously? This is the easiest choice in the goddamn game. Are you braindead? Holy shit')
                village1()

            else:
                print('')
                print('Input invalid. Please try again')
                print('')
                
def village2():
    relder = input('Do you speak with the ELDER, or decend into the RUINS?: ')
    if relder == 'RUINS':
        print('The sword weighs heavily on your back as you decend down the rickety old ladder')
