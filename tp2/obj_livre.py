from .obj_couleur import Couleur
from .obj_auteur import Auteur

class Livre(Couleur):
    nombre_total_livres = 0

    def __init__(self, titre, auteur, isbn=None, annee_publication=None, disponible=True):
        Livre.nombre_total_livres += 1
        self.id = Livre.nombre_total_livres
        self.titre = titre
        self.auteur = auteur  # Doit être une instance de Auteur
        self.isbn = isbn if isbn else "N/A"
        self.annee_publication = annee_publication if annee_publication else "inconnue"
        self.disponible = disponible

    def __str__(self):
        etat = f"{Livre.VERT}Dispo{Livre.NO_COLOR}" if self.disponible else f"{Livre.ROUGE}NON Dispo{Livre.NO_COLOR}"
        return (f"'{self.titre}' de {self.auteur.prenom} {self.auteur.nom} "
                f"(ISBN: {self.isbn}, publié en {self.annee_publication}) - {etat}")

if __name__ == "__main__":
    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    livre_1 = Livre("Les Piliers de la Terre", follett, "9782130428114", "1989")
    print(livre_1)