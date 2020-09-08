#Imports
import os
import os.path
from os import path

userName =  input('What is your Username?: ') #Asks the user to write their Username and saves their response in the variable 'userName'

if path.exists(userName + '_Access_File.py') == True: #Checks to see if the Username entered has an account and password. If the account exists, it goes through. If not, it goes to creating the account.
    accessFile = open(userName + '_Access_File.py','r') #Opens the Access File for the entered user and opens it for reading.
    password = accessFile.read() #Saves the contents of the Access file, which is the password, as the variable 'password'
    accessFile.close() #Closes the Access File
    tries = 0 #Sets the variable 'tries' as the Integer '0'
    
    while True: #Starts a 'while True' loop. This loop continues until manually broken 
        print(' ') #Just prints a space
        passwd = input('What is your password?: ') #Asks the user for their password and saves it as the variable 'passwd'
        
        if passwd == password: #Checks to see if the password entered and the password in the Access File match.
            print('Welcome, User ' + userName) #If the password matches, this welcomes the user.
            print(' ')
            tries2 = 0 #Sets the 'tries2' variable to the Integer 0       
            
            while True: #Another 'while True' 
                print(' ')
                print('1) Read Notes') #List of possible actions by the user
                print('2) Edit Notes')
                print('3) Create Notes')
                print('4) List Notes')
                print('5) Log Out')
                print(' ')
                noteManager = input('What would you like to do?: ') #Asks the user what action they want to perform and save it in the variable 'noteManager'
                
                if noteManager == '1': #Reads notes
                    notelist = os.listdir('William_Note_Directory') #Lists the current notes and saves it in the variable 'notelist'
                    print(notelist) #Prints out the variable 'notelist'
                    while True:
                        noteview = input('Which note would you like to view?: ') #Asks the user what note they want to view and saves it in the variable 'noteview'
                        if path.exists('William_Note_Directory/' + noteview):
                            notefiler = open('William_Note_Directory/' + noteview,'r') #Opens the specified note's file
                            print(' ') #Some formatting
                            print('___________________')
                            print(' ')
                            print(notefiler.read()) #Prints the note
                            print('___________________')
                            break
                        else: #The note entered didn't exist
                            print('Sorry, that isn\'t a valid note')
                            print('Please try again')
                            
                elif noteManager == '2': #Edits notes
                    notelist = os.listdir('William_Note_Directory')
                    print(notelist)
                    noteview = input('Which note would you like to edit?: ')
                    os.system('nano ' + userName + '_Note_Directory/' + noteview)
                    #Set aside for editing notes
                    
                elif noteManager == '3': #Creates notes
                    noteTitle = input('What would you like to name your note? (No spaces or special characters): ')
                    os.listdir(userName + '_Note_Directory')                
                    os.system('nano ' + userName + '_Note_Directory/' + noteTitle)
                    noteList = open(r'Note_List_Registry','r+')
                elif noteManager == '4': #Lists notes
                    notelist = os.listdir('William_Note_Directory')
                    print(' ')
                    print('________________')
                    print(' ')
                    print(notelist)
                    print('________________')
                elif noteManager == '5':
                        loggy = input('Are you sure you want to log out?: ')
                        if loggy == 'Yes' or loggy == 'yes' or loggy == 'y' or loggy == 'Y':
                            print('Goodbye!')
                            exit()
                    #Set aside for creating notes
                else: 
                    tries2 = tries2 + 1 #Adds 1 to the variable 
                    if tries2 == 5:
                        exit('Too many failures. Please log in again')
                    else:
                        print('Sorry, that isn\'t valid. Please try again!') 
        else: #The password doesn't match
            tries = tries + 1 #Hikes the variable 'tries' up by 1 
            print(' ') 
            print('Sorry, that wasn\'t valid. Please try again') 
            if tries >= 3: #Checks if the variable 'tries' is equal to or bigger than 3. This would indicate 3 password failures
                print(' ')
                exit('Try again later!') #Boots you out 
else:
    print(' ')
    q1 = input('Hmm, that User doesn\'t seem to exist. Would you like to create them now?: ')
    if q1 == 'no' or q1 == 'No':
        print(' ')
        print('Goodbye!')
        exit()
    else:
        newName = userName
        while True:
             while True: 
                print(' ')
                newPasswd = input('What Password would you like to have for the User ' + userName + '?: ')
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
                print('Please try again')
             else:
                break
parentPath = os.getcwd() + '/' #Absolute path to current directory      
directory = newName + '_Note_Directory'
path = os.path.join(parentPath, directory) 
os.mkdir(path)
noteList = open(r'Note_List_Registry','w+')
newAccessFile = open(newName + '_Access_File.py','w+')
newAccessFile.write(newPasswd)
print(' ')
print('Your new User has been created with the password ' + newPasswd)
print(' ')
print('Try to log in again!')
exit()
