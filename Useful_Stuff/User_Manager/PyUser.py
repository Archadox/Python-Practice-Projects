import os
import os.path
from os import path

userName =  input('What is your Username?: ')
if path.exists(userName + 'AccessFile.py') == True:
    accessFile = open(userName + 'AccessFile.py','r')
    password = accessFile.read()
    accessFile.close()
    tries = 0
    while True:
        print(' ')
        passwd = input('What is your password?: ')
        if passwd == password:
            print('Welcome, User ' + userName)
            exit()
        else:
            tries = tries + 1
            if tries >= 3:
                print(' ')
                exit('Try again later!')
else:
    print(' ')
    q1 = input('Hmm, that User doesn\'t seem to exist. Would you like to create them now?: ')
    if q1 == 'no' or q1 == 'No':
        print(' ')
        print('Goodbye!')
        exit()
    else:
        print(' ')
        newName = input('What Username would you like?: ')
        while True:
             while True: 
                print(' ')
                newPasswd = input('What Password would you like to have for this User?: ')
                print(' ')
                passwdConfirm = input('Please confirm your password: ')
                if newPasswd != passwdConfirm:
                    print(' ')
                    print('Sorry, your passwords do not match')
                    print(' ')
                    print('Please try again')
                else:
                    break       
             if len(newPasswd) < 5: 
                print(' ')
                print('Sorry, passwords must be over 5 characters')
                print(' ')
                print('Please try again')
             else:
                break
                
newAccessFile = open(newName + 'AccessFile.py','w+')
newAccessFile.write(newPasswd)
print(' ')
print('Your new User has been created with the password ' + newPasswd)
print(' ')
print('Welcome ' + newName + '!')
