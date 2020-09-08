name    = input('What is your name?: ')
age     = input('What is your age?: ')
dream   = input('What is your dream job?: ')
current = input('What is your current job?: ')

if dream == current:
    print('Your name is ' + name + ' and you are ' + age + ' years old. Your dream job is ' + dream + ' and you accomplished it! Good job!')
else:
    print('Your name is ' + name + ' and you are ' + age + ' years old. Your dream job is ' + dream + ' and your current job is ' + current)
    
