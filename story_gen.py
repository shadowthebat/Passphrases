from bs4 import BeautifulSoup
import requests
import random
from menu import *
import os


def get_story_links():  # returns links to story pages
    source = requests.get('https://americanliterature.com/short-stories-for-children')
    soup = BeautifulSoup(source.text, 'lxml')
    links = list()
    for i in soup.find_all(class_="imgcs"):  # finds, filters and appends to links list
        if '/author' == i.a['href'][:7] or '/childr' == i.a['href'][:7]:
            links.append('https://americanliterature.com/' + i.a['href'])
    return links

# ISSUES: works for most links that start with /author/
# must do further tests with /childrens-stories/
# however sometimes the slice of text is off
# also to consider, I noted a page with a div poem instead of p
# as part of the story REF: https://americanliterature.com//author/hans-christian-andersen/short-story/the-last-dream-of-old-oak


def get_story_text(url):  # creates a .txt of the story from target url
    source = requests.get(url)
    soup = BeautifulSoup(source.text, 'lxml')
    texthtml = soup.find_all('p')[2:-6]  # list of <p>, sliced for target story
    story = ''  # empty string for story
    for i in texthtml:  # adds the text from the paragraphs into story string
        story += i.text
        story += '\n'
    title = soup.find('h1').text  # defines title of story
    title += '.txt'  # defines textfile name and extention
    with open(title, 'w') as f:  # saves story to text file appropriately titled
        f.write(story)
    print('')
    print(f'{title[:-4].upper()}.txt has been generated')
    print('')
    typing('Continue to main menu')
    print('')
    x = input('$: ')


def New_Story_Generator():  # this code will create a text file containing a childrens story
    text_files = Menu()
    text_files.set_text_files()
    text_files.display()
    index = input('Generate new story? [Y/N] or delete old story? [D] $: ').lower()
    while index != 'y' and index != 'n' and index != 'd':
        index = input('Generate new story? [Y/N] Or choose stories to delete? [D] $: ').lower()
    if index == 'y':
        story_links = get_story_links()
        get_story_text(random.choice(story_links))
    elif index == 'd':
        text_files.display()
        index = input('Select Files [# # # etc..]$: ')
        index_list = [int(x) for x in index.split()]
        for index in index_list:
            os.remove(text_files.selection[index])
            print(f'{text_files.selection[index]} has been deleted')
        print('')
        typing('Continue to main menu')
        print('')
        x = input('$: ')
