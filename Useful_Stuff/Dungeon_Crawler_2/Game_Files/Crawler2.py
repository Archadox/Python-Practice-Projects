import os, sys

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
            eldersup = open('../User_Files/'+name+'/eldersup', 'w+')
            eldersup.write('0')
            arrival = open('../User_Files/'+name+'/arrival', 'w+')
            arrival.write('0')
            villagestatus = open('../User_Files/'+name+'/villagestatus', 'w+')
            villagestatus.write('1')
            print('')
            while True:
                corey = input('Would you like this character to be Hardcore? You would lose your save upon death. YES/NO: ')
                if corey == 'YES':
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
