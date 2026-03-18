# main_poo.py
from models import Livre, Utilisateur, Bibliotheque

bib  = Bibliotheque("Ma Bibliothèque")
user = Utilisateur("Abraham")

def menu_ajouter():
    titre  = input("Titre : ")
    auteur = input("Auteur : ")
    livre  = Livre(titre, auteur)
    bib.ajouter(livre)

def menu_rechercher():
    terme     = input("Titre ou auteur à rechercher : ")
    resultats = bib.rechercher(terme)
    if resultats:
        print(f"{len(resultats)} résultat(s) trouvé(s) :")
        for l in resultats:
            print(f"  {l}")
    else:
        print("Aucun résultat.")

def menu_supprimer():
    bib.afficher()
    if not bib.livres:
        return
    try:
        livre_id = int(input("ID du livre à supprimer : "))
        bib.supprimer(livre_id)
    except ValueError:
        print("Veuillez saisir un nombre.")

def menu_emprunter():
    bib.afficher()
    if not bib.livres:
        return
    try:
        livre_id = int(input("ID du livre à emprunter : "))

        for livre in bib.livres:
            if livre.id == livre_id:
                user.emprunter(livre)
                return
        print("Aucun livre avec cet ID.")
    except ValueError:
        print("Veuillez saisir un nombre.")

def menu_retourner():
    if not user.livres_empruntes:
        print(f"{user.nom} n'a aucun emprunt en cours.")
        return
    print(f" Emprunts de {user.nom} :")
    for l in user.livres_empruntes:
        print(f"  {l}")
    try:
        livre_id = int(input("ID du livre à retourner : "))
        for livre in user.livres_empruntes:
            if livre.id == livre_id:
                user.retourner(livre)
                return
        print("Aucun livre avec cet ID dans vos emprunts.")
    except ValueError:
        print("Veuillez saisir un nombre.")

def main():
    while True:
        print(f"\n===== {bib.nom} — {user.nom} =====")
        print("1. Ajouter un livre")
        print("2. Afficher tous les livres")
        print("3. Rechercher un livre")
        print("4. Supprimer un livre")
        print("5. Emprunter un livre")
        print("6. Retourner un livre")
        print("0. Quitter")
        choix = input("Votre choix : ")

        if choix == "0":
            print("Au revoir !")
            break
        elif choix == "1":
            menu_ajouter()
        elif choix == "2":
            bib.afficher()
        elif choix == "3":
            menu_rechercher()
        elif choix == "4":
            menu_supprimer()
        elif choix == "5":
            menu_emprunter()
        elif choix == "6":
            menu_retourner()
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()