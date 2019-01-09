from menu import *
from pass_gen import *
from char_counter import *
from story_gen import *


print('')
print('--Passphrase_Collection_STB--')
main_menu = Menu()
menu_items = ['Passphrase Accuracy Counter',
              'Passphrase Generator', 'Story Generator', 'Help']
functions = [Passphrase_Accuracy_Counter,
             Passphrase_Generator, Story_Generator, Help]
main_menu.set_from_scratch(menu_items)
main_menu.set_functions(functions)
main_menu.display()
main_menu.select()
