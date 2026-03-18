def afficher_menu():
    print("\n===== Bibliothèque =====")
    print("1. Ajouter un livre")
    print("2. Afficher tous les livres")
    print("3. Rechercher un livre")
    print("4. Supprimer un livre")
    print("0. Quitter")
    return input("Votre choix : ")

def main():
    while True:
        choix = afficher_menu()
        if choix == "0":
            print("Au revoir")
            break
        else:
            print("Fonctionalité à veinr ")
if __name__ == "__main__":
    main()