import random

# passphrase generator randomly generates passphrase
# from words found in textfile paramater
# until min char count acheived
# returns passphrase and wordcount of passphrase


def passphrase_gen(textfile, min_char):
    with open(textfile, 'r') as f:  # imports story string from textfile as story
        story = f.read()

    story_punctuated = story.split()  # splits story's words into list
    story = list()  # story is now empty so we can store words without punctuation
    punc = '.!?\"\',;:()'  # punctuation defined in string

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

    print(pass_list)  # prints list of words for readability
    print(p_phrase)
    print(len(p_phrase))


passphrase_gen('tandh.txt', 22)
