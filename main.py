from choix_fichier import choisir_fichier
from fonctions import lire_et_afficher_fichier_txt, balas_hammer


def print_hi(name):

    print("\n                 PROJET - RECHERCHE OPERATIONNELLE\n\n")

    #choix du fichier que l'utilisateur souhaite traiter
    fichier = choisir_fichier()
    print("Vous avez choisi d'analyser le fichier :", fichier)

    #lire fichier txt
    lire_et_afficher_fichier_txt(fichier)
    balas_hammer(fichier)







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
