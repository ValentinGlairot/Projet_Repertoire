import time


# Arrete le programme
def endprogram():
    print("Fermeture du programme...")
    time.sleep(2)
    print("~~ Le programme est fini ~~")


# L'utilisateur ecrit le nom
def write():
    nom = input("-------------------------------------------------------------------------"
                "\nNom (écrire 0 pour annuler): ")
    if nom == '0':
        return
    else:
# enregistre les nom dans un fichier texte
        with open('repertoire.txt', 'a') as f:
            f.write("Nom:" + nom)
            f.close()
            print('Nom Enregistré')
        with open('repertoire.txt', 'a') as f:
            numero = input("Téléphone : ")
            f.write(" Le numero:" + numero + "\n")
            f.close()
            print('Numéro Enregistré')
        write()


#regarde dans le repertoire si les noms sont present
def read():
    i = 0
    with open('repertoire.txt', 'r') as f:
# L'utilisateur entre le nom qu'il recherche
        recherche = input("-------------------------------------------------------------------------"
                          "\nEntrer le nom du contact:")
        for ligne in f:
            if recherche in ligne:
                pos1 = ligne.find('m:')
                pos2 = ligne.find(' ')
                pos3 = ligne.find('o:')
                print(ligne[pos1 + 2: pos2] + ":" + ligne[pos3 + 2:])
                i += 1
        if i == 0:
            print("le contact", recherche, "n'a pas été trouvé dans le répertoire")
        f.close()


# boucle du menu
while True:
    a = int(input("""-------------------------------------------------------------------------
    0-quitter 
    1-écrire dans le répertoire 
    2-Rechercher dans le répertoire 
    Votre choix ?: """))
    if a == 0:
        endprogram()
        break
    if a == 1:
        write()
    if a == 2:
        read()
