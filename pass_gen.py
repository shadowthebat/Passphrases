import random
from menu import *
from time import sleep
from typing import *

# passphrase generator randomly generates passphrase
# from words found in textfile paramater
# until min char count acheived
# returns passphrase and wordcount of passphrase


def Passphrase_Generator():
    text_files = Menu()
    text_files.set_text_files()
    text_files.set_title('choose story from which a passphrase will be generated')
    text_files.display()
    index = int(input('$: '))
    min_char = int(input('Enter minimum character length for passphrase $: '))
    with open(text_files.selection[index], 'r') as f:  # imports story string from textfile as story
        story = f.read()

    story_punctuated = story.split()  # splits story's words into list
    story = list()  # story is now empty so we can store words without punctuation
    punc = '.!?\"\',;:()-_[]{}1234567890'  # punctuation and numbers defined in string

    for word in story_punctuated:  # removes punctuation from words and appends to story
        newword = ''
        for letter in word:
            if letter not in punc:
                newword += letter
        story.append(newword.lower())

    p_phrase = ''  # empty string to store passphrase
    pass_list = []
    while len(p_phrase) < min_char:  # will continue to add random word to p_phrase until p_phrase is long enough
        choice = random.choice(story)
        p_phrase += choice
        pass_list.append(choice)

    print('')
    print('Passphrase generated:')
    print(p_phrase)
    print('')
    print(f'from the words:')
    print(pass_list)
    print('')
    print(f'Length: {len(p_phrase)}')
    print('')
    typing('Continue to main menu')
    print('')
    x = input('$: ')
