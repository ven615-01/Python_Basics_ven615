# this is going to be implemented later as a way to modify and format text with colour "red_text = (f'\33[0;31m \033[0m')""
import subprocess
import sys

menu_seperator = ["#"]
menu_items = [
    '\33[0;31m01 - Functions\033[0m',
    '\33[0;31m02 - variables, int float\033[0m',
    '\33[0;31m      and Bool,\033[0m',
    '',
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
# Menu items/index
print('###################################')
print(f'# {menu_items[0]}(WIP)             #') #                01 - Functions
print(f'# {menu_items[1]}       #') #                           02 - Variables, int,float:
print(f'# {menu_items[2]}(WIP)            #') #                        -and Bool
print(f'# {menu_items[3]}                                #') #       (space)
print(f'# {menu_items[4]}(TBA)         #')#                     03 - if statements
print(f'# {menu_items[5]}(TBA)                 #') #            04 - loops
print(f'# {menu_items[6]}                      #') #            05 - lists
print(f'# {menu_items[7]}               #')  #                 x 06 - list methods
print('###################################')
print()
menu_item_picked = input("Type in the number corresponding to the chapter you would like to navigate to or type exit to quit: ")


if menu_item_picked == '1':
    subprocess.run([sys.executable, "Functions.py"])
if menu_item_picked == '2':
    subprocess.run([sys.executable, "Variables.py"])
if menu_item_picked == '3':
    print("Those options are being added and are currently unavailable")
    menu_item_picked = input("Type in the number corresponding to the chapter you would like to navigate to or type exit to quit: ")
if menu_item_picked == '4':
    print("Those options are being added and are currently unavailable")
    menu_item_picked = input("Type in the number corresponding to the chapter you would like to navigate to or type exit to quit: ")

if menu_item_picked == '5':
    print("Those options are being added and are currently unavailable")
    menu_item_picked = input("Type in the number corresponding to the chapter you would like to navigate to or type exit to quit: ")

if menu_item_picked == '6':
    print("opening List_methods.py")
    subprocess.run([sys.executable, "List_methods.py"]) #opens the chapter that is another python file
    print("Opening chapter List_methods.py")

if menu_item_picked == 'exit' or 'exit':
    print("Goodbye!!")
