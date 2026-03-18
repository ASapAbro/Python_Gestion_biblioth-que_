# classe Livre

class Livre:
    compteur = 1

    def __init__(self, titre, auteur):
        self.id = Livre.compteur
        self.titre = titre
        self.auteur = auteur
        self.disponible = True
        Livre.compteur += 1

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            print(f"'{self.titre}' emprunté.")
        else:
            print(f"'{self.titre}' a déjà été emprunté.")

    def retourner(self):
        if not self.disponible:
            self.disponible = True
            print(f"'{self.titre}' retourné.")
        else:
            print(f"'{self.titre}' est déjà disponible.")

    def __str__(self):
        dispo = "Disponible" if self.disponible else "Emprunté"
        return f"[{self.id}] {self.titre} — {self.auteur} ({dispo})"


# classe Utilisateur

class Utilisateur:

    def __init__(self, nom):
        self.nom = nom
        self.livres_empruntes = []

    def emprunter(self, livre):
        if livre.disponible:
            livre.emprunter()
            self.livres_empruntes.append(livre)
        else:
            print(f"'{livre.titre}' n'est pas disponible.")

    def retourner(self, livre):
        if livre in self.livres_empruntes:
            livre.retourner()
            self.livres_empruntes.remove(livre)
        else:
            print(f"'{livre.titre}' ne fait pas partie de vos emprunts.")

    def __str__(self):
        if not self.livres_empruntes:
            return f"Utilisateur : {self.nom} — aucun emprunt en cours"
        titres = ", ".join(l.titre for l in self.livres_empruntes)
        return f"Utilisateur : {self.nom} — Emprunts en cours : {titres}"



# classe bibliotheque

class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres = []

    def ajouter (self, livre):
        self.livres.append(livre)
        print(f"'{livre.titre}' ajouté à la bibliotheque")

    def supprimer (self, livre_id):
        for livre in self.livres:
            if livre.id == livre_id:
                self.livres.remove(livre)
                print(f"'{livre.titre}' supprimé.")
                return
        print(f" Aucun livre avec l'ID : {livre.id} ")

    def rechercher(self, terme):
        terme = terme.lower()
        resultats = [l for l in self.livres
                     if terme in l.titre.lower()
                     or terme in l.auteur.lower()]
        return resultats

    def afficher(self):
        if not self.livres:
            print("La bibliotheque est vide")
            return
        print(f"\n=== {self.nom} ({len(self.livres)} livres) ===")
        for livre in self.livres:
            print(f"  {livre}")

# class livreClassique

class LivreClassique(Livre):

    def __init__(self, titre, auteur, siecle):
        super().__init__(titre, auteur)
        self.siecle = siecle

    def __str__(self):
        base = super().__str__()
        return base + f" Classique - {self.siecle}'e siecle"


#class livreAudio

class LivreAudio(Livre):

    def __init__(self, titre, auteur, duree_minutes):
        super().__init__(titre, auteur)
        self.duree_minutes = duree_minutes

    def __str__(self):
        base = super().__str__()
        return base + f" Audio - {self.duree_minutes} minutes"

#class bandeDessinee

class BandeDessinee(Livre):
    def __init__(self, titre, auteur, nb_planches):
        super().__init__(titre, auteur)
        self.nb_planches = nb_planches

    def __str__(self):
        base = super().__str__()
        return f"{base} | BD — {self.nb_planches} planches"


#class ebook

class Ebook(Livre):
    def __init__(self, titre, auteur, format_fichier):
        super().__init__(titre, auteur)
        self.format_fichier = format_fichier

    def __str__(self):
        base = super().__str__()
        return f"{base} | Ebook — {self.format_fichier.upper()}"


