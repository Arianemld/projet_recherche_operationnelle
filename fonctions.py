
def afficher_tableau(tableau):
    for ligne in tableau:
        ligne_str = ""
        for element in ligne:
            ligne_str += f"{element:15}"  # Permet de définir une certaine largeur des colonnes selon vos besoins
        print(ligne_str)

def lire_et_afficher_fichier_txt(nom_fichier):
    matrice_couts = []
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            ligne = ligne.strip().split()  # Supprimer les espaces en trop et diviser par les espaces
            #ligne = [int(element) if element.isdigit() else float(element) for element in ligne]  # Convertir en int ou float
            matrice_couts.append(ligne)

    print("Matrice des coûts :")
    afficher_tableau(matrice_couts)

def balas_hammer(nom_fichier):
    matrice_couts = []
    min_val_ligne = []
    min_val_colonne = []
    penalites_lignes = []
    penalites_colonnes = []


    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()[1:-1]  # Ignorer la première ligne et la dernière ligne
        for ligne in lignes:
            ligne = ligne.strip().split()  # Supprimer les espaces en trop et diviser par les espaces
            # Ignorer la dernière colonne
            ligne = [int(element) if element.isdigit() else float(element) for element in ligne[:-1]]
            matrice_couts.append(ligne)

            #trier la ligne+récupération des valeurs les plus petites
            ligne.sort()
            min2_val_ligne = ligne[:2]
            min_val_ligne.append(min2_val_ligne)

        #colonne val plsu petite
        nb_colonnes = len(matrice_couts[0])
        for j in range(nb_colonnes):
            colonne = [ligne[j] for ligne in matrice_couts]
            #trier
            colonne.sort()
            min2_val_colonne = colonne[:2]
            min_val_colonne.append(min2_val_colonne)

    print("Matrice sans offres et sans demandes et trier :")
    afficher_tableau(matrice_couts)

    print("Les deux valeurs les plus petites de chaque ligne :")
    for index, valeurs in enumerate(min_val_ligne, 1):
        penalite_ligne = valeurs[1] - valeurs[0]
        penalites_lignes.append(penalite_ligne)
        print(f"Ligne {index} : {valeurs}, Pénalité : {penalite_ligne}")


    print("Les deux valeurs les plus petites de chaque colonne :")
    for index, valeurs in enumerate(min_val_colonne, 1):
        penalite_colonne = valeurs[1] - valeurs[0]
        penalites_colonnes.append(penalite_colonne)
        print(f"Colonne {index} : {valeurs}, Pénalité : {penalite_colonne}")



    max_penalite = max(max(penalites_lignes), max(penalites_colonnes))
    print("La plus grande pénalité est : ", max_penalite)







    return min_val_ligne, min_val_colonne






