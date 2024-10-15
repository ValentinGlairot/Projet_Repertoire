from PIL import Image

def creation_image(couleur, taille=(128, 128)):
    img = Image.new("RGB", taille)
    print(f"Création de l'image de taille {taille} avec la couleur : {couleur}")
    
    for absisse in range(taille[0]):
        for ordonnée in range(taille[1]):
            img.putpixel((absisse, ordonnée), couleur)
            print(f"Pixel en ({absisse}, {ordonnée}) défini avec la couleur : {couleur}")
    
    print("Image créée.")
    img.show()
    print("Image affichée.")

# Test avec une couleur (par exemple, bleu) et une taille de 128x128 pixels
creation_image((0, 0, 255), taille=(128, 128))  # Bleu
