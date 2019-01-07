from bs4 import BeautifulSoup
import requests


def get_story_links():  # returns links to story pages
    source = requests.get('https://americanliterature.com/short-stories-for-children')
    soup = BeautifulSoup(source.text, 'lxml')
    links = list()
    for i in soup.find_all(class_="imgcs"):
        links.append('https://americanliterature.com/' + i.a['href'])
    return links


def get_story_text(url):  # creates a string of the story from target url
    if 'https://americanliterature.com//author/' in url:
        source = requests.get(url)
        soup = BeautifulSoup(source.text, 'lxml')
        texthtml = soup.find_all('p')[2:-6]  # list of <p>, sliced for target story
        story = ''  # empty string for story
        for i in texthtml:  # adds the text from the paragraphs into story string
            story += i.text
        print(story)


story_links = get_story_links()
get_story_text(
    'https://americanliterature.com//author/hans-christian-andersen/short-story/the-last-dream-of-old-oak')
# get_story_text(random.choice(story_links))
