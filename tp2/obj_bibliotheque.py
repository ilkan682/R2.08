import json
from .obj_auteur import Auteur
from .obj_membre import Membre
from .obj_livre import Livre
from .obj_couleur import Couleur

class Bibliotheque(Couleur):
    def __init__(self, fichier_auteurs_json, fichier_livres_json, fichier_membres_json):
        self.fichier_auteurs_json = fichier_auteurs_json
        self.fichier_livres_json = fichier_livres_json
        self.fichier_membres_json = fichier_membres_json
        self.auteurs = []
        self.livres = []
        self.membres = []

    def charger_auteurs(self, flag_affi=False):
        try:
            with open(self.fichier_auteurs_json, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    self.auteurs.append(Auteur(item["nom"], item["prenom"], item["pays"], item["date_naissance"]))
            if flag_affi: print(f"----> {len(self.auteurs)} auteurs chargés.")
        except Exception as e: print(f"Erreur auteurs: {e}")

    def charger_livres(self, flag_affi=False):
        try:
            with open(self.fichier_livres_json, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    auteur = self.check_auteur(item["auteur_nom"], item["auteur_prenom"])
                    if auteur:
                        self.livres.append(Livre(item["titre"], auteur, item["isbn"], item["annee_publication"]))
            if flag_affi: print(f"----> {len(self.livres)} livres chargés.")
        except Exception as e: print(f"Erreur livres: {e}")

    def charger_membres(self, flag_affi=False):
        try:
            with open(self.fichier_membres_json, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    self.membres.append(Membre(item["nom"], item["prenom"], item["date_naissance"]))
            if flag_affi: print(f"----> {len(self.membres)} membres chargés.")
        except Exception as e: print(f"Erreur membres: {e}")

    def check_auteur(self, nom, prenom):
        for auteur in self.auteurs:
            if auteur.nom == nom.upper() and auteur.prenom == prenom.capitalize():
                return auteur
        return None