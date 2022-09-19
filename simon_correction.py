import time
import random
import os

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


chiffre = random.randint(0, 9)

print("Bienvenue dans le jeu du Simon")

# Génération de la séquence initiale
sequence = ""
for i in range(4):
    chiffre = random.randint(0, 9)
    sequence += str(chiffre)


