#Seeing if the testing branch works
#Going to try to replace the keyboard module with a better one that doesn't require root
#Also, the current original_intro implementation is ass, so this will hopefully tighten it up

import os, time
from pynput.keyboard import Key, Listener
#import keyboard
#A terrible choice in module because now the entire progrm has to be run as root
#Not good enough yet to try the alternatives

def on_press(key):
    # print('{0} pressed'.format(
    #     key))
    pass

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

def listen_activator():
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

def original_intro():
    print('Press SPACE to advance the text\n')
    def spacey(key):
        global uppity
        if key == Key.esc:
            # Stop listener
            return False
        elif key == Key.space:
            try:
                if uppity == 1:
                    print('Your grave stirrs as you awaken from your near eternal slumber\n')
                    uppity = uppity+1
            except NameError:
                uppity = 1
            if uppity == 1:
                print('Your grave stirrs as you awaken from your near eternal slumber\n')
                uppity = uppity+1
            elif uppity == 2:
                print('You rise with a rusted sword in your hand and a key on your chest\n')
                uppity = uppity+1
            elif uppity == 3:
                print('Bla bla bla, you need to get powers to save an ancient kingdom\n')
                uppity = uppity+1
            elif uppity == 4:
                print('You enter a nearby village and purchase clothes with the ancient gold in your coffin\n')
                uppity = uppity+1
            elif uppity == 5:
                uppity = None
                return False
    with Listener(
            on_press=on_press,
            on_release=spacey) as listener:
        listener.join()

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
