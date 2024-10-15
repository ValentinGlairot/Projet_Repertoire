# Données de l'année 2019
annee2019 = [('janvier', 6), ('fevrier', 6), ('mars', 12),
             ('avril', 20), ('mai', 23), ('juin', 25),
             ('juillet', 29), ('aout', 25), ('septembre', 22),
             ('octobre', 15), ('novembre', 11), ('decembre', 7)]

z = annee2019[0][1]

# Trouver le mois avec la plus haute valeur
for mois in annee2019:
    if z < mois[1]:
        z = mois[1]

print(f"Valeur maximale des mois en 2019: {z}")

# Création d'un tableau avec une condition
tab = [5, 3, 4, 8]
mon_tab = [2 * t for t in tab if t > 4]
print(f"Mon tableau modifié : {mon_tab}")

# Extraction de données d'une matrice
m = [[1, 3, 4],
     [5, 6, 8],
     [2, 1, 3],
     [7, 8, 15]]
a = m[0][2]
print(f"Valeur extraite de la matrice : {a}")

# Somme des éléments d'une sous-matrice
m = [[1, 3],
     [5, 8],
     [2, 3]]
nb_colonne = 2
nb_ligne = 2
b = 0
for i in range(0, nb_ligne):
    for j in range(0, nb_colonne):
        b = b + m[i][j]
print(f"Somme des éléments de la sous-matrice : {b}")

# Recherche du maximum dans un tableau
tab = [4, 3, 0, 5]
def recherche_max(tab):
    maxi = 0
    for t in tab:
        if t > maxi:
            maxi = t
    return maxi

print(f"Maximum trouvé dans le tableau : {recherche_max(tab)}")

# Somme des éléments d'un tableau
tab1 = [3, 5, 8, 4]
def somme(tab1):
    s = 0
    for t in tab1:
        s = s + t
    return s

print(f"Somme des éléments de tab1 : {somme(tab1)}")

# Moyenne des éléments d'un tableau
tab = [1, 2, 3]
def moyenne(tab):
    somme = 0
    for i in tab:
        somme = somme + i
    y = somme / len(tab)
    return y

print(f"Moyenne des éléments du tableau : {moyenne(tab)}")

# Recherche d'un élément dans un tableau
def recherche(tab, n):
    indice = -1
    i = 0
    for t in tab:
        if n == t:
            indice = i
        i = i + 1
    return indice

n = 3
print(f"Indice de l'élément {n} dans tab : {recherche(tab, n)}")

# Parité d'un tableau
liste = [1.2, 3.25]
def parite(test):
    a = False
    for x in test:
        if x % 2 == 0:
            a = True
        return a

print(f"Le tableau contient un nombre pair ? {parite(liste)}")
