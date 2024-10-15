tab=[3,1,6,3,9,5,6,7]

def recherche(tab, n):
    indice = -1
    i = 0
    for t in tab :
        if n == t :
            indice = tab[n]
        i = i + 1
    return indice

print(recherche(tab,4))