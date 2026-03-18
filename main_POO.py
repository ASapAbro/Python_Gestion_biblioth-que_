# main_poo.py
from models import (Livre, Utilisateur, Bibliotheque,
                    LivreClassique, LivreAudio, BandeDessinee, Ebook)

bib  = Bibliotheque("Ma Bibliothèque")
user = Utilisateur("Abraham")

def menu_ajouter():
    print("\n--- Type de livre ---")
    print("1. Livre classique")
    print("2. Livre audio")
    print("3. Bande dessinée")
    print("4. Ebook")
    type_choix = input("Votre choix : ")

    titre  = input("Titre : ")
    auteur = input("Auteur : ")

    if type_choix == "1":
        siecle = int(input("Siècle (ex: 19) : "))
        livre  = LivreClassique(titre, auteur, siecle)

    elif type_choix == "2":
        duree = int(input("Durée en minutes : "))
        livre = LivreAudio(titre, auteur, duree)

    elif type_choix == "3":
        planches = int(input("Nombre de planches : "))
        livre    = BandeDessinee(titre, auteur, planches)

    elif type_choix == "4":
        format_fichier = input("Format (pdf/epub/mobi) : ")
        livre          = Ebook(titre, auteur, format_fichier)

    else:
        print("Type invalide.")
        return                        # on sort sans rien ajouter

    bib.ajouter(livre)                # on ajoute le livre créé

def menu_rechercher():
    terme     = input("Titre ou auteur à rechercher : ")
    resultats = bib.rechercher(terme)
    if resultats:
        print(f"\n{len(resultats)} résultat(s) :")
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
    print(f"\nEmprunts de {user.nom} :")
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

def afficher_menu():
    print(f"\n===== {bib.nom} =====")
    print(f"Utilisateur : {user.nom}")
    print(f"Livres disponibles : {len(bib.livres)}")
    print(f"Emprunts en cours  : {len(user.livres_empruntes)}")
    print("─" * 30)
    print("1. Ajouter un livre")
    print("2. Afficher tous les livres")
    print("3. Rechercher un livre")
    print("4. Supprimer un livre")
    print("5. Emprunter un livre")
    print("6. Retourner un livre")
    print("0. Quitter")
    return input("Votre choix : ")

def main():
    while True:
        choix = afficher_menu()

        if   choix == "0": print("Au revoir !"); break
        elif choix == "1": menu_ajouter()
        elif choix == "2": bib.afficher()
        elif choix == "3": menu_rechercher()
        elif choix == "4": menu_supprimer()
        elif choix == "5": menu_emprunter()
        elif choix == "6": menu_retourner()
        else: print("Choix invalide.")

if __name__ == "__main__":
    main()