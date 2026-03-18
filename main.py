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

# recherche et suppression

def rechercher_livre():
    rech = input("Titre ou auteur à rechercher : ").lower()
    resultats = [l for l in livres if rech in l["titre"].lower() or rech in l["auteur"].lower()]

    if resultats:
        print("\n--- Résultats ---")
        for i, l in enumerate(resultats, 1):
            print(f"{i}. {l['titre']} — {l['auteur']}")
    else:
        print("Aucun livre trouvé.")

def supprimer_livres():
     afficher_livres()
     if not livres:
         return
     try:
         idx = int(input("Numéro à supprimer : ")) - 1
         supprime = livres.pop(idx)
         print(f"✓ '{supprime['titre']}' supprimé.")
     except (ValueError, IndexError):
         print("Numéro invalide.")




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
        elif choix == "3":
            rechercher_livre()
        elif choix == "4":
            supprimer_livres()
        elif choix == "0":
            print("Au revoir")
            break
        else:
            print("Fonctionalité à veinr ")
if __name__ == "__main__":
    main()
