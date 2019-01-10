import sys
from time import sleep
import random


def typing(output):
    """
        Prints string to console simulating a 'typing on keyboard' effect
    """
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
