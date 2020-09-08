import os

os.system('figlet Server List:')

print('(Home PC) Paradoz')
print(' ')
server = input('What server do you want to log into?: ')

if server == 'P':
    os.system('ssh P')
    
else:    
    server = input('Sorry, that wasn\'t valid. Please try again: ')
    if server == 'P':
        os.system('ssh P')

    else:
        server = input('Last chance dumbass: ')
        if server == 'P':
            os.system('ssh P')
            
        else:
            print('You\'re not just wrong, you\'re stupid')               
            os.system('bash')    
