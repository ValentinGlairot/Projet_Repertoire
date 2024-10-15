mon_tuple = (5, 8, 6, 4)
a = mon_tuple[0]
b = mon_tuple[1]
print(f"Valeur de a : {a}")
print(f"Valeur de b : {b}")

mon_tab = [5, 8, 6, 9]
mon_tab[0] = 15
print(f"Tableau modifié : {mon_tab}")

mon_tuple = ("le", "monde", "bonjour")
msg = mon_tuple[2] + ""
print(f"Message : {msg}")

tab = (1, 8, (3, 4), "mardi")
print(f"Tuple complexe : {tab}")

tab = ("Paul", 2008) + ("Axel", 2009)
print(f"Tuple concaténé : {tab}")

t = 3 * ("orange", 6)
print(f"Tuple répété : {t}")
