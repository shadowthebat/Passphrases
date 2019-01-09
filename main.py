import os
import sys
from time import sleep
import random
from passphrase_gen import *


class Menu:
    def __init__(self):
        self.items = []
        self.title = 'menu'

    def set_title(title):  # sets menu title
        self.title = title

    def set_from_scratch(self, items_list):  # appends list of menu items with index
        index = 1
        for i in items_list:
            self.items.append('')
            self.items.append(f' {index}: {i}')

    def set_text_files(self):  # sets up menu items with index based on text files in working directory
        files = os.listdir()
        index = 1
        for i in files:
            if '.txt' in i:
                # adds empty string before each textfile in list for redability
                self.items.append('')
                self.items.append(f' {index}: {i[:-4]}')  # add textfile with index to list
                index += 1

    def display(self):  # Display's main menu
        sleep(0.3)
        typing(f'-- {self.title.upper()} --')
        sleep(0.5)
        print('')
        for line in self.items:
            sleep(0.0075)
            print(line)
        print('')


def typing(output):
    punctuation = ",.?!"
    for char in output:
        if char in punctuation:
            sleep(0.4)
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.4)
        else:
            sleep(random.uniform(0, 0.10))
            sys.stdout.write(char)
            sys.stdout.flush()


print('')
print('--Passphrase_STB--')
print('')
main_menu = Menu()
main_menu_items = ['Passphrase Character Counter',
                   'Passphrase Generator', 'Generate New Text File', 'Quit']
main_menu.set_from_scratch(main_menu_items)
main_menu.display()

t_menu = Menu()
t_menu.set_text_files()
t_menu.display()


'''
print('Chose from existing file: F')
print('or')
print('Generate new file: G')
print('')
start = input('F or G: ')
start = start.lower()
if start == 'f':
    input_t = input('Enter text file: ')
    input_len = input('Enter minimum desired passphrase length: ')
    input_len = int(input_len)
    print('')
    passphrase_gen(input_t, input_len)
    print('')
    print('Generate new phrase same')
'''
