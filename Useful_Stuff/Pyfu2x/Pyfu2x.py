#!/bin/python
import os
while True:
    format = input('Is the original a jpg or png?: ')
    if format == 'jpg' or format == 'png':
        break
    else:
        print(' ')
        print('Sorry that isn\'t valid, please try again.')
        print(' ')
print(' ')

while True:
    noise = input('How much noise removal do you want in the upscale? (0 - 3): ')
    if noise == '0' or noise == '1' or noise == '2' or noise == '3':
        break
    else:
        print(' ')
        print('Sorry that isn\'t valid, please try again.')
        print(' ')
print(' ')
while True:
    level = input('How many levels of upscaling do you want? (Limit five which is ridiculous): ')
    if level == '1' or level == '2' or level == '3' or level == '4' or level == '5':
        break
    else:
        print(' ')
        print('Sorry that isn\'t valid, please try again.')
        print(' ')
print(' ')        
turbo = input('Yes or No. Enable turbo mode? Takes significanty longer but produces an eight times better upscale: ')

if turbo == 'yes' or turbo == 'Yes' or turbo == 'y' or turbo == 'Y':
    turbo1 = '-x'
else:
    turbo1 = ''
if level == '5' and turbo1 == '-x':
    print(' ')
    print('This is a MASSIVE warning')
    print(' ')    
    print('You are about to execute the command on maximum settings')
    print(' ')
    print('This is very likely not necessary but I know that won\'t deter you')
    print(' ')
    print('This will make the image sharp in a way your eyes can\'t comprehend, it\'s pointless to do so')
    print(' ')
    print('It will also take a very long time especially the fifth iteration')
    print(' ')
    print('This will majorly tax your graphics card. Do NOT attempt this on a laptop. Do NOT attempt this on lower grade hardware. DO NOT attempt this in a VM without GPU passthrough')
    print(' ')
    print('If you truly want to proceed, type \'PROCEED\'')
    print(' ')
    proceed = input()
    if proceed != 'PROCEED':
        exit()
    else:
        pass
        

lev5 = 'waifu2x-ncnn-vulkan -i Original.'+ format +' -o Upscale1.png -n '+ noise +' '+ turbo1 +' && waifu2x-ncnn-vulkan -i Upscale1.png -o Upscale2.png -n '+ noise +' '+ turbo1 +' && waifu2x-ncnn-vulkan -i Upscale2.png -o Upscale3.png -n '+ noise +' '+ turbo1 +' && waifu2x-ncnn-vulkan -i Upscale3.png -o Upscale4.png -n '+ noise +' '+ turbo1 +' && waifu2x-ncnn-vulkan -i Upscale4.png -o Upscale5.png -n '+ noise +' '+ turbo1
lev4 = 'waifu2x-ncnn-vulkan -i Original.' + format +' -o Upscale1.png -n ' + noise +' ' + turbo1 +' && waifu2x-ncnn-vulkan -i Upscale1.png -o Upscale2.png -n ' + noise +' ' + turbo1 +' && waifu2x-ncnn-vulkan -i Upscale2.png -o Upscale3.png -n ' + noise +' ' + turbo1 +' && waifu2x-ncnn-vulkan -i Upscale3.png -o Upscale4.png -n ' + noise +' ' + turbo1 
lev3 = 'waifu2x-ncnn-vulkan -i Original.' + format +' -o Upscale1.png -n ' + noise +' ' + turbo1 +' && waifu2x-ncnn-vulkan -i Upscale1.png -o Upscale2.png -n ' + noise +' ' + turbo1 +' && waifu2x-ncnn-vulkan -i Upscale2.png -o Upscale3.png -n ' + noise +' ' + turbo1
lev2 = 'waifu2x-ncnn-vulkan -i Original.' + format +' -o Upscale1.png -n ' + noise +' ' + turbo1 +' && waifu2x-ncnn-vulkan -i Upscale1.png -o Upscale2.png -n ' + noise +' ' + turbo1
lev1 = 'waifu2x-ncnn-vulkan -i Original.' + format +' -o Upscale1.png -n ' + noise +' ' + turbo1
if level == '5':
    print(lev5)         
    os.system(lev5)
    
elif level == '4':
    print(lev4)
    os.system(lev4)
    
elif level == '3':
    print(lev3)
    os.system(lev3)
    
elif level == '2':
    print(lev2)    
    os.system(lev2)
       
elif level == '1':
    print(lev1)
    os.system(lev1)   
