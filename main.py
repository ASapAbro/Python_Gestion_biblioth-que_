# Ajouter et afficher des livres
livres = []
def ajouter_livre():
    titre = input("titre :")
    auteur = input("Auteur :")
    livres.append({"titre": titre, "auteur": auteur})
    print(f"'{titre}' à été ajouté.")


def afficher_livres():
    if not livres:
        print("Aucun livre enregistré.")
        return
    print("\n--- Liste des livres ---")
    for i, livre in enumerate(livres, 1):
        print(f"{i}. {livre['titre']} — {livre['auteur']}")


# menu Itératif

def afficher_menu():
    print("\n===== Bibliothèque =====")
    print("1. Ajouter un livre")
    print("2. Afficher tous les livres")
    print("3. Rechercher un livre")
    print("4. Supprimer un livre")
    print("0. Quitter")
    return input("Votre choix : ")


#point d'entré

def main():
    while True:
        choix = afficher_menu()
        if choix == "1":
            ajouter_livre()
        elif choix == "2":
            afficher_livres()
        elif choix == "0":
            print("Au revoir")
            break
        else:
            print("Fonctionalité à veinr ")
if __name__ == "__main__":
    main()
