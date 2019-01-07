import sys
from time import sleep
import random


def typing(output):
    punctuation = ",.?!\n"
    for char in output:
        if char in punctuation:
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(0.2)
        else:
            sleep(random.uniform(0, 0.05))
            sys.stdout.write(char)
            sys.stdout.flush()
    print('')
