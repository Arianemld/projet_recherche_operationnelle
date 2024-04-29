#fichier
def lire_fichier(nom_fichier):
    tableau = []
    with open(nom_fichier, 'r') as f:
        for line in f:
            tache = list(map(int, line.strip().split()))
            tableau.append(tache)
    return tableau


def afficher_tableau(tableau):
    for ligne in tableau:
        ligne_str = ""
        for element in ligne:
            ligne_str += f"{element:15}"  # Permet de définir une certaine largeur des colonnes selon vos besoins
        print(ligne_str)


#matrice des couts
def matrice_couts(nom_fichier):
    matrice_couts = []
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            ligne = ligne.strip().split()  # Supprimer les espaces en trop et diviser par les espaces
            #ligne = [int(element) if element.isdigit() else float(element) for element in ligne]  # Convertir en int ou float
            matrice_couts.append(ligne)

    print("Matrice des coûts :")
    afficher_tableau(matrice_couts)


#Nord-ouest
def afficher_offre(tableau):
    offres = [ligne[-1] for ligne in tableau[1:-1]]
    #print("Offres :", offres)
    return offres

def afficher_demande(tableau):
    demande = tableau[-1]
    #print("Demandes :",demande)
    return demande


def nord_ouest(tableau):

    offres = afficher_offre(tableau)
    demandes = afficher_demande(tableau)

    # Initialiser la solution de transport avec des zéros
    solution = [[0] * len(demandes) for _ in range(len(offres))]

    # Indices pour parcourir les lignes et les colonnes
    ligne, colonne = 0, 0

    # Parcourir les offres et les demandes pour allouer les quantités
    for i, offre in enumerate(offres):
        for j, demande in enumerate(demandes):
            quantite = min(offre, demande)
            solution[ligne][colonne] = quantite
            offre -= quantite
            demandes[j] -= quantite  # Mettre à jour les demandes restantes
            colonne += 1  # Passer à la colonne suivante
            if offre == 0:  # Si l'offre est épuisée, passer à la ligne suivante
                break
        ligne += 1  # Passer à la ligne suivante
        colonne = 0  # Revenir à la première colonne

    return solution









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

    #print("Matrice sans offres et sans demandes et trier :")
    #afficher_tableau(matrice_couts)

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






