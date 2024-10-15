tableau=[1,2,3,4,5,6,7,8,9,10]


def recherche_max(tab):
    maxi = tab[0]
    for t in range(1,len(tab)) :
        if tab[t] > maxi :
            maxi = tab[t]
    return maxi


print(recherche_max(tableau))