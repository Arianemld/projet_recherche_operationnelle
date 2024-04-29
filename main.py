from choix_fichier import choisir_fichier
from fonctions import matrice_couts, balas_hammer, afficher_offre, afficher_demande, lire_fichier, nord_ouest, \
    afficher_tableau


def print_hi(name):

    print("\n                 PROJET - RECHERCHE OPERATIONNELLE\n\n")

    #choix du fichier que l'utilisateur souhaite traiter
    fichier = choisir_fichier()
    print("Vous avez choisi d'analyser le fichier :", fichier)

    #lire fichier txt
    matrice_couts(fichier)
    print()
    tableau = lire_fichier(fichier)
    afficher_offre(tableau)
    print()
    afficher_demande(tableau)
    print()
    solution = nord_ouest(tableau)
    print("\nSolution de transport (Nord-Ouest) :")
    afficher_tableau(solution)
    print()
    balas_hammer(fichier)







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/











# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
