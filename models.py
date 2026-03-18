# classe Livres

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
            print(f"'{self.titre}'emprunter")
        else:
            print(f"'{self.titre}' à deja été emprunter")


    def retourner(self):
        if self.disponible:
            self.disponible = True
            print(f"'{self.titre}'retourner")
        else:
            print(f"'{self.titre}'est deja disponible'")

    def __str__(self):
        dispo = "Disponible" if self.disponible else "Emprunter"
        return f"Livres: {self.id}, {self.titre}, {self.auteur} ({dispo})"



# classe Utilisateur







# classe Bibliothèque








# classe Livres