tab=[1,2,3,4,5,6,7,8,9,10]


def moyenne(tab):
    a = len(tab)
    for t in tab:
        s = t + a
        b = s/t
        return b
    
print(moyenne(tab))