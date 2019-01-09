import os
import sys
from time import sleep
import random
from typing import typing


class Menu:
    def __init__(self):
        self.items = []
        self.title = 'menu'
        self.selection = {}

    def set_title(self, title):  # sets menu title
        self.title = title

    def set_from_scratch(self, items_list):  # appends list of menu items with index
        index = 1
        for i in items_list:
            self.items.append('')
            self.items.append(f' {index}: {str(i)}')
            index += 1

    def set_functions(self, functions_list):
        index = 1
        for i in functions_list:
            self.selection[index] = i
            index += 1

    def set_text_files(self):  # sets up menu items with index based on text files in working directory
        files = os.listdir()
        self.title = 'text files'
        index = 1
        for i in files:
            if '.txt' in i:
                # adds empty string before each textfile in list for redability
                self.items.append('')
                self.items.append(f' {index}: {i[:-4]}')  # add textfile with index to list
                self.selection[index] = i
                index += 1

    def display(self):  # Display's main menu
        sleep(0.3)
        print('')
        typing(f'-- {self.title.upper()} --')
        sleep(0.5)
        print('')
        for line in self.items:
            sleep(0.0075)
            print(line)
        print('')
        sleep(0.0075)
        print(' 0: Quit')
        print('')

    def select(self):
        cmd = int(input('$: '))
        while cmd != 0:
            for i in self.selection:
                if i == cmd:
                    self.selection[i]()
                    self.display()
                    cmd = int(input('$: '))


def Help():
    print('-- HELP SECTION --')
    print('')
    print('Passphrase Accuracy Counter:')
    print('For testing the accuracy of typing a new passphrase')
    print('while keeping track of it\'s character count.')
    print('')
    print('Passphrase Generator:')
    print('Generates passphrase based on a childrens story')
    print('')
    print('')
    print('Story Generator:')
    print('Generates / deletes children\'s stories')
    print('')
    print('')
    print('')
    typing('Continue to main menu')
    print('')
    x = input('$: ')
