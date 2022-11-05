import os

# Créer un répertoire save si il n' existe pas
os.makedirs(name="save", exist_ok=True)

# Créer un fichier save.txt si il n' existe pas
path = 'save/save.txt'

with open(path, 'a+') as file:  # Ouverture du Fichier en mode ajout
    size = os.path.getsize(path)  # Size récupère la taille du fichier
    if size == 0:  # Si le fichier est vide
        gender = str(input("Monsieur ou Madame ? "))
        name = str(input("Veuillez saisir votre nom ? "))
        file.write(gender+" "+name)  # Insertion dans le fichier

file.close()
file2 = open(path, 'r') # Ouverture du Fichier en mode lecture
print("Bonjour", file2.read())
file2.close()
