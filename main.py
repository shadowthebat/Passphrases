from menu import *
from pass_gen import *
from char_counter import *
from story_gen import *


print('')
print('--Passphrase_Collection_STB--')
main_menu = Menu()

# Defines menu items for main_menu display
menu_items = ['Passphrase Accuracy Counter',
              'Passphrase Generator', 'Story Generator', 'Help']
# Defines functions for main_menu selection
functions = [Passphrase_Accuracy_Counter,
             Passphrase_Generator, Story_Generator, Help]

# Adds items to main_menu
main_menu.set_from_scratch(menu_items)
# Adds functions to main_menu
main_menu.set_functions(functions)

main_menu.display()  # Prints the main menu
main_menu.select()  # Awaits user input on loop until valid input or 0 to exit
