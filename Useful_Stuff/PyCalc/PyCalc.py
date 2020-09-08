import os 
import pyfiglet
print(pyfiglet.figlet_format('PyCalc'))
#os.system('figlet PyCalc')
print('Simple Python Calculator')
while True:
    Equation_Var = input()
    if Equation_Var == 'bye' or Equation_Var == 'exit':
            print('Goodbye!')
            break
    exec('print(' + Equation_Var + ')')
#    Last_Equation = open(r"Last_Equation","w+")
 #   Last_Equation.truncate()
  #  Last_Equation.write()
   # Last_Equation.close()
