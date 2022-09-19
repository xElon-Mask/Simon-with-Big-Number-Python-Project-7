"""
0 - Générer une chaine de caractère qui contient 4 chiffres aléatoires, c'est votre séquence initiale.

1 - Ajouter un nouveau nombre aléatoire à la fin de votre séquence

2 - Nettoyer l'écran et affichez "Retenez la séquence" pendant 1 seconde

3 - Afficher la séquence à mémoriser pendant 3 secondes

4 - Nettoyer n'écran et demander la réponse à l'utilisateur

5 - Si la réponse est bonne, afficher pendant 1 seconde "Bonne réponse, votre score est : xxx", puis reboucler à l'étape 1

5bis - Si la réponse n'est pas bonne, sortir du programme et afficher : "Mauvaise réponse, la séquence était : xxxx, votre score final : xxxx"
"""
import random
import os
import time

# fonction qui nettoie le terminal
def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

# Génération d'une chaine de caractère qui contient 4 chiffres aléatoires,la séquence de démarrage du jeu
n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)
n4 = random.randint(0, 9)
Initial_Sequence = str(n1) + str(n2) + str(n3) + str(n4)

score_user = 0

# algorithme du jeu
while True:
    Initial_Sequence = Initial_Sequence + str(random.randint(0, 9))
    print(f"Retenez la séquence : {Initial_Sequence}")
    time.sleep(3)
    clear_screen()
    reponse_utilisateur = input("Quel était le nombre affiché ?")
    if Initial_Sequence == reponse_utilisateur:
        score_user += 1
        print(f"Bonne réponse, votre score est : {score_user}")
    else:
        print(f"Mauvaise réponse, la séquence était : {Initial_Sequence}, votre score final : {score_user}")
        exit()
    
