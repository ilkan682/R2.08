from .obj_couleur import Couleur

class Auteur(Couleur):
    nombre_total_auteurs = 0

    def __init__(self, nom, prenom, pays=None, date_naissance=None):
        Auteur.nombre_total_auteurs += 1
        self.id = Auteur.nombre_total_auteurs
        self.nom = nom.upper()
        self.prenom = prenom.capitalize()
        self.pays = pays if pays else "inconnu"
        self.date_naissance = date_naissance if date_naissance else "inconnue"

    def __str__(self):
        return (f"{Auteur.MAGENTA}[{self.id}]{Auteur.NO_COLOR}\t"
                f"{self.prenom} {self.nom} (né(e) le {self.date_naissance} en {self.pays})")

if __name__ == "__main__":
    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    verne = Auteur("VERNE", "Jules", "France", "08/02/1828")
    bridou = Auteur("BRIDOU", "Justin", None, None)
    print(follett)
    print(verne)
    print(bridou)