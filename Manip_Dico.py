import math

point_de_vie = 15
a = 5
b = 16
c = 3.14 / 2
d = b / a
e = b // a
f = b % a
g = math.pow(a, 2)
h = math.sqrt(b)
i = math.sin(c)

a = "Hello"
b = "World"
mon_expression = a + b
mon_nombre = 5
res = f"Nombre de personnes : {mon_nombre}"

def ma_fontion(x):
    y = 3 * x + 2
    return y

def ma_fonction(x, b):
    y = 4 * x + b
    return y

def annonce(num, prov, dest):
    if dest != "0":
        msg = f"le train n° {num} en provenance de {prov} et à destination de {dest}, entre en gare."
    else:
        msg = f"le train n° {num} en provenance de {prov} entre en gare. Ce train est terminus Triffouillis-les-Oies."
    return msg

print(annonce(4242, "Paris", "0"))
