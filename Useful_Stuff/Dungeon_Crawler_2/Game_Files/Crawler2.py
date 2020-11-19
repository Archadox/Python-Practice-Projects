#Seeing if the testing branch works
import os, time
import keyboard #A terrible choice in module because now the entire progrm has to be run as root
#Not good enough yet to try the alternatives

def original_intro():
    #Probably doesn't need to be a function but whatever
    #Designed to be executed by the charcre function after a successful character creation
    upperino = 1
    while True:
        if keyboard.is_pressed('space'):
            if upperino == 1:
                print('Your grave stirrs as you awaken from your near eternal slumber\n')
                upperino = 2
                time.sleep(.5)

            elif upperino == 2:
                print('You rise with a rusted sword in your hand and a key on your chest\n')
                upperino = 3
                time.sleep(.5)

            elif upperino == 3:
                print('Bla bla bla, you need to get powers to save an ancient kingdom\n')
                upperino = 4
                time.sleep(.5)

            elif upperino == 4:
                print('You enter a nearby village and purchase clothes with the ancient gold in your coffin\n')
                upperino = 5
                time.sleep(.5)

            elif upperino == 5:
                upperino = None
                #time.sleep(.1)
                break

def intro():
    #The intro that plays whenever the game is begun
    print('Type HELP to get a list of actions you can perform')
    print('')
    print('Always type actions in all caps')
    print('')

def namecheck():
    global name
    name = input('What is your travellers name?: ')
    try:
        with open ('../User_Files/'+name+'/'+name) as charfile:
            print(charfile.readlines())
    except FileNotFoundError:
        charcre()

def namesave():
    #Saves the name of the current player in a temporary file
    namefileer = open('../Temporary_Files/Current_Player_Name', 'w+')
    namefileer.write(name)
    namefileer.close()

def charcre():
    #A shittily named function to create the player's character if the character doesn't exist
    # global name
    # name = input('What is your travellers name?: ')
    # try:
    #     with open (name+'/'+name) as charfile:
    #         print(charfile.readlines())
    # except FileNotFoundError:
        butt = input('Would you like to create the character ' + name + ' now? YES/NO: ')
        if butt=='YES':
            os.mkdir('../User_Files/'+name)

            charfile = open('../User_Files/'+name+'/'+name, 'w+')
            # eldersup = open('../User_Files/'+name+'/eldersup', 'w+')
            # eldersup.write('0')
            # arrival = open('../User_Files/'+name+'/arrival', 'w+')
            # arrival.write('0')
            # villagestatus = open('../User_Files/'+name+'/villagestatus', 'w+')
            # villagestatus.write('1')
            print('')
            while True:
                corey = input('Would you like this character to be Hardcore? You would lose your save upon death. YES/NO: ')
                if corey == 'YES':
                    print('Don\'t make the wrong choice!')
                    charfile.write('../User_Files/'+name+' \n0\nAlive\nHardcore')
                    charfile.close()
                    break
                elif corey == 'NO':
                    print('Okay, no Hardcore for you')
                    charfile.write('../User_Files/'+name+' \n0\nAlive\nNormalcore')
                    charfile.close()
                    break
                else:
                    print('')
                    print('Input invalid. Please try again')
                    print('')

def inventory_check():
    #A function to check the inventory of the player
    pass

def game_help():
    #A function to show the list of actions the player can perform
    pass

#def start_village()


#intro() #Introducing instructions, plays every time the game is started
#namecheck() #Asks the user's name, if name doesn't exist, calls upon the charcre function to create it
original_intro()
