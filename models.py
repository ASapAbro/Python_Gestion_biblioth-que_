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
            print("'{self.titre}' emprunté.")
        else:
            print("'{self.titre}' a déjà été emprunté.")

    def retourner(self):
        if not self.disponible:
            self.disponible = True
            print("'{self.titre}' retourné.")
        else:
            print(f"'{self.titre}' est déjà disponible.")

    def __str__(self):
        dispo = "Disponible" if self.disponible else "Emprunté"
        return "[{self.id}] {self.titre} — {self.auteur} ({dispo})"


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
            return "Utilisateur : {self.nom} — aucun emprunt en cours"
        titres = ", ".join(l.titre for l in self.livres_empruntes)
        return "Utilisateur : {self.nom} — Emprunts en cours : {titres}"

