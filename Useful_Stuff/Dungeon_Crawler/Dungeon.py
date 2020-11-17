import os, sys
#Designed to mimick Elderbug from Hollow Knight lmao
print('Type the bolded text to make choices. Always type in all caps to make the choices.')
print('')
print('Keep in mind, this is hardcore. You die, your save is gone.')
print('')
name = input('What is your travellers name?: ')

try:
    with open (name) as charfile:
        print(charfile.readlines())
except FileNotFoundError:
    while True:
        butt = input('Would you like to create the character ' + name + ' now? YES/NO: ') 
        if butt=='YES':
            os.mkdir(name)
            charfile = open(name+'/'+name, 'w+')
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
                    print('Input invalid. Please try again')
                    
            print('Okay, character created!')
            break
        elif butt =='NO':
            print('Alright, maybe some other time!')
            exit()
        else:
            print('Input invalid. Please try again')
    
print('')
print('Your name is '+ name +' and you are travelling through this forgotten kingdom with no weapon or magic')
print('You see a village')
print('In the village is an elder man and a well that decends into deep catacombs, likely containing great treasure and hidden beasts') 
while True:
    relder = input('Do you speak with the ELDER, or decend into the RUINS?: ')
    if relder==('RUINS'):
        print('You climb into the damp, musty stone well. The ladder creaks and you fear it will give under your weight.')
        print('Your feet touch moist ground, and you open your eyes.')
        print('You can barely see, except for the door glowing, blocking the path in front of you.')
        print('There is a fancy keyhole in the door.')
        print('')
        stoopid = input('Do you try to FORCE the ancient glowing artifact holding immesurable magic, or ASCEND to perhaps find the ornate key.')
        print('')
        if stoopid == 'FORCE':
            print('Nice one dumbass, a surge of magic flows through your body, you collapse and die.')
            charfile = open(name+'/'+name, 'w+')
            charfile.write(name+' \n0\nAlive')
            charfile.close()
            exit()
        elif stoopid == 'ASCEND':
            print('You climb back up the well, the ladder threatening to shatter upon every step until finally, you reach the top')
    elif relder==('ELDER'):
        break
print('Yahooo')
