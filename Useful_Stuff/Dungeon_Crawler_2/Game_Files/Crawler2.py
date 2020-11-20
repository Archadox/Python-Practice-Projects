import os, time
from pynput.keyboard import Key, Listener

gameDir = '/home/william/Python-Practice-Projects/Useful_Stuff/Dungeon_Crawler_2/'

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
                uppity = None
                start_village()

    with Listener(
            on_press=on_press,
            on_release=spacey) as listener:
        listener.join()

def intro():
    #The intro that plays whenever the game is begun
    print('Type HELP to get a list of actions you can perform\n')
    print('Always type actions in all caps\n')

def namecheck():
    global name
    name = input('What is your travellers name?: ')
    try:
        with open (gameDir+'User_Files/'+name+'/'+name) as charfile:
            print(charfile.readlines())
    except FileNotFoundError:
        charcre()

def namesave():
    #Saves the name of the current player in a temporary file
    namefileer = open(gameDir+'Temporary_Files/Current_Player_Name', 'w+')
    namefileer.write(name)
    namefileer.close()

def charcre():
        butt = input('Would you like to create the character ' + name + ' now? YES/NO: ')
        if butt=='YES':
            os.mkdir(gameDir+'User_Files/'+name)
            charfile = open(gameDir+'User_Files/'+name+'/'+name, 'w+')
            print('')
            while True:
                corey = input('Would you like this character to be Hardcore? You would lose your save upon death. YES/NO: ')
                if corey == 'YES':
                    print('Don\'t make the wrong choice!')
                    charfile.write(gameDir+'User_Files/'+name+' \n0\nAlive\nHardcore')
                    charfile.close()
                    break
                elif corey == 'NO':
                    print('Okay, no Hardcore for you')
                    charfile.write(gameDir+'User_Files/'+name+' \n0\nAlive\nNormalcore')
                    charfile.close()
                    break
                else:
                    print('')
                    print('Input invalid. Please try again')
                    print('')

        elif butt == 'NO':
            print('Maybe another time')
            exit()

def inventory_check():
    #A function to check the inventory of the player
    pass

def game_help():
    #A function to show the list of actions the player can perform
    pass

def start_village():
    #The first village the player sees
    def spacey(key):
        if key == Key.esc:
            global uppity2
            # Stop listener
            return False
        elif key == Key.space:
            try:
                if uppity2 == 1:
                    print('Your grave stirrs as you awaken from your near eternal slumber\n')
                    uppity2 = uppity2+1
            except NameError:
                uppity2 = 1
            if uppity2 == 1:
                print('The village seems deserted apart from these silent watchers \nthat seem to poke their heads behind the bricks the moment your head swings in their direction\n')
                uppity2 = uppity2+1
            elif uppity2 == 2:
                print('You see a strange well, no bucket or water, but a ladder, leading into a seemingly endless depth\n')
                uppity2 = uppity2+1
            elif uppity2 == 3:
                print('One of the figures is standing near the well, too far to fully make out their features, but they clearly stare in your direction\n')
                uppity2 = uppity2+1
            elif uppity2 == 4:
                print('You begin walking over to the well, determined to find the secrets that hide within\n')
                uppity2 = uppity2+1
            elif uppity2 == 5:
                uppity2 = None
                return False

    with Listener(
            on_press=on_press,
            on_release=spacey) as listener:
        listener.join()

intro() #Introducing instructions, plays every time the game is started
namecheck() #Asks the user's name, if name doesn't exist, calls upon the charcre function to create it
#original_intro()
