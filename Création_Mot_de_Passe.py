import random
import string
import csv

def mot_de_passe():
    liste = []
    for _ in range(1239):
        chiffre = random.randint(10, 99)
        lettres = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        mdp = f"{lettres}{chiffre}"
        liste.append(mdp)
    return liste

def exporter(tableau, nom_fichier):
    with open(nom_fichier, "w", newline='') as fichier:
        writer = csv.writer(fichier)
        for row in tableau:
            writer.writerow([row])

tableau_mdp = mot_de_passe()

print(tableau_mdp)

exporter(tableau_mdp, 'mots_de_passe.csv')
