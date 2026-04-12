# this is going to be implemented later as a way to modify and format text with colour "red_text = (f'\33[0;31m \033[0m')""
import subprocess
import sys

menu_seperator = ["#"]
menu_items = [
    '\33[0;31m01 - variables(to be added)\033[0m',
    '\33[0;31m02 - int,str,bool\033[0m',
    '\33[0;31m03 - if statements\033[0m',
    '\33[0;31m04 - loops\033[0m',
    '\33[0;31m05 - lists\033[0m',
    '\33[0;31m06 - list methods\033[0m',
]
print()
print("Welcome to my tutorial where I will basically be documenting everything I learn")
print("in the hopes of teaching other newbies by documenting my learning process")
print()
print("TBA = To Be Added")
print()
print('###################################')
print(f'# {menu_items[0]}(TBA)#')
print(f'# {menu_items[1]}(TBA)          #')
print(f'# {menu_items[2]}(TBA)         #')
print(f'# {menu_items[3]}(TBA)                 #')
print(f'# {menu_items[4]}(TBA)                 #')
print(f'# {menu_items[5]}               #')
print('###################################')
print()
menu_item_picked = int(input("Type in the number corresponding to the chapter you would like to navigate to: "))

if menu_item_picked == int(6):
    print("opening List_methods.py")
    subprocess.run([sys.executable, "List_methods.py"]) #opens the chapter that is another python file
    print("Opening chapter List_methods.py")