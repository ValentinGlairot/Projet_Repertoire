for i in range (5):
 nom=input('Entrez un mot') 
 with open('fichier.txt','a') as f :
     f.write(nom+"\n")
    