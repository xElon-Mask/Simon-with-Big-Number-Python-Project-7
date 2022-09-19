import time
import random
import os

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')