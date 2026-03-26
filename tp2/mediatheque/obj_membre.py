from .obj_couleur import Couleur

class Membre(Couleur):
    nombre_total_membres = 0

    def __init__(self, nom, prenom, date_naissance):
        Membre.nombre_total_membres += 1
        self.id = Membre.nombre_total_membres
        self.nom = nom.upper()
        self.prenom = prenom.capitalize()
        self.date_naissance = date_naissance
        self.livres_empruntes = []

    def __str__(self):
        return f"{self.prenom} {self.nom} (né(e) le {self.date_naissance})"

    def lister_emprunts(self):
        if not self.livres_empruntes:
            print(f"\t{Membre.ROUGE}----> {self.prenom} {self.nom} n'a aucun livre emprunté.{Membre.NO_COLOR}")
        else:
            print(f"\t{self.prenom} {self.nom} a emprunté les livres suivants :")
            for i, livre in enumerate(self.livres_empruntes, 1):
                print(f"\t\t-{i}. {livre.titre} de {livre.auteur.prenom} {livre.auteur.nom}")

    def emprunter_livre(self, livre):
        if livre.disponible:
            livre.disponible = False
            self.livres_empruntes.append(livre)
            print(f"\t{Membre.VERT}----> Le livre '{livre.titre}' a été emprunté par {self.prenom} {self.nom}.{Membre.NO_COLOR}")
        else:
            print(f"\t{Membre.ROUGE}************ Erreur : Le livre '{livre.titre}' est déjà emprunté.{Membre.NO_COLOR}")

    def restituer_livre(self, livre):
        if livre in self.livres_empruntes:
            livre.disponible = True
            self.livres_empruntes.remove(livre)
            print(f"\t{Membre.VERT}----> Le livre '{livre.titre}' a été restitué par {self.prenom} {self.nom}.{Membre.NO_COLOR}")
        else:
            print(f"\t{Membre.ROUGE}************ Erreur : Ce membre n'a pas emprunté ce livre.{Membre.NO_COLOR}")