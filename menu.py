import os
import sys
from time import sleep
import random
from typing import typing


class Menu:
    """
            Template for creating command line menus with functionality
    """

    def __init__(self):
        self.items = []
        self.title = 'menu'
        self.selection = {}

    def set_title(self, title):
        """
            Sets the title of the menu
        """
        self.title = title

    def set_from_scratch(self, items_list):
        """
            Creates menu items with indexes
        """
        index = 1
        for i in items_list:
            self.items.append('')
            self.items.append(f' {index}: {str(i)}')
            index += 1

    def set_functions(self, functions_list):
        """
            Associates functions to appropriate indexes
        """
        index = 1
        for i in functions_list:
            self.selection[index] = i
            index += 1

    def set_text_files(self):
        """
            Alternative to set from scratch.
            Creates menu(sets item and index) from text files in working directory
        """
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

    def display(self):
        """
            Displays the menu to console
        """
        sleep(0.3)
        print('')
        # Print title
        typing(f'-- {self.title.upper()} --')
        sleep(0.5)
        print('')
        # Print menu item one by one
        for line in self.items:
            sleep(0.0075)
            print(line)
        print('')
        sleep(0.0075)
        # Adds Quit option at index 0
        print(' 0: Quit')
        print('')

    def select(self):
        """
            Continuously prompts user for input, calls appropriate function based on index(input) given
            Loop until input == 0 (Quit)
        """
        cmd = int(input('$: '))
        while cmd != 0:
            for i in self.selection:
                if i == cmd:
                    self.selection[i]()
                    self.display()
                    cmd = int(input('$: '))

# Note: update function to import HELP SECTION from txt file instead of printing each line
# Note: remember to exclude HELP SECTION txt file from Menu.Method: self.set_text_files()


def Help():
        """
            Prints description of program functionality
        """
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
