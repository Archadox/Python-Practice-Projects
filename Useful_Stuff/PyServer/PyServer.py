import os
os.system('figlet Server List')
print('(Home PC Local) (P)aradoz')
print('(Home PC Remote) Parado(x)')
print(' ')
while True:
    server = input('What server would you like to log into?: ')
    if server == 'P' or server == 'X' or server == 'p' or server == 'x':
        break
    elif server == 'bye' or server == 'exit':
        exit()
    else:
        print('Sorry, that wasn\'t valid, please try again')

if server == 'p' or server == 'P':
    os.system('ssh P')
