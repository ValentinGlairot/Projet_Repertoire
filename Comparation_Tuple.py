annee2019 = [('janvier', 6), ('février', 6), ('mars', 12), ('avril', 20), 
             ('mai', 23), ('juin', 25), ('juillet', 29), ('août', 25), 
             ('septembre', 22), ('octobre', 15), ('novembre', 11), ('décembre', 7)]

m = annee2019[0][1]
print(f"Valeur initiale de m : {m}")

for mois in annee2019:
    if m > mois[1]:
        m = mois[1]
        print(f"Nouvelle valeur de m après comparaison avec {mois[0]} : {m}")

print(f"La plus petite valeur trouvée : {m}")
