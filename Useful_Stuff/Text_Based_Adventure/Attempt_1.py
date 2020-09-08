import os 
from os import path

charName = input('What is your character name? (No spaces or special characters): ')
existence = path.exists(charName + '_Char_File')
if existence == False:
    print(' ')
    creator = input('Hmm, that character doesn\'t seem to exist. Would you like to create them now?: ')
    if creator == 'yes' or creator == 'Yes' or creator == 'y' or creator == 'Y':
        charFiler = open(charName + '_Char_File','w+')
        print(' ')
        print('The character ' + charName + ' has been created!')
        print('Try to log in again!')
    else:
        print(' ')
        exit('Goodbye!')    
     
print('You are an explorer who has recently found the ancient elven ruin Drakkesta')
print('Your possesions consist of a Steel Dagger, a bag to contain your stuff and knowlege of some healing spells')
